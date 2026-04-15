"""
Dashboard Configuration Integration
Loads Pixie's Picks, Sales, Featured items, Bundles, and Carousels
for use by the storefront generator.
"""
import json
import os

DATA_DIR = os.path.expanduser("~/Desktop/Pixies_Vape_Shop")
BUNDLES_PATH = os.path.join(DATA_DIR, "bundles.json")
FEATURED_PATH = os.path.join(DATA_DIR, "featured.json")
SALES_PATH = os.path.join(DATA_DIR, "sales.json")
PICKS_PATH = os.path.join(DATA_DIR, "pixies_picks.json")
CAROUSELS_PATH = os.path.join(DATA_DIR, "carousels.json")
TOKER_POKER_CSV = os.path.expanduser("~/Desktop/Toker_Poker_Products.csv")


def load_json_file(path, default=None):
    """Load a JSON file safely"""
    if default is None:
        default = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Could not load {path}: {e}")
            return default
    return default


def get_picks():
    """Get list of Pixie's Pick SKUs"""
    data = load_json_file(PICKS_PATH, {"items": []})
    return data.get("items", [])


def get_sales():
    """Get sales data (items on sale and global discount)"""
    data = load_json_file(SALES_PATH, {"items": [], "global_discount": 10})
    return {
        "items": data.get("items", []),
        "global_discount": data.get("global_discount", 10)
    }


def get_featured():
    """Get featured items"""
    data = load_json_file(FEATURED_PATH, {"items": []})
    return data.get("items", [])


def get_bundles():
    """Get all active bundles"""
    data = load_json_file(BUNDLES_PATH, {})
    bundles = {}

    for bundle_id, bundle in data.items():
        if isinstance(bundle, dict) and bundle.get("active", True):
            # Ensure the bundle applies to the correct website
            website = bundle.get("website", "").lower()
            if website == "tokerpoker.pixiespantryshop.com":
                bundles[bundle_id] = bundle

    return bundles


def get_carousels():
    """Get featured carousels"""
    data = load_json_file(CAROUSELS_PATH, {"carousels": []})
    return data.get("carousels", [])


