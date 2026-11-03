
# CSV Summary Tool

A command-line Python tool that reads a CSV dataset and prints summary statistics for numeric columns.

## Features
- Reads CSV files using a command-line argument
- Calculates mean, median, and standard deviation
- Displays results in a formatted table
- Handles missing files and invalid CSV input

## Requirements
- Python 3
- pandas

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py sample.csv
```

Replace `sample.csv` with the path to your own CSV file.

## Example Output
The tool prints mean, median, and standard deviation for each numeric column.

## Error Handling
If the input file does not exist, the tool displays a clear error message.

## Disclaimer
This project is created for educational purposes.
