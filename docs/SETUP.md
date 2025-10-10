
# Lab Setup Notes (PsychoPy Template)

## Environments
- Prefer **Conda** for easier installs on Windows.
- Pin PsychoPy to a known good version for your lab (e.g., `psychopy==2024.2.*`) in `requirements.txt` once validated.
- Some hardware integrations (e.g., parallel port) require admin drivers; document that in your task README.

## PsychoPy Builder
- Save your task `.psyexp` inside `builder/`.
- Export the auto-generated `.py` for versioning if needed (optional).
- Store stimuli under `stimuli/` and conditions under `conditions/`.

## Triggers
- Keep a single source-of-truth TSV/CSV in `triggers/` with columns like:
  - `event_name`, `event_code`, `lsl_stream`, `port`, `description`
- Create a tiny helper (`code/triggers.py`) to send triggers consistently.

## Data
- Writes to `data/` (gitignored). Consider CSV or Parquet for portability.
- Include `participant`, `session`, `run`, timestamps, and task provenance in each row.

## Validation
- Add assertions and sanity checks to `code/check_template.py` as the template evolves.
- Consider a nightly CI that validates conditions/triggers format across tasks that use this template.
