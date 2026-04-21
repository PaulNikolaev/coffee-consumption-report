from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True, slots=True)
class VideoMetrics:
    """Normalized CSV row used inside the application."""

    title: str
    ctr: float
    retention_rate: float
    views: int
    likes: int
    avg_watch_time: float

    @classmethod
    def from_csv_row(cls, row: Mapping[str, str]) -> "VideoMetrics":
        """Build a typed model from a CSV row."""
        return cls(
            title=row["title"],
            ctr=float(row["ctr"]),
            retention_rate=float(row["retention_rate"]),
            views=int(row["views"]),
            likes=int(row["likes"]),
            avg_watch_time=float(row["avg_watch_time"]),
        )
