#!/usr/bin/env python3
"""
Generate shop.html with products from Dyspensr_Master_Catalog_Priced.csv
"""
import pandas as pd

# Load the catalog
df = pd.read_csv('Dyspensr_Master_Catalog_Priced.csv')

# Generate product cards
product_cards = []
for _, row in df.iterrows():
    try:
        price = float(str(row['Your Online Price']).replace('$', ''))
        msrp = float(str(row['MSRP']).replace('$', '')) if pd.notna(row['MSRP']) else price
    except:
        price = 0.0
        msrp = 0.0
    
    description = str(row['Meta Description'])[:120] if pd.notna(row['Meta Description']) else ''
    
    product_cards.append(f'''
    <div class="card">
        <img src="{row['Image URL']}" alt="{row['Clean Product Name']}" style="width: 100%; border-radius: 12px;">
        <h3>{row['Clean Product Name']}</h3>
        <p>{description}...</p>
        <div class="price">${price:.2f}<span class="strike">${msrp:.2f}</span></div>
        <button class="btn" data-add='{"sku":"{row['SKU']}","name":"{row['Clean Product Name']}","price":{price * 100}}'>Add to Cart</button>
    </div>
    ''')

# Read the template
with open('shop_template.html', 'r') as f:
    html = f.read()

# Inject products
html = html.replace('{{PRODUCT_CARDS}}', '\n'.join(product_cards))

# Save the file
with open('shop.html', 'w') as f:
    f.write(html)

print("✓ Generated shop.html with {} products".format(len(product_cards)))