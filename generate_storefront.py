"""
Generate Shopify-compatible HTML and Google Merchant Feed XML for Pixie's Pantry.
"""
import pandas as pd
import os
from dashboard_config import (
    get_picks, get_sales, get_featured, get_bundles, get_carousels,
    build_badge_html, build_bundle_section, build_carousels_section,
    build_google_merchant_feed_xml
)


def generate_html(products_df):
    """Generate HTML for Shopify storefront."""
    picks = get_picks()
    sales = get_sales()
    featured = get_featured()
    
    # Start HTML
    html = ["""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pixie's Pantry | Premium Filtration & Extraction Systems</title>
        <style>
            .product-card {
                position: relative;
                border: 1px solid #333;
                border-radius: 8px;
                padding: 15px;
                margin: 10px;
                background: #1a1a2e;
                color: #fff;
            }
            .badge-pick {
                position: absolute;
                top: 10px;
                left: 10px;
                background: linear-gradient(135deg, #d4af37, #f4d03f);
                color: #111;
                padding: 5px 12px;
                font-size: 0.75em;
                font-weight: 700;
                text-transform: uppercase;
                border-radius: 4px;
                box-shadow: 0 2px 8px rgba(212, 175, 55, 0.4);
            }
            .badge-sale {
                position: absolute;
                top: 10px;
                right: 10px;
                background: #e74c3c;
                color: #fff;
                padding: 5px 12px;
                font-size: 0.75em;
                font-weight: 700;
                text-transform: uppercase;
                border-radius: 4px;
            }
            .badge-featured {
                position: absolute;
                bottom: 10px;
                left: 10px;
                background: #9b59b6;
                color: #fff;
                padding: 5px 12px;
                font-size: 0.75em;
                font-weight: 700;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <h1 style="text-align: center; color: #d4af37;">Pixie's Pantry</h1>
        <p style="text-align: center; color: #888;">Premium filtration and extraction systems for effortless sessions.</p>
    """]
    
    # Add bundles section
    html.append(build_bundle_section())
    
    # Add carousels section
    html.append(build_carousels_section())
    
    # Add products
    html.append('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; padding: 20px;">')
    
    for _, row in products_df.iterrows():
        sku = row['SKU']
        name = row['Product Name']
        price = row['Your Online Price']
        image = row['Image URL']  # Use the Image URL from the CSV
        
        # Ensure the image URL is valid
        if pd.isna(image) or not image.startswith('http'):
            image = 'https://via.placeholder.com/300x300?text=No+Image'
        
        html.append(f'''
        <div class="product-card">
            {build_badge_html(sku)}
            <img src="{image}" alt="{name}" style="width: 100%; border-radius: 4px;">
            <h3 style="margin: 10px 0;">{name}</h3>
            <p style="color: #d4af37; font-weight: bold;">${price}</p>
            <button style="background: #d4af37; color: #111; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;">Add to Cart</button>
        </div>
        ''')
    
    html.append('</div>')
    html.append('</body></html>')
    
    return "\n".join(html)


def main():
    # Load product data
    csv_path = os.path.join(os.path.expanduser("~/Desktop/Pixies_Vape_Shop"), "Dyspensr_Master_Catalog_Priced.csv")
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found. Please ensure the file exists.")
        return
    
    products_df = pd.read_csv(csv_path)
    
    # Generate HTML
    html_output = generate_html(products_df)
    with open(os.path.join(os.path.expanduser("~/Desktop/Pixies_Vape_Shop"), "index.html"), "w") as f:
        f.write(html_output)
    print("✅ Generated index.html")
    
    # Generate Google Merchant Feed
    xml_feed = build_google_merchant_feed_xml(products_df.to_dict('index'))
    with open(os.path.join(os.path.expanduser("~/Desktop/Pixies_Vape_Shop"), "google_merchant_feed.xml"), "w") as f:
        f.write(xml_feed)
    print("✅ Generated google_merchant_feed.xml")


if __name__ == "__main__":
    main()