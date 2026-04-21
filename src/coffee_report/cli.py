import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    """Create the base CLI parser for future report commands."""
    return argparse.ArgumentParser(
        prog="coffee-report",
        description="Build coffee consumption reports from CSV files.",
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Parse CLI arguments and exit successfully.

    The reporting workflow will be added in the next implementation stages.
    """
    parser = build_parser()
    parser.parse_args(argv)
    return 0
