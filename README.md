# CSV File Chunker

This Python script chunks a large CSV file into smaller files, each less than 4 MB in size. It's useful for processing or uploading large CSV files in smaller, more manageable pieces.

## Features

- Splits a large CSV file into smaller chunks
- Preserves the header row in each chunk
- Validates input file (existence, non-empty, CSV format)
- Validates output (ensures all rows are preserved)
- Handles Unicode (UTF-8) encoding

## Requirements

- Python 3.6+
- No external libraries required (uses only Python standard library)

## Usage

Run the script from the command line, providing the path to the CSV file you want to chunk:
