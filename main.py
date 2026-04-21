import sys
from pathlib import Path


PROJECT_SRC = Path(__file__).resolve().parent / "src"

if str(PROJECT_SRC) not in sys.path:
    # Allow running `python main.py` without installing the package first.
    sys.path.insert(0, str(PROJECT_SRC))

from coffee_report.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
