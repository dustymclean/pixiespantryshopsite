# Stripe Configuration
STRIPE_PUBLIC_KEY = "pk_live_51TKWUQPgf6ETeSSJEyWJrTMuNJWuoVaAfgdhWoZfwrYxq7fa8sC4fI1Tx1xdthrZ1jZmrSVP4rOjFSI3ztFmV2iQ00zwHXHeoB"
import os

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")

def get_picks():
    """Return a list of SKUs for "picks" (featured products)."""
    return []  # Placeholder: No picks by default


def get_sales():
    """Return a list of SKUs for products on sale."""
    return []  # Placeholder: No sales by default


def get_featured():
    """Return a list of SKUs for featured products."""
    return []  # Placeholder: No featured products by default


def get_bundles():
    """Return a list of bundles for the storefront."""
    return []  # Placeholder: No bundles by default


def get_carousels():
    """Return a list of carousels for the storefront."""
    return []  # Placeholder: No carousels by default


def build_badge_html(sku):
    """Build HTML for badges (picks, sales, featured) based on SKU."""
    badges = []
    if sku in get_picks():
        badges.append('<div class="badge-pick">PICK</div>')
    if sku in get_sales():
        badges.append('<div class="badge-sale">SALE</div>')
    if sku in get_featured():
        badges.append('<div class="badge-featured">FEATURED</div>')
    return "".join(badges)


def build_bundle_section():
    """Build HTML for the bundles section."""
    bundles = get_bundles()
    if not bundles:
        return ""
    html = ['<div style="padding: 20px;"><h2 style="color: #d4af37;">Bundles</h2>']
    html.append('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px;">')
    for bundle in bundles:
        html.append(f'''
        <div class="product-card">
            <img src="{bundle.get('image', 'https://via.placeholder.com/300x300?text=Bundle')}" alt="{bundle.get('name', 'Bundle')}" style="width: 100%; border-radius: 4px;">
            <h3 style="margin: 10px 0;">{bundle.get('name', 'Bundle')}</h3>
            <p style="color: #d4af37; font-weight: bold;">${bundle.get('price', '0.00')}</p>
            <button style="background: #d4af37; color: #111; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;">Add to Cart</button>
        </div>
        ''')
    html.append('</div></div>')
    return "".join(html)


def build_carousels_section():
    """Build HTML for the carousels section."""
    carousels = get_carousels()
    if not carousels:
        return ""
    html = ['<div style="padding: 20px;"><h2 style="color: #d4af37;">Carousels</h2>']
    for carousel in carousels:
        html.append(f'<h3 style="color: #d4af37;">{carousel.get("title", "Carousel")}</h3>')
        html.append('<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px;">')
        for item in carousel.get("items", []):
            html.append(f'''
            <div class="product-card">
                <img src="{item.get('image', 'https://via.placeholder.com/300x300?text=Item')}" alt="{item.get('name', 'Item')}" style="width: 100%; border-radius: 4px;">
                <h3 style="margin: 10px 0;">{item.get('name', 'Item')}</h3>
                <p style="color: #d4af37; font-weight: bold;">${item.get('price', '0.00')}</p>
                <button style="background: #d4af37; color: #111; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;">Add to Cart</button>
            </div>
            ''')
        html.append('</div>')
    html.append('</div>')
    return "".join(html)


def build_google_merchant_feed_xml(products):
    """Build Google Merchant Feed XML from products."""
    from xml.etree.ElementTree import Element, SubElement, tostring
    from xml.dom import minidom
    
    rss = Element('rss', version='2.0', xmlns__g='http://base.google.com/ns/1.0')
    rss.set('xmlns:g', 'http://base.google.com/ns/1.0')
    channel = SubElement(rss, 'channel')
    title = SubElement(channel, 'title')
    title.text = 'Pixie\'s Pantry'
    link = SubElement(channel, 'link')
    link.text = 'https://vapes.pixiespantryshop.com'
    description = SubElement(channel, 'description')
    description.text = 'Premium filtration and extraction systems for effortless sessions.'
    
    for _, product in products.items():
        item = SubElement(channel, 'item')
        SubElement(item, 'g:id').text = str(product.get('SKU', ''))
        SubElement(item, 'g:title').text = product.get('Product Name', '')
        SubElement(item, 'g:description').text = product.get('Product Name', '')
        SubElement(item, 'g:link').text = f"https://vapes.pixiespantryshop.com/products/{product.get('SKU', '')}"
        SubElement(item, 'g:image_link').text = product.get('Image URL', 'https://via.placeholder.com/300x300?text=No+Image')
        SubElement(item, 'g:price').text = f"{product.get('Your Online Price', '0.00')} USD"
        SubElement(item, 'g:availability').text = 'in stock'
        SubElement(item, 'g:brand').text = 'Pixie\'s Pantry'
        SubElement(item, 'g:condition').text = 'new'
    
    rough_string = tostring(rss, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
