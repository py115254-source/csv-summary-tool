
"""
Command-line CSV summary statistics tool.
"""

import argparse
import sys
from pathlib import Path

import pandas as pd


def calculate_summary(file_path: str) -> pd.DataFrame:
    """Load a CSV file and calculate statistics for numeric columns."""
    csv_path = Path(file_path)

    if not csv_path.is_file():
        raise FileNotFoundError(f"File not found: {csv_path}")

    df = pd.read_csv(csv_path)
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        return pd.DataFrame(
            columns=["mean", "median", "std"]
        )

    return numeric_df.agg(["mean", "median", "std"]).T


def main() -> int:
    """Parse command-line arguments and display CSV statistics."""
    parser = argparse.ArgumentParser(
        description="Print summary statistics for numeric CSV columns."
    )
    parser.add_argument(
        "file",
        help="Path to the input CSV file",
    )
    args = parser.parse_args()

    try:
        summary = calculate_summary(args.file)

        if summary.empty:
            print("No numeric columns found.")
            return 0

        print(f"\nSummary statistics for: {args.file}")
        print(summary.to_string())
        return 0

    except FileNotFoundError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.", file=sys.stderr)
        return 1
    except pd.errors.ParserError:
        print("Error: Invalid CSV format.", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Error reading file: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
