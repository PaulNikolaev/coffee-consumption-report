from pathlib import Path

import pytest

from coffee_report.csv_reader import read_csv_file, read_csv_files
from coffee_report.exceptions import InputFileNotFoundError
from coffee_report.models import VideoMetrics


def write_csv(path: Path, rows: list[str]) -> None:
    path.write_text(
        "\n".join(
            [
                "title,ctr,retention_rate,views,likes,avg_watch_time",
                *rows,
            ]
        ),
        encoding="utf-8",
    )


def test_read_csv_file_returns_typed_records(tmp_path: Path) -> None:
    csv_path = tmp_path / "stats.csv"
    write_csv(csv_path, ["Video A,18.5,42,1000,120,4.7"])

    records = read_csv_file(csv_path)

    assert records == [
        VideoMetrics(
            title="Video A",
            ctr=18.5,
            retention_rate=42.0,
            views=1000,
            likes=120,
            avg_watch_time=4.7,
        )
    ]


def test_read_csv_files_combines_rows_from_all_files(tmp_path: Path) -> None:
    first_csv = tmp_path / "stats1.csv"
    second_csv = tmp_path / "stats2.csv"
    write_csv(first_csv, ["Video A,18.5,42,1000,120,4.7"])
    write_csv(second_csv, ["Video B,21.0,35,2500,340,5.1"])

    records = read_csv_files([first_csv, second_csv])

    assert [record.title for record in records] == ["Video A", "Video B"]


def test_read_csv_file_raises_clear_error_for_missing_path(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.csv"

    with pytest.raises(InputFileNotFoundError, match="Input CSV file does not exist"):
        read_csv_file(missing_path)
