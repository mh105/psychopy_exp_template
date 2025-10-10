
# PsychoPy Task Template (GitHub Template Ready)

A minimal, lab-friendly template for building **PsychoPy-based** experiments (Builder or Coder) with a clean folder layout, reproducible environments, and basic CI checks. Use this as a **GitHub template** so new tasks start from a consistent scaffold.

---

## 🚀 Quick Start

### 1) Create the template repo on GitHub
1. Go to **GitHub → New repository**.
2. Name it something like `psychopy-task-template`.
3. **Check “Template repository.”**
4. Add a README, choose a license (MIT recommended), and create the repo.

> If you’re reading this locally, push these files to that repo and enable the template toggle in **Settings → General → Template repository**.

### 2) Clone and set up locally
```bash
git clone https://github.com/<you>/psychopy-task-template.git
cd psychopy-task-template
```

Use **Conda** (recommended) or **pip**:

**Conda**
```bash
conda env create -f environment.yml
conda activate psychopy-tmpl
```

**pip**
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Verify the template works
```bash
python code/check_template.py
```
You should see `Template structure looks good.`

### 4) Open in PsychoPy (Builder users)
- Put your `.psyexp` files into `builder/` (an example placeholder is there).
- Open **PsychoPy → Builder** and load your task.

### 5) Run the example Python entry point (Coder users)
```bash
python code/run_task.py --participant TEST --session 1
```
This script demonstrates basic CLI args, condition loading, and a safe import pattern for PsychoPy.

---

## 📁 Folder Layout

```
.
├─ builder/                # Your .psyexp Builder files live here
├─ code/                   # Python utilities / main runner scripts
├─ conditions/             # CSV/TSV condition files
├─ stimuli/                # Images/audio/video (consider Git LFS)
├─ triggers/               # Trigger maps (e.g., LSL, parallel port)
├─ data/                   # Output data (gitignored)
├─ logs/                   # Log files (gitignored)
├─ docs/                   # Setup/how-to docs
└─ .github/workflows/      # CI checks
```

---

## 🧪 CI (GitHub Actions)

This template includes a tiny CI workflow that runs `code/check_template.py` on each push/PR to ensure
required folders and example files exist. It’s lightweight (no heavy PsychoPy install).

If you later want to run Builder headlessly or add unit tests, add steps here as needed.

---

## 🧩 Using This as a Template (for new tasks)

1. In GitHub, click **Use this template** (green button).
2. Name your new repo (e.g., `flanker-nback-2025`).
3. Clone it and start adding your task:
   - Add `.psyexp` to `builder/`
   - Add `conditions/*.csv`
   - Add `triggers/*.tsv`
   - Put stimuli under `stimuli/` (and run `git lfs track "*.wav"`, etc.)
4. Update the README for the specific task.

---

## 🔌 Triggers & Conditions

- **Conditions** go in `conditions/`. See `example_conditions.csv` for columns typically used (`trial`, `n_back`, `flanker_center`, `flanker_array`, `correct_response`, etc.).
- **Triggers** go in `triggers/`. See `example_triggers.tsv` for time-based or event-code maps; adapt for **LSL**, **parallel port**, or your device.

---

## 🧰 Local Tips

- Install **Git LFS** if you store large binary assets (audio/video/images):
  ```bash
  git lfs install
  git lfs track "*.wav" "*.mp4" "*.png" "*.jpg"
  git add .gitattributes
  git commit -m "chore: track large assets with LFS"
  ```
- Keep raw data out of Git (already gitignored).
- Use branches + PRs; consider protecting `main` in repo **Settings → Branches**.

---

## 📝 License

MIT by default—change if your lab requires something else.
