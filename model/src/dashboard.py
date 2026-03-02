import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import threading
import time
import sys

# Add project root to path to import utils and processor
sys.path.append('/home/italiano/projects/my-nova-mktg-crew')
from utils.file_utils import list_cohorts
from data.src.dynamic_processor import process_cohort_data

# Auto-shutdown pattern
def shutdown():
    time.sleep(300)
    os._exit(0)
threading.Thread(target=shutdown, daemon=True).start()

# Page Config - Sidebar collapsed by default
st.set_page_config(page_title="Become an Agentic Architect", layout="wide", initial_sidebar_state="collapsed")

# Sidebar - Cohort Selection
st.sidebar.header("Cohort Management")
base_cohorts_path = '/home/italiano/projects/my-nova-mktg-crew/project-context/analysis/raw/cohorts'
available_cohorts = sorted(list_cohorts(base_cohorts_path))

if not available_cohorts:
    st.error("No cohorts found in the raw data directory.")
    st.stop()

selected_cohort = st.sidebar.selectbox("Select Cohort", options=available_cohorts, index=available_cohorts.index('3') if '3' in available_cohorts else 0)

# Load and Process Data
@st.cache_data(show_spinner="Processing cohort data...")
def get_data(cohort_id):
    # Trigger processing of latest files
    success = process_cohort_data(cohort_id)
    if not success:
        return None, None, None
        
    base_path = '/home/italiano/projects/my-nova-mktg-crew/data/processed'
    df_enriched = pd.read_csv(os.path.join(base_path, f'cohort{cohort_id}_students_enriched.csv'))
    
    trends_path = os.path.join(base_path, f'cohort{cohort_id}_daily_trends.csv')
    df_trends = pd.read_csv(trends_path) if os.path.exists(trends_path) else pd.DataFrame()
    
    matrix_path = os.path.join(base_path, f'cohort{cohort_id}_syllabus_matrix.csv')
    df_matrix = pd.read_csv(matrix_path) if os.path.exists(matrix_path) else None
    
    return df_enriched, df_trends, df_matrix

df, df_trends, df_matrix = get_data(selected_cohort)

if df is None:
    st.error(f"Failed to load data for Cohort {selected_cohort}. Please check the raw data files.")
    st.stop()

# Sidebar Filters
st.sidebar.header("Filters")
tier_filter = st.sidebar.multiselect("Select Engagement Tier", options=df['Engagement Tier'].unique(), default=df['Engagement Tier'].unique())
at_risk_filter = st.sidebar.selectbox("Show At-Risk Only?", options=["All", "Yes", "No"])

# Filter Data
filtered_df = df[df['Engagement Tier'].isin(tier_filter)]
if at_risk_filter == "Yes":
    filtered_df = filtered_df[filtered_df['At-Risk'] == True]
elif at_risk_filter == "No":
    filtered_df = filtered_df[filtered_df['At-Risk'] == False]

# Dashboard Header
st.title(f"🎓 Become an Agentic Architect - Cohort {selected_cohort}")
st.markdown(f"**Cohort Start Date:** Feb 23, 2026 | **Current Status:** Week 1 (Foundations & Project 1)")

# Create Tabs
tab1, tab2, tab3 = st.tabs(["📊 Engagement Overview", "🎯 Syllabus Progress", "🏆 Student Leaderboard"])

