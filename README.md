# CSV Cleaner Tool Guide

This guide provides instructions on how to use the `csvcleaner.py` Python script to clean a CSV file, extracting only the necessary columns: Order ID, Order Status, Order Date, Customer Name, # Unique Products in Order, Product ID, Product QTY, Product SKU, and Product Name.

## Prerequisites

- Python must be installed on your system.
- The `csvcleaner.py` script must be saved in your home directory.

## Setup

1. **Python Script**: 
   Make sure the `csvcleaner.py` script is stored in your home directory (`~/`).

2. **Bash Script**: 
   A bash script named `run_csv_cleaner.sh` should be placed on your Desktop.

## Prepare Your CSV File

- The CSV file you want to process must be the only file located in a folder named `raw_csv` on your Desktop.

## Running the Script

1. **Set Permissions**: 
   Before running the script for the first time, set the execute permissions by running `chmod +x ~/Desktop/run_csv_cleaner.sh` in the terminal.

2. **Launch the Script**: 
   Double-click the `run_csv_cleaner.sh` script on your Desktop or run it from the terminal.

## Output

- The cleaned CSV file will be saved on your Desktop with the filename format: `BigCommerce Orders CSV (cleaned) [YYYY-MM-DD].csv`, where `[YYYY-MM-DD]` is the current date.

## Troubleshooting

- If the script does not run when double-clicked, try running it from the terminal with `~/Desktop/run_csv_cleaner.sh`.
- Make sure there are no additional CSV files in the `raw_csv` folder on your Desktop.
- Ensure that the `csvcleaner.py` script is present in your home directory and not moved or renamed.
