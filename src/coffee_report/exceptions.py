from pathlib import Path


class CoffeeReportError(Exception):
    """Base exception for the application."""


class InputFileNotFoundError(CoffeeReportError):
    """Raised when a requested CSV file does not exist."""

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        message = f"Input CSV file does not exist: {file_path}"
        super().__init__(message)
