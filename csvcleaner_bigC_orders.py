import pandas as pd
import re
from datetime import datetime

# Function to extract details from the Product Details column
def extract_product_details(details):
    # Find all instances of the patterns in the details string
    product_ids = re.findall(r'Product ID: (\d+)', details)
    qtys = re.findall(r'Product Qty: (\d+)', details)
    skus = re.findall(r'SKU: ([\w-]+)', details)
    names = re.findall(r'Product Name: ([^,]+)', details)
    
    # Handle multiple entries separated by "|"
    product_ids = product_ids[0].split('|') if product_ids else ['']
    qtys = qtys[0].split('|') if qtys else ['']
    skus = skus[0].split('|') if skus else ['']
    names = [name.split('|')[0] for name in names] if names else ['']
    
    # Return the first found entry for each detail (or empty string if not found)
    return product_ids[0], qtys[0], skus[0], names[0]

def clean_csv(input_file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file_path)

    # Define the columns to keep based on the screenshot provided
    # Since 'Order Aging' was not found, it has been excluded
    columns_to_keep = ['Order ID', 'Order Status', 'Order Date', 'Customer Name', '# Unique Products in Order']
    
    # Check if the column '# Unique Products in Order' exists in the dataframe, if not, use 'Total Quantity'
    if '# Unique Products in Order' not in df.columns:
        columns_to_keep[-1] = 'Total Quantity'  # Assuming this is the intended column
    
    # Apply the function to each row in the Product Details column for the new columns
    details = df['Product Details'].map(extract_product_details)
    df['Product ID'], df['Product QTY'], df['Product SKU'], df['Product Name'] = zip(*details)

    # Create a new DataFrame with only the specified columns
    df_cleaned = df[columns_to_keep + ['Product ID', 'Product QTY', 'Product SKU', 'Product Name']]

    # Save the cleaned DataFrame to a new CSV file
    today_date = datetime.now().strftime('%Y-%m-%d')
    output_file_path = f'BigCommerce Orders CSV (cleaned) {today_date}.csv'
    df_cleaned.to_csv(output_file_path, index=False)
    
    return output_file_path

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python clean_csv_script.py <path_to_csv_file>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    cleaned_csv = clean_csv(input_csv)
    print(f"Cleaned CSV saved as: {cleaned_csv}")
