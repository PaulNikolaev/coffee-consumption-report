from coffee_report.models import VideoMetrics
from coffee_report.reports.clickbait import ClickbaitReport


def make_record(
        title: str,
        ctr: float,
        retention_rate: float,
) -> VideoMetrics:
    return VideoMetrics(
        title=title,
        ctr=ctr,
        retention_rate=retention_rate,
        views=1000,
        likes=100,
        avg_watch_time=5.0,
    )


def test_clickbait_report_filters_sorts_and_limits_columns() -> None:
    report = ClickbaitReport()
    records = [
        make_record("Qualified B", ctr=16.2, retention_rate=39.5),
        make_record("Rejected by ctr", ctr=15.0, retention_rate=22.0),
        make_record("Qualified A", ctr=22.4, retention_rate=31.0),
        make_record("Rejected by retention", ctr=25.0, retention_rate=40.0),
    ]

    result = report.build(records)

    assert result == [
        {
            "title": "Qualified A",
            "ctr": 22.4,
            "retention_rate": 31.0,
        },
        {
            "title": "Qualified B",
            "ctr": 16.2,
            "retention_rate": 39.5,
        },
    ]
