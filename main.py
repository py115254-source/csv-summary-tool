
import argparse
from pathlib import Path

import pandas as pd


def main():
    parser = argparse.ArgumentParser(
        description="Read a CSV file and print summary statistics."
    )
    parser.add_argument("file", help="Path to the CSV file")
    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.is_file():
        print(f"Error: File not found: {file_path}")
        return

    try:
        df = pd.read_csv(file_path)
        numeric_df = df.select_dtypes(include="number")

        if numeric_df.empty:
            print("No numeric columns found.")
            return

        summary = numeric_df.agg(["mean", "median", "std"]).T
        print(f"\nSummary statistics for: {file_path}")
        print(summary.to_string())

    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: Could not parse the CSV file.")
    except OSError as error:
        print(f"Error reading file: {error}")


if __name__ == "__main__":
    main()
