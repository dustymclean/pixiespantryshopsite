import csv

# Load Toker Poker products
products = []
with open('toker_poker_catalog.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row.get('Available', '').lower() != 'true':
            continue
        sku = row.get('Piece SKU', '').strip()
        if not sku:
            continue
        
        products.append({
            'sku': sku,
            'title': row.get('Product Title', 'Toker Poker'),
            'brand': 'Toker Poker',
            'collection': row.get('Collection', ''),
            'price': row.get('MSRP (Retail) Clean', '10.99'),
            'image_url': row.get('Primary Image URL', ''),
            'available': True
        })

# Generate HTML for Toker Poker products
html_cards = []
for product in products:
    if not product['available']:
        continue
    
    html_cards.append(f'''
<div class="card" onclick="openModal('{product['sku']}')" data-search="{product['title'].lower()} {product['collection'].lower()} {product['brand'].lower()}" data-name="{product['title']}" data-brand="{product['brand']}" data-cat="{product['collection']}" data-price="{product['price']}">
    <img src="{product['image_url']}" alt="{product['title']}" class="card-img" loading="lazy">
    <div class="card-body">
        <div class="card-brand">{product['brand']}</div>
        <div class="card-title">{product['title']}</div>
        <div class="card-price">${product['price']}</div>
    </div>
</div>
''')

# Save the HTML to a file
with open('toker_poker_cards.html', 'w', encoding='utf-8') as f:
    f.write(''.join(html_cards))