from collections.abc import Mapping, Sequence

from tabulate import tabulate

from coffee_report.reports.base import ReportRow

REPORT_COLUMNS = ("title", "ctr", "retention_rate")


def render_report_table(rows: Sequence[ReportRow]) -> str:
    """Render report rows as a console table with fixed columns."""
    normalized_rows = [
        _select_report_columns(row)
        for row in rows
    ]
    return tabulate(
        normalized_rows,
        headers="keys",
        tablefmt="github",
        disable_numparse=True,
    )


def _select_report_columns(row: Mapping[str, object]) -> ReportRow:
    return {column: row[column] for column in REPORT_COLUMNS}
