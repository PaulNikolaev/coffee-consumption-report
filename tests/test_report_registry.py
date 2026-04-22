import pytest

from coffee_report.exceptions import UnknownReportError
from coffee_report.reports import get_report, get_supported_report_names


def test_get_supported_report_names_returns_clickbait() -> None:
    assert get_supported_report_names() == ("clickbait",)


def test_get_report_returns_clickbait_report_for_supported_name() -> None:
    report = get_report("clickbait")

    assert report.name == "clickbait"


def test_get_report_raises_clear_error_for_unknown_name() -> None:
    with pytest.raises(UnknownReportError, match="Available reports: clickbait"):
        get_report("unknown")
