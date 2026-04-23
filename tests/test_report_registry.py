import pytest

from coffee_report.exceptions import UnknownReportError
from coffee_report.reports import get_report


def test_get_report_raises_clear_error_for_unknown_name() -> None:
    with pytest.raises(UnknownReportError, match="Available reports: clickbait"):
        get_report("unknown")
