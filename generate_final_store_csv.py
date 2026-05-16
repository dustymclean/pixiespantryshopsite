#!/usr/bin/env python3
"""
Generate the final store CSV for Pixie's Pantry by merging:
1. Base Shopify CSV (4.7.26_filled_shopify_import.csv)
2. Medusa medical items (medusa_medical_items.csv)
3. Pricing overrides (special_variable_pricing_audit.csv)
4. Tiered pricing logic (good_better_best_pricing_matrix.csv)

Output: ~/Desktop/Pixies_Vape_Shop/final_store_import.csv
"""

import csv
import re
from pathlib import Path
from typing import Dict, List, Optional

# Paths
DOWNLOADS = Path("~/Downloads").expanduser()
DESKTOP = Path("~/Desktop/Pixies_Vape_Shop").expanduser()
DESKTOP.mkdir(exist_ok=True)

BASE_CSV = DOWNLOADS / "4.7.26_filled_shopify_import.csv"
MEDUSA_CSV = DOWNLOADS / "medusa_medical_items.csv"
PRICING_AUDIT_CSV = DOWNLOADS / "special_variable_pricing_audit.csv"
TIER_MATRIX_CSV = DOWNLOADS / "good_better_best_pricing_matrix.csv"
OUTPUT_CSV = DESKTOP / "final_store_import.csv"

# Tier multipliers (cost → retail)
TIER_MULTIPLIERS = {
    "GOOD": 1.8,
    "BETTER": 2.2,
    "BEST": 3.0,
    "BETTER+": 2.5,
    "GOOD+": 2.0,
}


def clean_price(price_str: str) -> float:
    """Convert "$12.34" → 12.34"""
    if not price_str:
        return 0.0
    return float(re.sub(r"[^0-9.]", "", price_str))


def generate_sku_from_slug(slug: str) -> str:
    """Convert slug to Pixie's SKU format (e.g., "10-25-straight-recycler" → "HUMAN-GRADE-10-25-RECYCLER")"""
    # Remove quotes and special chars
    slug = slug.replace('"', "").replace("'", "")
    # Capitalize and replace separators
    words = re.split(r"[-_ ]", slug)
    words = [word.upper() for word in words if word]
    return "-".join(words)


def load_base_csv() -> Dict[str, Dict]:
    """Load base Shopify CSV (key: Handle)"""
    base_data = {}
    with open(BASE_CSV, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            base_data[row["Handle"]] = row
    return base_data


def load_medusa_csv() -> List[Dict]:
    """Load Medusa CSV and generate SKUs"""
    medusa_items = []
    with open(MEDUSA_CSV, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row["slug"]:
                continue
            # Generate SKU from slug
            sku = generate_sku_from_slug(row["slug"])
            # Clean cost
            cost = clean_price(row["primary_price_guess"])
            # Determine tier multiplier
            tier = row["good_better_best"] or "BETTER"
            multiplier = TIER_MULTIPLIERS.get(tier, 2.2)
            retail = round(cost * multiplier, 2)
            
            medusa_items.append({
                "Handle": row["slug"],
                "Title": row["taxonomy_product_name"] or row["title"],
                "Body (HTML)": row["taxonomy_description"] or "",
                "Vendor": row["brand_guess"] or "Medusa",
                "Product Category": "Hardware",
                "Variant SKU": sku,
                "Variant Price": retail,
                "Cost Per Item": cost,
                "Variant Compare At Price": round(retail * 1.2, 2),  # 20% MSRP proxy
                "Tags": f"Medusa, {row['clinical_tier']}, {row['hardware_class']}, {tier}",
                "_Pricing Tier": tier,
                "_Gross Margin $": round(retail - cost, 2),
                "_Gross Margin %": round((retail - cost) / retail * 100, 1) if retail > 0 else 0.0,
                "_Pricing Method": "Medusa Tiered Markup",
            })
    return medusa_items


def load_pricing_overrides() -> Dict[str, Dict]:
    """Load pricing overrides (key: Variant SKU)"""
    overrides = {}
    with open(PRICING_AUDIT_CSV, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            overrides[row["SKU"]] = {
                "_Pixies Recommended Retail": clean_price(row["Retail"]),
                "_Market MSRP / Proxy": clean_price(row["MSRP/Proxy"]),
                "_Pricing Tier": row["Tier"],
                "_Pricing Method": row["Pricing Method"],
            }
    return overrides


def merge_data(base_data: Dict[str, Dict], medusa_items: List[Dict], overrides: Dict[str, Dict]) -> List[Dict]:
    """Merge all data sources"""
    final_data = []
    
    # Add base items
    for handle, row in base_data.items():
        final_data.append(row)
    
    # Add Medusa items
    for item in medusa_items:
        # Apply pricing overrides if SKU matches
        sku = item["Variant SKU"]
        if sku in overrides:
            item.update(overrides[sku])
        final_data.append(item)
    
    return final_data


def write_final_csv(data: List[Dict]):
    """Write final CSV with all columns from base CSV + custom columns"""
    # Load all columns from base CSV
    with open(BASE_CSV, mode="r", encoding="utf-8-sig") as f:
        base_reader = csv.DictReader(f)
        shopify_columns = base_reader.fieldnames
    
    # Pixie's custom columns (ensure they don't overlap with Shopify columns)
    custom_columns = [
        "_Pricing Brand", "_Pricing Product Title", "_Pixies Recommended Retail", 
        "_Market MSRP / Proxy", "_Pricing Tier", "_Gross Margin $", 
        "_Gross Margin %", "_Pricing Method", "_Price Confidence",
    ]
    
    # Combine columns (Shopify first, then custom)
    all_columns = list(shopify_columns) + [col for col in custom_columns if col not in shopify_columns]
    
    # Ensure all rows have all columns (fill missing with empty string)
    normalized_data = []
    for row in data:
        normalized_row = {col: row.get(col, "") for col in all_columns}
        normalized_data.append(normalized_row)
    
    # Write CSV
    with open(OUTPUT_CSV, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=all_columns)
        writer.writeheader()
        writer.writerows(normalized_data)


if __name__ == "__main__":
    print("Loading base CSV...")
    base_data = load_base_csv()
    
    print("Loading Medusa items...")
    medusa_items = load_medusa_csv()
    
    print("Loading pricing overrides...")
    overrides = load_pricing_overrides()
    
    print("Merging data...")
    final_data = merge_data(base_data, medusa_items, overrides)
    
    print(f"Writing final CSV to {OUTPUT_CSV}...")
    write_final_csv(final_data)
    
    print("✅ Done!")