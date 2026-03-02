# Student Engagement Metrics Documentation

## Overview
This document outlines the metrics and logic used in the Student Engagement Dashboard for the "Become an Agentic Architect" program. The dashboard is designed to track student progress, identify at-risk learners, and celebrate high achievers across multiple cohorts.

## Core Metrics

### 1. Engagement Score
The primary quantitative measure of a student's activity.
- **Formula**: `(Module Item Views * 1) + (Projects Submitted * 50) + (Community Posts * 10) + (Zoom Join Clicks * 5) + (Events Attended * 20)`
- **Purpose**: Provides a weighted activity index where high-impact actions (projects, events) carry more weight than passive consumption (views).

### 2. Points
A scale used for the Student Leaderboard.
- **Formula**: `Same as Engagement Score`
- **Purpose**: Presents engagement in a clear, unweighted point system for gamification.

### 3. Engagement Tier
Categorizes students based on their Engagement Score.
- **High**: Score > 100
- **Medium**: 30 < Score <= 100
- **Low**: Score <= 30

### 4. At-Risk Status
Identifies students who may need additional support or intervention.
- **Logic**: A student is flagged as "At-Risk" if they are in the **Low** Engagement Tier OR have **0** Projects Submitted.
- **Interpretation**: Even if a student is viewing modules, failure to submit projects is a critical indicator of falling behind in an application-heavy program.

### 5. On-Track Status
A binary indicator for meeting minimum weekly expectations.
- **Logic**: A student is "On-Track" if they have completed all tasks from previous weeks (even if "Late" relative to original deadlines) and have no "Missing" items.
- **Interpretation**: Late completion of historical weeks does not disqualify "On-Track" status for the current reporting period. A student is only "Behind" if they have uncompleted tasks from weeks that have fully passed (pre-Monday of the current week).
- **Example**: Queen Osuji completed Week 0 modules late but has started Week 1 activities. Since she has no "Missing" items from past weeks, she is classified as "On-Track".

## Syllabus Completion Matrix Logic

The matrix tracks completion of specific milestones defined in the program syllabus.

### Status Definitions:
- **On-Time (Green)**: The student viewed/completed the milestone item before the Sunday 23:59 deadline of the assigned week.
- **Late (Yellow)**: The student completed the item, but after the assigned week's deadline.
- **Missing (Red)**: The deadline has passed, and no record of completion exists.
- **Pending (Black)**: The deadline has not yet passed, and the student has not yet completed the item.

### Date Boundaries:
- **Cohort Start**: Feb 23, 2026 (Monday)
- **Week 1 Deadline**: March 1, 2026 (Sunday, 23:59)
- **Week 2 Deadline**: March 8, 2026 (Sunday, 23:59)
- ...and so on.
- **Week 0**: Items expected to be completed before the official start date (Deadline: Feb 22, 2026).

## Dynamic Data Loading
The dashboard automatically scans the `project-context/analysis/raw/cohorts/COHORT#` directory and selects the files with the latest timestamp for each metric type (e.g., `active_students_over_time`, `module_item_view_detail`). This ensures the dashboard always reflects the most recent data uploaded to the project.
