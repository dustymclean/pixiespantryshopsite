#!/usr/bin/env python3
"""
Scrape Toker Poker products from tokerpoker.pixiespantryshop.com
and save to tokerpoker_products.json
"""
import requests
from bs4 import BeautifulSoup
import json
import os

# Configuration
STORE_URL = "https://tokerpoker.pixiespantryshop.com"
OUTPUT_FILE = os.path.expanduser("~/Desktop/Pixies_Vape_Shop/tokerpoker_products.json")


def scrape_toker_poker():
    """Scrape Toker Poker products from the storefront"""
    print(f"Scraping Toker Poker products from {STORE_URL}...")
    
    try:
        # Fetch the storefront HTML
        response = requests.get(STORE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product data
        products = []
        product_cards = soup.select('.product-card')  # Update selector based on actual HTML
        
        for card in product_cards:
            title = card.select_one('.product-title').text.strip() if card.select_one('.product-title') else "No Title"
            sku = card.select_one('.product-sku').text.strip() if card.select_one('.product-sku') else "No SKU"
            price = card.select_one('.product-price').text.strip() if card.select_one('.product-price') else "0.00"
            image_url = card.select_one('.product-image')['src'] if card.select_one('.product-image') else ""
            
            # Clean price (remove $ and commas)
            price = price.replace('$', '').replace(',', '')
            
            products.append({
                "sku": sku,
                "title": title,
                "price": price,
                "image_url": image_url,
                "status": "Active"
            })
        
        # Save to JSON
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2)
        
        print(f"✅ Scraped {len(products)} products. Saved to {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"❌ Error scraping Toker Poker: {e}")


if __name__ == "__main__":
    scrape_toker_poker()