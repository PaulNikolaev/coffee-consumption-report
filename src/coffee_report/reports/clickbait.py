from collections.abc import Sequence

from coffee_report.models import VideoMetrics
from coffee_report.reports.base import BaseReport, ReportRow


class ClickbaitReport(BaseReport):
    """Report with videos that have suspiciously high CTR and low retention."""

    name = "clickbait"

    def build(self, records: Sequence[VideoMetrics]) -> list[ReportRow]:
        filtered_records = [
            record
            for record in records
            if record.ctr > 15 and record.retention_rate < 40
        ]
        sorted_records = sorted(
            filtered_records,
            key=lambda record: record.ctr,
            reverse=True,
        )
        return [
            {
                "title": record.title,
                "ctr": record.ctr,
                "retention_rate": record.retention_rate,
            }
            for record in sorted_records
        ]