def load_toker_poker_products():
    """Load Toker Poker products from CSV"""
    import csv
    products = {}

    if not os.path.exists(TOKER_POKER_CSV):
        print(f"Warning: Toker Poker CSV not found at {TOKER_POKER_CSV}")
        return products

    try:
        with open(TOKER_POKER_CSV, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                sku = row.get("SKU", "").strip()
                if not sku:
                    continue
                products[sku] = {
                    "brand": row.get("Brand", "Toker Poker"),
                    "product_name": row.get("Product Name", ""),
                    "sku": sku,
                    "price": float(row.get("Your Online Price", 0)),
                    "inventory": int(row.get("Inventory", 0)),
                    "bundle_eligible": row.get("Bundle Eligible", "No").lower() == "yes",
                    "website": "tokerpoker.pixiespantryshop.com"
                }
        return products
    except Exception as e:
        print(f"Warning: Could not load Toker Poker CSV: {e}")
        return {}


def is_pick(sku):
    """Check if SKU is a Pixie's Pick"""
    return sku in get_picks()


def is_on_sale(sku):
    """Check if SKU is on sale"""
    return sku in get_sales()["items"]


def is_featured(sku):
    """Check if SKU is featured"""
    return sku in get_featured()


def is_toker_poker_product(sku):
    """Check if SKU is a Toker Poker product"""
    toker_products = load_toker_poker_products()
    return sku in toker_products


def get_sale_price(original_price, sku):
    """Calculate sale price for an item"""
    sales = get_sales()
    if sku in sales["items"]:
        discount = sales["global_discount"]
        return original_price * (1 - discount / 100)
    return original_price


def get_product_badges(sku):
    """Get all badges for a product"""
    badges = []
    if is_pick(sku):
        badges.append({
            "type": "pick",
            "label": "Pixie's Pick",
            "color": "#d4af37",
            "position": "top-left"
        })
    if is_on_sale(sku):
        badges.append({
            "type": "sale",
            "label": "On Sale",
            "color": "#e74c3c",
            "position": "top-right"
        })
    if is_featured(sku):
        badges.append({
            "type": "featured",
            "label": "Featured",
            "color": "#9b59b6",
            "position": "bottom-left"
        })
    if is_toker_poker_product(sku):
        badges.append({
            "type": "toker_poker",
            "label": "Toker Poker",
            "color": "#2ecc71",
            "position": "bottom-right"
        })
    return badges


def build_badge_html(sku):
    """Build HTML for product badges (golden banner for picks, sale banner for sales)"""
    badges = get_product_badges(sku)
    html_parts = []

    for badge in badges:
        if badge["type"] == "pick":
            # Golden banner for Pixie's Picks (top-left)
            html_parts.append(f'''<div class="badge-pick" style="position:absolute;top:10px;left:10px;background:linear-gradient(135deg,#d4af37,#f4d03f);color:#111;padding:5px 12px;font-size:0.75em;font-weight:700;text-transform:uppercase;border-radius:4px;box-shadow:0 2px 8px rgba(212,175,55,0.4);">⭐ Pixie's Pick</div>''')
        elif badge["type"] == "sale":
            # Red banner for sales (top-right)
            html_parts.append(f'''<div class="badge-sale" style="position:absolute;top:10px;right:10px;background:#e74c3c;color:#fff;padding:5px 12px;font-size:0.75em;font-weight:700;text-transform:uppercase;border-radius:4px;">🔥 On Sale</div>''')
        elif badge["type"] == "featured":
            # Purple banner for featured (bottom-left)
            html_parts.append(f'''<div class="badge-featured" style="position:absolute;bottom:10px;left:10px;background:#9b59b6;color:#fff;padding:5px 12px;font-size:0.75em;font-weight:700;border-radius:4px;">⭐ Featured</div>''')

    return "".join(html_parts)


def build_bundle_section():
    """Build HTML section for bundles"""
    bundles = get_bundles()
    if not bundles:
        return ""

    html_parts = [build_banner(), '''
<section id="bundles" class="bundles-section" style="padding:40px 20px;background:rgba(212,175,55,0.05);">
    <h2 style="text-align:center;font-size:2em;margin-bottom:30px;color:#d4af37;">📦 Premium Bundles</h2>
    <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;">
''']

    for bundle_id, bundle in bundles.items():
        name = bundle.get("name", "Premium Bundle")
        discount = bundle.get("discount", 15)
        desc = bundle.get("description", "")
        products = bundle.get("products", [])

        # Calculate bundle savings
        total_price = 0
        product_cards = []
        for sku in products[:4]:  # Show max 4 products
            # This would need product data passed in, so we'll use placeholder
            product_cards.append(f'<div style="background:#2a2a3e;padding:10px;border-radius:8px;margin:5px;">SKU: {sku}</div>')

        html_parts.append(f'''
        <div class="bundle-card" style="background:rgba(255,255,255,0.05);border:2px solid #d4af37;border-radius:16px;padding:20px;">
            <h3 style="color:#d4af37;margin-bottom:10px;">{name}</h3>
            <div style="background:#1a1a2e;border-radius:8px;padding:10px;margin:10px 0;">
                {"".join(product_cards[:3])}
                {f'<div style="text-align:center;color:#888;margin-top:5px;">+{len(products)-3} more</div>' if len(products) > 3 else ''}
            </div>
            <div style="color:#e74c3c;font-weight:bold;font-size:1.5em;">{discount}% OFF Bundle</div>
            <p style="color:#888;font-size:0.9em;margin-top:10px;">{desc[:150]}...</p>
            <button onclick="contactForBundle('{bundle_id}')" style="background:linear-gradient(135deg,#d4af37,#b8960c);color:#111;border:none;padding:12px 24px;border-radius:8px;font-weight:600;cursor:pointer;margin-top:15px;width:100%;">Contact for Bundle Price</button>
        </div>
''')

    html_parts.append('</div></section>')
    return "".join(html_parts)


def build_carousels_section():
    """Build HTML for featured carousels"""
    carousels = get_carousels()
    if not carousels:
        return ""

    html_parts = []
    for carousel in carousels:
        title = carousel.get("title", "Featured Collection")
        layout = carousel.get("layout", "grid")
        c_id = carousel.get("id", "carousel")

        html_parts.append(f'''
<div class="carousel-section" style="padding:20px 0;">
    <h3 style="font-size:1.5em;margin-bottom:15px;color:#fff;">{title}</h3>
    <div id="{c_id}" class="carousel-{layout}" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:15px;">
    </div>
</div>
''')

    return "".join(html_parts)


def build_google_merchant_feed_xml(products_dict):
    """
    Build Google Merchant Center XML feed with all enriched data
    This should be called by generate_storefront.py
    """
    import re

    picks = get_picks()
    sales = get_sales()
    featured = get_featured()

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<rss xmlns:g="http://base.google.com/ns/1.0" version="2.0">')
    lines.append('<channel>')
    lines.append('<title>Pixie\'s Pantry</title>')
    lines.append('<link>https://vapes.pixiespantryshop.com</link>')
    lines.append('<description>Premium aromatherapy devices and accessories</description>')
    lines.append('<language>en-us</language>')

    for sku, p in products_dict.items():
        status = p.get("status", "Active")
        if status.lower() in ["hidden", "inactive", ""]:
            continue

        price = p.get("price", "0")
        try:
            price_val = float(str(price).replace("$", ""))
            if price_val <= 0:
                continue
        except:
            continue

        title = p.get("seo_title") or p.get("title", "Product")
        desc = p.get("description") or f"Premium {p.get('category', 'product')} from {p.get('brand', 'top brand')}"
        image = p.get("image_url", "")
        url = f"https://vapes.pixiespantryshop.com/products/{p.get('url_handle', sku)}"

        # Google-safe content
        safe_title = re.sub(r'(?i)\bvape(?:s|rs|ing)?\b', 'Aromatherapy Device', title)
        safe_desc = re.sub(r'(?i)\bvape(?:s|rs|ing)?\b', 'aromatherapy device', desc)

        lines.append('<item>')
        lines.append(f'    <g:id>{sku}</g:id>')
        lines.append(f'    <g:title><![CDATA[{safe_title[:150]}]]></g:title>')
        lines.append(f'    <g:description><![CDATA[{safe_desc[:5000]}]]></g:description>')
        lines.append(f'    <g:link>{url}</g:link>')
        lines.append(f'    <g:image_link>{image}</g:image_link>')
        lines.append(f'    <g:price>{price_val:.2f} USD</g:price>')

        # Sale price if on sale
        if sku in sales["items"]:
            sale_price = price_val * (1 - sales["global_discount"] / 100)
            lines.append(f'    <g:sale_price>{sale_price:.2f} USD</g:sale_price>')

        lines.append('    <g:availability>in stock</g:availability>')
        lines.append('    <g:condition>new</g:condition>')
        lines.append(f'    <g:brand><![CDATA[{p.get("brand", "Premium")}]]></g:brand>')

        if p.get("category"):
            lines.append(f'    <g:product_type><![CDATA[{p.get("category")}]]></g:product_type>')

        # Custom labels for Google Shopping campaigns
        if sku in picks:
            lines.append('    <g:custom_label_0>Pixies Pick</g:custom_label_0>')
        if sku in sales["items"]:
            lines.append('    <g:custom_label_1>On Sale</g:custom_label_1>')
        if sku in featured:
            lines.append('    <g:custom_label_2>Featured</g:custom_label_2>')

        lines.append('</item>')

    lines.append('</channel>')
    lines.append('</rss>')

    return "\n".join(lines)


# Convenience function to get all config at once
def calculate_bundle_price(cart_items, bundle_id):
    """Calculate the final price for a bundle, including surcharges and discounts"""
    bundles = get_bundles()
    bundle = bundles.get(bundle_id, {})
    discount_type = bundle.get("discount_type")
    discount_value = bundle.get("discount_value", 0)
    min_items = bundle.get("min_items", 0)
    surcharge_skus = bundle.get("surcharge", {}).get("premium_skus", [])
    surcharge_amount = bundle.get("surcharge", {}).get("amount", 0)
    free_shipping_threshold = bundle.get("shipping", {}).get("free_threshold", 0)

    # Filter cart items to only include Toker Poker products in the bundle
    toker_poker_items = [item for item in cart_items if is_toker_poker_product(item["sku"])]
    if len(toker_poker_items) < min_items:
        return None  # Bundle not applicable

    # Calculate subtotal
    subtotal = sum(item["price"] for item in toker_poker_items)

    # Apply surcharges for premium SKUs
    surcharge_total = sum(surcharge_amount for item in toker_poker_items if item["sku"] in surcharge_skus)

    # Apply discount
    if discount_type == "percentage":
        discount = subtotal * (discount_value / 100)
    elif discount_type == "free_lowest_item":
        discount = min(item["price"] for item in toker_poker_items)
    else:
        discount = 0

    # Calculate shipping
    shipping_cost = 0 if subtotal >= free_shipping_threshold else bundle.get("shipping", {}).get("flat_rate", 0)

    # Final price
    total = (subtotal + surcharge_total) - discount + shipping_cost
    return {
        "subtotal": subtotal,
        "surcharge": surcharge_total,
        "discount": discount,
        "shipping": shipping_cost,
        "total": total
    }


def build_banner():
    """Build the banner for Toker Poker bundles"""
    return '''
<div style="background: linear-gradient(90deg, #2ecc71, #3498db); color: white; padding: 15px; text-align: center; font-size: 1.2em; font-weight: bold; margin-bottom: 20px;">
    🚀 BUNDLE & SAVE: Buy 5 Toker Pokers, Get the 6th FREE + FREE Shipping!
    <a href="#bundles" style="color: white; text-decoration: underline; margin-left: 10px;">[BUILD YOUR PACK]</a>
</div>
'''


def get_all_config():
    """Get all dashboard configuration in one call"""
    return {
        "picks": get_picks(),
        "sales": get_sales(),
        "featured": get_featured(),
        "bundles": get_bundles(),
        "carousels": get_carousels()
    }


if __name__ == "__main__":
    # Test the module
    print("Dashboard Configuration Module")
    print("=" * 40)
    print(f"Pixie's Picks: {len(get_picks())} items")
    print(f"On Sale: {len(get_sales()['items'])} items")
    print(f"Featured: {len(get_featured())} items")
    print(f"Bundles: {len(get_bundles())} active")
    print(f"Carousels: {len(get_carousels())} configured")