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

### Examples

1. Chunking a file named "customer_data.csv" in the current directory:

   ```bash
   python chunk.py customer_data.csv
   ```

2. Chunking a file in a subdirectory:

   ```bash
   python chunk.py data/sales_2023.csv
   ```

3. Chunking a file with an absolute path:

   ```bash
   python chunk.py /home/user/documents/large_dataset.csv
   ```

## Output

The script creates a new directory for the chunked files. The directory name is based on the input file's name, with "_chunks" appended.

### Example Outputs

1. For input file "customer_data.csv":
   - Output directory: `customer_data_chunks/`
   - Chunk files:
     - `customer_data_chunk_0.csv`
     - `customer_data_chunk_1.csv`
     - `customer_data_chunk_2.csv`
     - ... (number of files depends on the size of the input)

2. For input file "data/sales_2023.csv":
   - Output directory: `sales_2023_chunks/`
   - Chunk files:
     - `sales_2023_chunk_0.csv`
     - `sales_2023_chunk_1.csv`
     - ... (number of files depends on the size of the input)

Each chunk file will contain the header row from the original CSV file, followed by a portion of the data rows. The last chunk may be smaller than the others.

After processing, the script will display:
- The total number of rows in the original file
- The number of chunks created
- Confirmation that all rows were successfully chunked

If any errors occur during processing, an error message will be displayed instead.