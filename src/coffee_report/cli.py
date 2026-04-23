import argparse
import sys
from collections.abc import Sequence

from coffee_report.csv_reader import read_csv_files
from coffee_report.exceptions import CoffeeReportError
from coffee_report.output import render_report_table
from coffee_report.reports import get_report, get_supported_report_names


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI parser for report generation."""
    parser = argparse.ArgumentParser(
        prog="coffee-report",
        description="Build coffee consumption reports from CSV files.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="One or more input CSV files.",
    )
    parser.add_argument(
        "--report",
        required=True,
        help=(
            "Report name to build. "
            f"Supported values: {', '.join(get_supported_report_names())}."
        ),
    )
    return parser


def run(argv: Sequence[str] | None = None) -> str:
    """Run the reporting workflow and return the formatted table."""
    parser = build_parser()
    args = parser.parse_args(argv)
    records = read_csv_files(args.files)
    report = get_report(args.report)
    rows = report.build(records)
    return render_report_table(rows)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI entrypoint and return a process exit code."""
    try:
        report_output = run(argv)
    except CoffeeReportError as error:
        print(str(error), file=sys.stderr)
        return 1

    print(report_output)
    return 0