with tab1:
    st.markdown("---")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Students", len(df))
    col2.metric("At-Risk Students", int(df['At-Risk'].sum()))
    col3.metric("Avg Engagement Score", f"{df['Engagement Score'].mean():.2f}")
    col4.metric("Total Projects Submitted", int(df['Projects Submitted'].sum()))

    st.markdown("---")

    # Visualizations
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.subheader("Engagement Tier Distribution")
        fig_tier = px.pie(df, names='Engagement Tier', color='Engagement Tier',
                         color_discrete_map={'High': 'green', 'Medium': 'orange', 'Low': 'red'})
        st.plotly_chart(fig_tier, use_container_width=True)

    with row1_col2:
        st.subheader("Daily Activity Trends (Views)")
        if not df_trends.empty:
            fig_trend = px.line(df_trends, x='Date', y='View Count', title="Course Content Views Over Time")
            st.plotly_chart(fig_trend, use_container_width=True)
        else:
            st.info("No trend data available for this cohort.")

    st.markdown("---")

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.subheader("Engagement Score vs Projects Submitted")
        fig_scatter = px.scatter(filtered_df, x='Engagement Score', y='Projects Submitted', 
                                 color='Engagement Tier', hover_name='Name', size='Module Item Views')
        st.plotly_chart(fig_scatter, use_container_width=True)

    with row2_col2:
        st.subheader("At-Risk Analysis")
        at_risk_summary = df['At-Risk'].value_counts().reset_index()
        at_risk_summary.columns = ['Status', 'Count']
        at_risk_summary['Status'] = at_risk_summary['Status'].map({True: 'At-Risk', False: 'Healthy'})
        fig_at_risk = px.bar(at_risk_summary, x='Status', y='Count', color='Status',
                             color_discrete_map={'At-Risk': 'red', 'Healthy': 'blue'})
        st.plotly_chart(fig_at_risk, use_container_width=True)

    st.markdown("---")

    # Student Detail Table
    st.subheader("Student Engagement Details")
    st.dataframe(filtered_df[['Name', 'Email', 'Engagement Score', 'Engagement Tier', 'At-Risk', 'Projects Submitted', 'Module Item Views', 'Community Posts']], 
                 use_container_width=True)

    # Download Button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Filtered Data", data=csv, file_name=f"cohort{selected_cohort}_engagement_filtered.csv", mime="text/csv")

with tab2:
    st.markdown("---")
    # Syllabus Progress Visualization
    st.subheader("🎯 Syllabus Progress")
    
    # 1st Row: Milestones
    st.info("""
    **Week 1 Milestones (Foundations & Project 1):**
    - ✅ **Module Views**: At least 3 items viewed (Foundations, Agentic Loop, CrewAI Setup).
    - ✅ **Participation**: At least 1 Community Post or Zoom Join Click.
    - 🎯 **Goal**: Define Project 1 (Problem Statement & Initial Scope).
    """)

    # 2nd Row: Aligned Charts
    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        on_track_count = df['On-Track'].sum()
        on_track_pct = (on_track_count / len(df)) * 100
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = on_track_pct,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "% Students On-Track", 'font': {'size': 20}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': 'red'},
                    {'range': [50, 80], 'color': 'orange'},
                    {'range': [80, 100], 'color': 'green'}],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        
        fig_gauge.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with row2_col2:
        on_track_summary = df['On-Track'].value_counts().reset_index()
        on_track_summary.columns = ['Status', 'Count']
        on_track_summary['Status'] = on_track_summary['Status'].map({True: 'On-Track', False: 'Behind'})
        fig_on_track = px.bar(on_track_summary, x='Status', y='Count', color='Status',
                             color_discrete_map={'On-Track': 'green', 'Behind': 'red'},
                             text='Count', title="Student Status vs Week 1 Goals")
        fig_on_track.update_layout(height=350)
        st.plotly_chart(fig_on_track, use_container_width=True)

    # 3rd Row: Module/Project Tracking Matrix
    st.markdown("---")
    st.subheader("📋 Module & Project Completion Matrix")
    if df_matrix is not None:
        # Create a display version of the matrix
        display_matrix = df_matrix.copy()
        
        def color_status(val):
            if val == 'On-Time': 
                return 'background-color: #c6efce; color: black' # Light Green
            elif val == 'Late': 
                return 'background-color: #ffeb9c; color: black' # Light Yellow
            elif val == 'Missing': 
                return 'background-color: #ffc7ce; color: black' # Light Red
            elif val == 'Pending' or val == "" or pd.isna(val):
                return 'background-color: black; color: black'
            return ''

        st.dataframe(display_matrix.style.applymap(color_status, subset=display_matrix.columns[2:]), use_container_width=True)
    else:
        st.warning("Syllabus matrix data not found for this cohort.")

with tab3:
    st.subheader("🏆 Student Leaderboard")
    st.markdown("Celebrating our most active learners! Points are calculated based on module views, project submissions, community participation, and event attendance.")
    
    # Prepare Leaderboard Data
    leaderboard_df = df.copy()
    
    # Sort by Points descending
    leaderboard_df = leaderboard_df.sort_values(by='Points', ascending=False)
    
    # Select and rename columns for display - Privacy Centric (No Email, No Tier)
    display_cols = ['Name', 'Points', 'Projects Submitted', 'Module Item Views', 'Community Posts']
    leaderboard_display = leaderboard_df[display_cols].reset_index(drop=True)
    leaderboard_display.index += 1 # Rank starting from 1
    
    st.table(leaderboard_display)
