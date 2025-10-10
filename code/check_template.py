
import sys
from pathlib import Path
import pandas as pd

REQUIRED_DIRS = ["builder", "code", "conditions", "stimuli", "triggers", "data", "logs", "docs"]

def main():
    root = Path(".")
    missing = [d for d in REQUIRED_DIRS if not (root / d).exists()]
    if missing:
        print("[error] Missing required directories:", ", ".join(missing))
        sys.exit(1)

    # Validate example conditions
    cond = root / "conditions" / "example_conditions.csv"
    if not cond.exists():
        print("[error] Missing example conditions:", cond)
        sys.exit(2)

    try:
        df = pd.read_csv(cond)
    except Exception as e:
        print("[error] Failed reading example_conditions.csv:", e)
        sys.exit(3)

    expected_cols = {"trial","n_back","flanker_center","flanker_array","correct_response","isi_ms","stim_ms"}
    if not expected_cols.issubset(df.columns):
        print("[error] example_conditions.csv is missing columns:", expected_cols - set(df.columns))
        sys.exit(4)

    # Validate example triggers (optional)
    trig = root / "triggers" / "example_triggers.tsv"
    if trig.exists():
        try:
            tdf = pd.read_csv(trig, sep="\t")
        except Exception as e:
            print("[error] Failed reading example_triggers.tsv:", e)
            sys.exit(5)
        needed = {"event_name","event_code","description"}
        if not needed.issubset(tdf.columns):
            print("[error] example_triggers.tsv missing columns:", needed - set(tdf.columns))
            sys.exit(6)

    print("Template structure looks good.")
    sys.exit(0)

if __name__ == "__main__":
    main()
