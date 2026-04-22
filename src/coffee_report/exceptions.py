from pathlib import Path


class CoffeeReportError(Exception):
    """Base exception for the application."""


class InputFileNotFoundError(CoffeeReportError):
    """Raised when a requested CSV file does not exist."""

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        message = f"Input CSV file does not exist: {file_path}"
        super().__init__(message)


class UnknownReportError(CoffeeReportError):
    """Raised when a requested report name is not supported."""

    def __init__(self, report_name: str, available_reports: tuple[str, ...]) -> None:
        self.report_name = report_name
        self.available_reports = available_reports
        available = ", ".join(available_reports)
        message = f"Unknown report: {report_name}. Available reports: {available}"
        super().__init__(message)
