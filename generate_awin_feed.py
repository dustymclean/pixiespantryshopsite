#!/usr/bin/env python3
"""
Generate Awin product feed from Dyspensr_Master_Catalog_Priced.csv.
Output: awin_feed.csv (Awin-compatible format).
"""

import csv
import os
from datetime import datetime

# Paths
INPUT_CSV = "/Users/dusty/Desktop/Dyspensr_Master_Catalog_Priced.csv"
OUTPUT_CSV = "/Users/dusty/Desktop/Pixies_Vape_Shop/awin_feed.csv"
UPDATED_CSV = "/Users/dusty/Desktop/Dyspensr_Master_Catalog_Priced_with_awin.csv"

# Awin feed headers
awin_headers = [
    "id", "title", "description", "link", "image_link", 
    "price", "brand", "category", "availability"
]

def map_awin_links():
    """Map Awin links to products and save updated CSV."""
    awin_mapping = {
        "Dr. Dabber": "https://drdabber.sjv.io/c/5929369/1892868/22644",
        "Daily High Club": "https://daily-high-club-affiliate-program.pxf.io/c/5929369/673119/10481",
        "Smoke Cartel": "https://smokecartel.pxf.io/c/5929369/2120665/26924",
        "Nalgene": "https://nalgene.pxf.io/c/5929369/970979/12848",
        "Brondell": "https://brondell.pxf.io/c/5929369/887206/12276",
        "Anker": "https://ankersolix.pxf.io/c/5929369/2241990/29130"
    }
    
    # Read input CSV and add awin_link column
    updated_rows = []
    with open(INPUT_CSV, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['awin_link']
        for row in reader:
            brand = row.get('brand', '')
            description = row.get('description', '').lower()
            
            # Map Awin link based on brand, description, or category
            awin_link = ""
            for brand_key, link in awin_mapping.items():
                # Check brand, description, or category
                if (
                    brand_key.lower() in brand.lower()
                    or brand_key.lower() in description.lower()
                    or brand_key.lower() in row.get('category', '').lower()
                    or brand_key.lower() in row.get('product_type', '').lower()
                ):
                    awin_link = link
                    break
            
            # Manual overrides for specific SKUs (force-assign Awin links)
            manual_mapping = {
                "MEDUSA-10-25-STRAIGHT-RECYCLER": "https://smokecartel.pxf.io/c/5929369/2120665/26924",  # Smoke Cartel
                "MEDUSA-11-5-SWISS-INCYCLER": "https://daily-high-club-affiliate-program.pxf.io/c/5929369/673119/10481",  # Daily High Club
                "MEDUSA-12-TUBE": "https://nalgene.pxf.io/c/5929369/970979/12848",  # Nalgene
                # Force-assign Awin links to the first 3 products for testing
                "MEDUSA-10-25-STRAIGHT-RECYCLER": "https://smokecartel.pxf.io/c/5929369/2120665/26924",
                "MEDUSA-11-5-SWISS-INCYCLER": "https://daily-high-club-affiliate-program.pxf.io/c/5929369/673119/10481",
                "MEDUSA-12-TUBE": "https://nalgene.pxf.io/c/5929369/970979/12848"
            }
            if row.get('variant_sku') in manual_mapping:
                awin_link = manual_mapping[row['variant_sku']]
            
            row['awin_link'] = awin_link
            updated_rows.append(row)
    
    # Write updated CSV
    with open(UPDATED_CSV, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)
    
    print(f"✅ Updated CSV with Awin links: {UPDATED_CSV}")

def generate_awin_feed():
    """Generate Awin feed from updated CSV."""
    products = []
    
    # Read updated CSV
    with open(UPDATED_CSV, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            # Skip if no Awin link
            if not row.get('awin_link'):
                continue
            
            # Map fields to Awin format
            product = {
                "id": row.get('variant_sku', row.get('product_id', '')),
                "title": row.get('parent_product_name', '').strip('"'),
                "description": row.get('description', '').replace("\n", " ").replace("\r", ""),
                "link": row.get('awin_link', ''),
                "image_link": row.get('primary_image_url', ''),
                "price": row.get('store_price', '0.00'),
                "brand": row.get('brand', 'Pixie’s Pantry'),
                "category": row.get('category', 'Hardware'),
                "availability": "in stock"
            }
            products.append(product)
    
    # Write output CSV
    with open(OUTPUT_CSV, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=awin_headers)
        writer.writeheader()
        writer.writerows(products)
    
    print(f"✅ Awin feed generated: {OUTPUT_CSV} ({len(products)} products)")

if __name__ == "__main__":
    map_awin_links()
    generate_awin_feed()