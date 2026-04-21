import csv
from collections.abc import Sequence
from pathlib import Path

from coffee_report.exceptions import InputFileNotFoundError
from coffee_report.models import VideoMetrics


def read_csv_file(path: str | Path) -> list[VideoMetrics]:
    """Read one CSV file and return normalized records."""
    file_path = Path(path)

    if not file_path.is_file():
        raise InputFileNotFoundError(file_path)

    with file_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        return [VideoMetrics.from_csv_row(row) for row in reader]


def read_csv_files(paths: Sequence[str | Path]) -> list[VideoMetrics]:
    """Read multiple CSV files and combine their rows."""
    records: list[VideoMetrics] = []

    for path in paths:
        records.extend(read_csv_file(path))

    return records
