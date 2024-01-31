# CSV Cleaning Tool Guide

This guide provides instructions on how to use a Python script to clean a CSV file, extracting only the necessary columns: Product ID, QTY, SKU, and Product Name.

## Prerequisites

- Python installed on your system.
- A CSV file to be processed.

## Setup

1. **Place the CSV File**: 
   Ensure the CSV file you want to process is the only file in a dedicated folder on your Desktop. The folder can have any name.

2. **Script and Bash File**: 
   The Python script and a bash file (`run_script.sh`) should be placed on your Desktop.

## Running the Script

1. **Open Terminal**: 
   Open a terminal window.

2. **Navigate to Desktop**: 
   Use the command `cd ~/Desktop` to navigate to your Desktop.

3. **Run the Bash Script**: 
   Execute the bash script by typing `./csvcleaner.sh`. This script will automatically find the CSV file in the specified folder, process it, and save the cleaned file on the Desktop.

## Output

- The cleaned CSV file will be saved on the Desktop with the filename format: `BigCommerce Orders CSV (cleaned) [YYYY-MM-DD].csv`, where `[YYYY-MM-DD]` is the current date.

## Troubleshooting

- Ensure Python is correctly installed by running `python --version` in the terminal.
- Make sure the bash script has execute permissions. You can set this with `chmod +x run_script.sh` on the terminal.
- If there are any errors during the script execution, they will be displayed in the terminal.
