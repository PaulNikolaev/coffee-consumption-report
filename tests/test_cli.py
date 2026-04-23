from pathlib import Path
import subprocess
import sys

from coffee_report import cli

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "main.py", *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


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


def test_run_builds_sorted_report_from_merged_files(tmp_path: Path) -> None:
    first_csv = tmp_path / "stats1.csv"
    second_csv = tmp_path / "stats2.csv"
    write_csv(
        first_csv,
        [
            "Lower CTR,17.0,35,100,10,4.1",
            "Filtered out,14.0,20,100,10,4.1",
        ],
    )
    write_csv(
        second_csv,
        [
            "Higher CTR,24.0,30,100,10,4.1",
            "Rejected by retention,30.0,40,100,10,4.1",
        ],
    )

    result = cli.run(
        ["--files", str(first_csv), str(second_csv), "--report", "clickbait"]
    )

    lines = result.splitlines()
    headers = [cell.strip() for cell in lines[0].split("|")[1:-1]]

    assert headers == ["title", "ctr", "retention_rate"]
    assert "views" not in result
    assert lines[2] == "| Higher CTR | 24.0  | 30.0             |"
    assert lines[3] == "| Lower CTR  | 17.0  | 35.0             |"


def test_cli_builds_clickbait_report_from_multiple_files() -> None:
    result = run_cli(
        "--files",
        "data/stats1.csv",
        "data/stats2.csv",
        "--report",
        "clickbait",
    )

    assert result.returncode == 0
    assert "title" in result.stdout
    assert "ctr" in result.stdout
    assert "retention_rate" in result.stdout
    assert "Секрет который скрывают тимлиды" in result.stdout
    assert "Почему продакшн упал в пятницу вечером" in result.stdout
    assert "25.0" in result.stdout
    assert "21" in result.stdout
    assert result.stderr == ""
