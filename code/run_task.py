
import argparse
import os
import sys
import time
from pathlib import Path
import pandas as pd

def safe_import_psychopy():
    try:
        import psychopy  # noqa: F401
        from psychopy import visual, core, event  # type: ignore
        return visual, core, event
    except Exception as e:
        print("[warn] PsychoPy not available or failed to import:", e)
        return None, None, None

def load_conditions(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Conditions file not found: {path}")
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in (".tsv", ".tab"):
        return pd.read_csv(path, sep="\t")
    raise ValueError(f"Unsupported conditions file type: {path.suffix}")

def main():
    parser = argparse.ArgumentParser(description="Minimal PsychoPy task runner (template).")
    parser.add_argument("--participant", required=True, help="Participant ID")
    parser.add_argument("--session", type=int, default=1, help="Session number")
    parser.add_argument("--conditions", default="conditions/example_conditions.csv", help="Path to conditions CSV/TSV")
    args = parser.parse_args()

    conditions_path = Path(args.conditions)
    df = load_conditions(conditions_path)
    print(f"[info] Loaded {len(df)} condition rows from {conditions_path}")

    # Create output folder
    out_dir = Path("data")
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d-%H%M%S")
    out_csv = out_dir / f"{args.participant}_ses-{args.session}_{ts}.csv"

    # Try PsychoPy display (optional)
    visual, core, event = safe_import_psychopy()
    if visual is None:
        print("[info] Skipping visual demo because PsychoPy is not available.")
        # Save minimal provenance + first few rows
        df.head(5).to_csv(out_csv, index=False)
        print(f"[info] Wrote demo data to {out_csv}")
        return

    # Minimal welcome screen demo
    win = visual.Window(size=(800, 600), fullscr=False, units='pix')
    msg = visual.TextStim(win, text=f"Welcome {args.participant}!\nSession {args.session}\nPress any key to exit demo.", height=28)
    msg.draw()
    win.flip()
    event.waitKeys()
    win.close()
    core.quit()

if __name__ == "__main__":
    main()
