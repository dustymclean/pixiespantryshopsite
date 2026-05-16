#!/usr/bin/env python3
"""
Categorize products into clinical clusters (100 at a time).
"""
import csv
import json

# Clinical clusters mapping (Category/Subcategory → Cluster)
CLUSTER_MAPPING = {
    # Cluster A: Active Electronic TEDs
    "Vaporizers": "Cluster A: Active Electronic TEDs",
    "Portable Vaporizers": "Cluster A: Active Electronic TEDs",
    "Desktop Vaporizers": "Cluster A: Active Electronic TEDs",
    "Vape Pens": "Cluster A: Active Electronic TEDs",
    "E-Cigarettes": "Cluster A: Active Electronic TEDs",
    
    # Cluster B: Passive/Manual TEDs
    "Dab Rigs": "Cluster B: Passive/Manual TEDs",
    "Oil Rigs": "Cluster B: Passive/Manual TEDs",
    "Nectar Collectors": "Cluster B: Passive/Manual TEDs",
    "Torches": "Cluster B: Passive/Manual TEDs",
    
    # Cluster C: Hydrated Filters
    "Bongs": "Cluster C: Hydrated Filters",
    "Bubblers": "Cluster C: Hydrated Filters",
    "Water Pipes": "Cluster C: Hydrated Filters",
    
    # Cluster D: Botanical Homogenizers
    "Grinders": "Cluster D: Botanical Homogenizers",
    "Shredders": "Cluster D: Botanical Homogenizers",
    "Rolling Trays": "Cluster D: Botanical Homogenizers",
    
    # Cluster E: Atmospheric Preservation Units
    "Jars": "Cluster E: Atmospheric Preservation Units",
    "Stash Boxes": "Cluster E: Atmospheric Preservation Units",
    "Storage": "Cluster E: Atmospheric Preservation Units",
    
    # Cluster F: Mass Verification Instruments (Reusable, precision dosing/ignition)
    "Scales": "Cluster F: Mass Verification Instruments",
    "Lighters": "Cluster F: Mass Verification Instruments",
    "Toker Poker": "Cluster F: Mass Verification Instruments",
    
    # Cluster G: Chemical Sterilization Agents
    "Cleaners": "Cluster G: Chemical Sterilization Agents",
    "ISO Alcohol": "Cluster G: Chemical Sterilization Agents",
    
    # Cluster H: Induction Heaters
    "Induction Heaters": "Cluster H: Induction Heaters",
    
    # Cluster I: Pressure Regulation Hardware
    "Carb Caps": "Cluster I: Pressure Regulation Hardware",
    "Bangers": "Cluster I: Pressure Regulation Hardware",
    
    # Cluster J: Clinical Extract Applicators
    "Cartridges": "Cluster J: Clinical Extract Applicators",
    "Carts": "Cluster J: Clinical Extract Applicators",
    "Dab Tools": "Cluster J: Clinical Extract Applicators",
}

# Default cluster if no match
DEFAULT_CLUSTER = "Cluster E: Atmospheric Preservation Units"

def assign_cluster(category, subcategory):
    """Assign a clinical cluster based on category/subcategory."""
    if subcategory in CLUSTER_MAPPING:
        return CLUSTER_MAPPING[subcategory]
    elif category in CLUSTER_MAPPING:
        return CLUSTER_MAPPING[category]
    else:
        return DEFAULT_CLUSTER

def categorize_products(offset=0, limit=100):
    """Categorize products in batches of 100."""
    input_csv = "~/Desktop/Medical_Pivot_Master_Catalog.csv"
    output_csv = "~/Desktop/Medical_Pivot_Master_Catalog_Categorized.csv"
    
    # Load products
    with open(input_csv.replace("~", "/Users/dusty"), 'r', encoding='utf-8') as f:
        products = list(csv.DictReader(f))
    
    # Categorize batch
    updated = 0
    for product in products[offset:offset+limit]:
        cluster = assign_cluster(product.get('Category', ''), product.get('Subcategory', ''))
        if product.get('Clinical Cluster') != cluster:
            product['Clinical Cluster'] = cluster
            updated += 1
    
    # Save updates
    with open(output_csv.replace("~", "/Users/dusty"), 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)
    
    print(f"✅ Categorized {updated} products (offset {offset}).")
    print(f"Next batch: python3 categorize_products.py --offset {offset + limit}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=100)
    args = parser.parse_args()
    
    categorize_products(offset=args.offset, limit=args.limit)