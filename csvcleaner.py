import csv
import re
import os
from datetime import datetime

# Function to extract details from the Product Details column
def extract_product_details(details):
    product_ids = re.findall(r'Product ID: (\d+)', details)
    qtys = re.findall(r'Product Qty: (\d+)', details)
    skus = re.findall(r'SKU: ([\w-]+)', details)
    names = re.findall(r'Product Name: ([^,]+)', details)

    product_ids = product_ids[0].split('|') if product_ids else ['']
    qtys = qtys[0].split('|') if qtys else ['']
    skus = skus[0].split('|') if skus else ['']
    names = [name.split('|')[0] for name in names] if names else ['']

    return product_ids[0], qtys[0], skus[0], names[0]

def clean_csv(input_folder_path, output_folder_path):
    csv_files = [f for f in os.listdir(input_folder_path) if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError("No CSV file found in the specified directory.")
    input_file_path = os.path.join(input_folder_path, csv_files[0])

    with open(input_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        # Find the index of the columns we need
        try:
            details_index = header.index('Product Details')
            columns_to_keep_indices = [header.index(col) for col in ['Order ID', 'Order Status', 'Order Date', 'Customer Name', '# Unique Products in Order']]
        except ValueError as e:
            raise ValueError(f"Column not found in CSV: {e}")

        # Create the output file
        today_date = datetime.now().strftime('%Y-%m-%d')
        output_file_name = f'BigCommerce Orders CSV (cleaned) {today_date}.csv'
        output_file_path = os.path.join(output_folder_path, output_file_name)

        with open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            # Write the header
            new_header = [header[i] for i in columns_to_keep_indices] + ['Product ID', 'Product QTY', 'Product SKU', 'Product Name']
            writer.writerow(new_header)

            # Process each row
            for row in reader:
                details = row[details_index]
                product_id, qty, sku, name = extract_product_details(details)
                new_row = [row[i] for i in columns_to_keep_indices] + [product_id, qty, sku, name]
                writer.writerow(new_row)

    return output_file_name

if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop")
    input_folder_name = "raw_csv"
    input_folder_path = os.path.join(desktop_path, input_folder_name)

    try:
        cleaned_csv_name = clean_csv(input_folder_path, desktop_path)
        print(f"Cleaned CSV saved as: {cleaned_csv_name} on the Desktop")
    except Exception as e:
        print(str(e))
