from coffee_report.exceptions import UnknownReportError
from coffee_report.reports.base import BaseReport
from coffee_report.reports.clickbait import ClickbaitReport

REPORTS: dict[str, type[BaseReport]] = {
    ClickbaitReport.name: ClickbaitReport,
}


def get_supported_report_names() -> tuple[str, ...]:
    """Return all supported report names."""
    return tuple(REPORTS)


def get_report(report_name: str) -> BaseReport:
    """Return the report instance for the requested name."""
    normalized_name = report_name.strip().lower()
    report_class = REPORTS.get(normalized_name)

    if report_class is None:
        raise UnknownReportError(report_name, get_supported_report_names())

    return report_class()
