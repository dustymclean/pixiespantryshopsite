"""
Dyspensr Scraper: Automated product data ingestion for Pixie's Pantry.
Scrapes supplier websites, applies pricing psychology, and updates the master catalog.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import re


def scrape_pulsar():
    """Mock data for Pulsar products."""
    products = [
        {
            'SKU': 'WP974',
            'Product Name': 'Pulsar CORE 10” Premium Filtration System',
            'Wholesale Cost': 17.50,
            'Image URL': 'https://cdn.shopify.com/s/files/1/0568/2780/5886/files/pulsar-core-beaker-water-pipe-update.webp',
            'Category': 'Filtration Devices',
            'Brand': 'Pulsar'
        },
        {
            'SKU': 'WP975',
            'Product Name': 'Pulsar CORE 9” Portable Filtration Device',
            'Wholesale Cost': 16.50,
            'Image URL': 'https://cdn.shopify.com/s/files/1/0568/2780/5886/files/pulsar-core-straight-tube-water-pipe-update.webp',
            'Category': 'Filtration Devices',
            'Brand': 'Pulsar'
        },
        {
            'SKU': 'WP976',
            'Product Name': 'Pulsar CORE 6” Precision Extraction System',
            'Wholesale Cost': 15.95,
            'Image URL': 'https://cdn.shopify.com/s/files/1/0568/2780/5886/files/pulsar-core-dab-rig-update.webp',
            'Category': 'Extraction Systems',
            'Brand': 'Pulsar'
        }
    ]
    return pd.DataFrame(products)


def scrape_seshgear():
    """Mock data for SeshGear products."""
    products = [
        {
            'SKU': 'V1218D',
            'Product Name': 'SeshGear Ray Gun Precision Power Supply',
            'Wholesale Cost': 56.75,
            'Image URL': 'https://cdn.shopify.com/s/files/1/0568/2780/5886/files/seshgear-ray-gun-510-vape-battery-lead-updated.webp',
            'Category': 'Power Supplies',
            'Brand': 'SeshGear'
        },
        {
            'SKU': 'WP953',
            'Product Name': 'SeshGear 11.75” Premium Filtration System',
            'Wholesale Cost': 29.99,
            'Image URL': 'https://cdn.shopify.com/s/files/1/0568/2780/5886/files/seshgear-spinner-beaker-bong-1.png',
            'Category': 'Filtration Devices',
            'Brand': 'SeshGear'
        }
    ]
    return pd.DataFrame(products)


def apply_pricing_psychology(df):
    """Apply dynamic pricing and psychology (e.g., $49.99 instead of $50)."""
    def calculate_retail_price(cost):
        if cost < 15:
            return cost * 2.5
        elif cost < 50:
            return cost * 2.0
        else:
            return cost * 1.8
    
    df['Your Online Price'] = df['Wholesale Cost'].apply(calculate_retail_price)
    df['Your Online Price'] = df['Your Online Price'].apply(lambda x: f"${x - 0.01:.2f}")  # Psychology pricing
    return df


def sanitize_for_frontend(df):
    """Sanitize product names/descriptions for front-end display."""
    def sanitize_text(text):
        replacements = {
            r'(?i)\bvape(?:s|rs|ing)?\b': 'filtration system',
            r'(?i)\bbong\b': 'filtration device',
            r'(?i)\bdab rig\b': 'extraction system'
        }
        for old, new in replacements.items():
            text = re.sub(old, new, text)
        return text
    
    df['Product Name'] = df['Product Name'].apply(sanitize_text)
    df['SEO Title'] = df['Product Name'].apply(lambda x: f"{x} | Premium Quality")
    df['Meta Description'] = df.apply(
        lambda row: f"Premium {row['Category']} from {row['Brand']}. Designed for smooth, effortless sessions.",
        axis=1
    )
    df['Search Tags'] = df.apply(
        lambda row: f"{row['Category'].lower()}, {row['Brand'].lower()}, premium, durable, easy to clean",
        axis=1
    )
    return df


def main():
    # Scrape suppliers
    pulsar_df = scrape_pulsar()
    seshgear_df = scrape_seshgear()
    
    # Combine data
    all_products = pd.concat([pulsar_df, seshgear_df], ignore_index=True)
    
    # Apply pricing and sanitization
    all_products = apply_pricing_psychology(all_products)
    all_products = sanitize_for_frontend(all_products)
    
    # Save to CSV
    output_path = os.path.join(os.path.expanduser("~/Desktop/Pixies_Vape_Shop"), "Dyspensr_Master_Catalog_Priced.csv")
    all_products.to_csv(output_path, index=False)
    print(f"✅ Updated {output_path} with {len(all_products)} products")


if __name__ == "__main__":
    main()