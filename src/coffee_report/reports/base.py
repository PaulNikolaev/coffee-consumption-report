from abc import ABC, abstractmethod
from collections.abc import Sequence

from coffee_report.models import VideoMetrics

ReportRow = dict[str, object]


class BaseReport(ABC):
    """Common contract for all report implementations."""

    name: str

    @abstractmethod
    def build(self, records: Sequence[VideoMetrics]) -> list[ReportRow]:
        """Build a report from normalized video metrics."""
