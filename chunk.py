# Write a function to chunk a CSV file into smaller files of less than 4 MB in size
import csv
import os
import sys

# Define the default chunk size (4 MB)
DEFAULT_CHUNK_SIZE = 4 * 1024 * 1024  # 4 MB in bytes

def validate_input(input_file):
    # Check if the file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file '{input_file}' does not exist.")
    
    # Check if the file is not empty
    if os.path.getsize(input_file) == 0:
        raise ValueError(f"The file '{input_file}' is empty.")
    
    # Check if the file has a .csv extension
    if not input_file.lower().endswith('.csv'):
        raise ValueError(f"The file '{input_file}' is not a CSV file.")
    
    # Check if the file is a valid CSV
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Try to read the first row
    except csv.Error:
        raise ValueError(f"The file '{input_file}' is not a valid CSV file.")

def chunk_csv(file_path, output_dir, chunk_size=DEFAULT_CHUNK_SIZE):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get the base name of the input file without the extension
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header row
        
        file_count = 0
        current_chunk_size = 0
        current_chunk = []
        
        for row in reader:
            # Calculate the size of the current row
            row_size = sum(len(str(cell)) for cell in row) + len(row) - 1  # Account for commas
            
            # Check if adding this row would exceed the chunk size
            if current_chunk_size + row_size > chunk_size:
                # Write the current chunk to a new file
                output_file_path = os.path.join(output_dir, f'{base_name}_chunk_{file_count}.csv')
                with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
                    writer = csv.writer(output_file)
                    writer.writerow(header)  # Write the header
                    writer.writerows(current_chunk)
                
                # Reset for the next chunk
                file_count += 1
                current_chunk = []
                current_chunk_size = 0
            
            # Add the row to the current chunk
            current_chunk.append(row)
            current_chunk_size += row_size
        
        # Write any remaining rows to a final chunk
        if current_chunk:
            output_file_path = os.path.join(output_dir,  f'{base_name}_chunk_{file_count}.csv')
            with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(header)
                writer.writerows(current_chunk)

def validate_chunks(file_path, output_dir):
    # Count the total number of rows in the original file (excluding the header)
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        original_row_count = sum(1 for _ in reader)

    # Count the total number of rows in all chunked files
    total_chunked_rows = 0
    for chunk_file in os.listdir(output_dir):
        if chunk_file.endswith('.csv'):
            chunk_file_path = os.path.join(output_dir, chunk_file)
            with open(chunk_file_path, 'r', newline='', encoding='utf-8') as chunkfile:
                reader = csv.reader(chunkfile)
                next(reader)  # Skip the header
                chunk_row_count = sum(1 for _ in reader)
                total_chunked_rows += chunk_row_count
                print(f'{chunk_file}: {chunk_row_count} rows')

    # Validate the row counts
    print(f'Total rows in original file: {original_row_count}')
    print(f'Total rows in chunked files: {total_chunked_rows}')
    if original_row_count == total_chunked_rows:
        print('Validation successful: Row counts match.')
    else:
        print('Validation failed: Row counts do not match.')

# Example usage
if len(sys.argv) < 2:
    print("Usage: python chunk.py <input_file_path>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    validate_input(input_file)
    
    # Get the base name of the input file without the extension
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    # Set output directory name as basename_chunks
    output_dir = f'{base_name}_chunks'

    chunk_csv(input_file, output_dir)
    validate_chunks(input_file, output_dir)
except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)