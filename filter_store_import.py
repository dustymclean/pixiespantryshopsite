#!/usr/bin/env python3
"""
Filter final_store_import.csv to only include rows where Variant SKU exists in 
Dyspensr_Master_Catalog_Priced.csv (variant_sku column).
"""

import csv
import sys


def load_skus_from_master_catalog(file_path):
    """Load variant_sku values from Dyspensr_Master_Catalog_Priced.csv."""
    skus = set()
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sku = row.get('variant_sku', '').strip()
            if sku:
                skus.add(sku)
    return skus


def filter_store_import(input_path, output_path, master_skus):
    """Filter final_store_import.csv to only include rows with SKUs in master_skus."""
    with open(input_path, mode='r', encoding='utf-8') as infile, \
         open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            variant_sku = row.get('Variant SKU', '').strip()
            if variant_sku in master_skus:
                writer.writerow(row)


def main():
    # Paths
    master_catalog_path = '/Users/dusty/Desktop/Dyspensr_Master_Catalog_Priced.csv'
    store_import_path = '/Users/dusty/Desktop/Pixies_Vape_Shop/final_store_import.csv'
    output_path = '/Users/dusty/Desktop/Pixies_Vape_Shop/filtered_store_import.csv'
    
    # Load SKUs from master catalog
    print("Loading SKUs from master catalog...")
    master_skus = load_skus_from_master_catalog(master_catalog_path)
    print(f"Found {len(master_skus)} unique SKUs in master catalog.")
    
    # Filter store import
    print("Filtering store import...")
    filter_store_import(store_import_path, output_path, master_skus)
    print(f"Filtered store import saved to: {output_path}")


if __name__ == "__main__":
    main()