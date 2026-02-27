# Git & Git LFS

This repo uses **Git LFS** for large files (`.mp4`, `.mp3`, `.pdf`, `.png`, `.pptx`).

## First-time push (this repo was committed without LFS)

Because the initial commit was made without Git LFS installed, you need to migrate existing history so large files are stored in LFS before pushing to GitHub (which rejects files over 100 MB).

1. **Install [Git LFS](https://git-lfs.com)** (e.g. `brew install git-lfs` or see git-lfs.com).

2. **Enable LFS in this repo:**
   ```bash
   git lfs install
   ```

3. **Rewrite history to use LFS** for the tracked types:
   ```bash
   git lfs migrate import --include="*.mp4,*.mp3,*.pdf,*.png,*.pptx" --everything
   ```

4. **Push to remote:**
   ```bash
   git push -u origin main
   ```

## After that (or after a fresh clone)

Run once per machine:

```bash
git lfs install
```

Then add, commit, and push as usual. LFS will handle the large assets automatically.
