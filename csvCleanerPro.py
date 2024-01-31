import csv
import re
import os
from datetime import datetime

# Function to extract and split details from the Product Details column for multiple products
def extract_and_split_product_details(details):
    # Split the details by the pipe '|' character and then extract individual product details
    split_details = details.split('|')
    products = []
    for detail in split_details:
        product_id = re.search(r'Product ID: (\d+)', detail)
        qty = re.search(r'Product Qty: (\d+)', detail)
        sku = re.search(r'SKU: ([\w-]+)', detail)
        name = re.search(r'Product Name: ([^,]+)', detail)

        products.append((
            product_id.group(1) if product_id else '',
            qty.group(1) if qty else '',
            sku.group(1) if sku else '',
            name.group(1) if name else ''
        ))
    return products

def clean_csv(input_folder_path, output_folder_path):
    csv_files = [f for f in os.listdir(input_folder_path) if f.endswith('.csv')]
    if not csv_files:
        raise FileNotFoundError("No CSV file found in the specified directory.")
    input_file_path = os.path.join(input_folder_path, csv_files[0])

    with open(input_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        # Find the index of the columns we need
        details_index = header.index('Product Details')
        columns_to_keep_indices = [header.index(col) for col in ['Order ID', 'Order Status', 'Order Date', 'Customer Name', '# Unique Products in Order']]

        # Create the output file
        today_date = datetime.now().strftime('%Y-%m-%d')
        output_file_name = f'BigCommerce Orders CSV (cleaned) {today_date}.csv'
        output_file_path = os.path.join(output_folder_path, output_file_name)

        with open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            new_header = [header[i] for i in columns_to_keep_indices] + ['Product ID', 'Product QTY', 'Product SKU', 'Product Name']
            writer.writerow(new_header)

            # Process each row
            for row in reader:
                details = row[details_index]
                products = extract_and_split_product_details(details)

                for product in products:
                    new_row = [row[i] for i in columns_to_keep_indices] + list(product)
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
