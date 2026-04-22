from collections.abc import Sequence

from coffee_report.exceptions import UnknownReportError
from coffee_report.models import VideoMetrics
from coffee_report.reports.base import BaseReport, ReportRow


class ClickbaitReport(BaseReport):
    """Placeholder report reserved for the clickbait implementation."""

    name = "clickbait"

    def build(self, records: Sequence[VideoMetrics]) -> list[ReportRow]:
        raise NotImplementedError(
            "The clickbait report implementation will be added in the next stage."
        )


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
