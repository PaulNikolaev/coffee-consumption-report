import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "main.py", *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


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


def test_cli_returns_error_for_unknown_report() -> None:
    result = run_cli(
        "--files",
        "data/stats1.csv",
        "--report",
        "unknown",
    )

    assert result.returncode == 1
    assert "Unknown report: unknown" in result.stderr
