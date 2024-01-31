# CSV Cleaner Tool Guide

This guide provides detailed instructions on how to use the `csvcleaner.py` Python script to clean a CSV file. The script extracts specific columns: Order ID, Order Status, Order Date, Customer Name, # Unique Products in Order, Product ID, Product QTY, Product SKU, and Product Name.
> [!NOTE] 
> This tool is designed for **MacOS and Linux** (Unix-based systems).

## Prerequisites

- Python must be installed on your system.
- You need to have a CSV file to be processed.

## Setup

1. **Python Script**: 
   - Download or copy the `csvcleaner.py` script.
   - Save this script in your home directory (`~/`).

2. **Prepare Your Desktop**:
   - Create a new folder on your Desktop named `raw_csv`.
   - Place the CSV file you want to process in the `raw_csv` folder. Ensure it's the only file in this folder.

3. **Bash Script**:
   - Ensure that the `run_csv_cleaner.sh` bash script is placed on your Desktop.

## Running the Script

1. **Set Permissions** (First Time Only): 
   - Open the Terminal.
   - Run the command: `chmod +x ~/Desktop/run_csv_cleaner.sh` to set execute permissions for the bash script.

2. **Launch the Script**: 
   - Double-click the `run_csv_cleaner.sh` script on your Desktop or run it from the terminal.

## Output

- The cleaned CSV file will be saved on your Desktop with the filename format: `BigCommerce Orders CSV (cleaned) [YYYY-MM-DD].csv`, where `[YYYY-MM-DD]` is the current date.

## Troubleshooting

- If the script does not run when double-clicked, try running it from the terminal with `~/Desktop/run_csv_cleaner.sh`.
- Ensure there are no additional CSV files in the `raw_csv` folder on your Desktop.
- Confirm that the `csvcleaner.py` script is in your home directory and has not been moved or renamed.
