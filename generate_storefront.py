#!/usr/bin/env python3
"""
Generate the Pixie's Pantry storefront HTML from product data.
"""
import os
import csv


def generate_storefront():
    """Generate the storefront HTML."""
    # Load product data
    products = []
    csv_path = os.path.expanduser("~/Desktop/Dyspensr_Master_Catalog_Priced.csv")
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Skip inactive or invalid products
                status = row.get("Status", "") or ""
                if status.strip().lower() not in ["active", ""]:
                    continue
                
                sku = row.get("SKU", "") or ""
                title = row.get("Product Name", "") or ""
                if not sku.strip() or not title.strip():
                    continue
                
                products.append({
                    "sku": sku.strip(),
                    "title": title.strip(),
                    "price": row.get("Your Retail Price", "0").strip(),
                    "image_url": row.get("Image URL", "").strip(),
                    "description": row.get("Meta Description", "").strip(),
                    "category": row.get("Product Type", "General").strip()
                })
    
    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pixie's Pantry</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
        
        body {
            font-family: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            margin: 0;
            padding: 0;
            background: #f9f9f9;
            color: #333;
        }
        
        /* Header for mobile navigation */
        header {
            position: sticky;
            top: 0;
            background: white;
            z-index: 100;
            padding: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .search-bar {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            width: 100%;
            box-sizing: border-box;
        }
        
        .hamburger-menu {
            display: none;
            font-size: 24px;
            cursor: pointer;
            padding: 5px;
        }
        
        .mobile-nav {
            display: none;
            background: white;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        
        .mobile-nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .mobile-nav a {
            text-decoration: none;
            color: #333;
            font-weight: bold;
        }
        
        .scrolling-banner {
            overflow: hidden;
            white-space: nowrap;
            background: #333;
            color: white;
            padding: 10px 0;
            width: 100%;
        }
        
        .scrolling-text {
            display: inline-block;
            padding-left: 100%;
            animation: scroll 20s linear infinite;
        }
        
        .scrolling-text span {
            margin-right: 50px;
            display: inline-block;
        }
        
        .scrolling-text a {
            color: #d4af37;
            text-decoration: none;
        }
        
        .scrolling-text a:hover {
            text-decoration: underline;
        }
        
        @keyframes scroll {
            0% { transform: translateX(0); }
            100% { transform: translateX(-100%); }
        }
        
        .founder-note {
            background: #fff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            margin: 20px auto;
            max-width: 800px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .founder-note h3 {
            margin-top: 0;
            color: #d4af37;
            font-size: 24px;
        }
        
        .founder-note p {
            margin-bottom: 12px;
            line-height: 1.6;
            color: #444;
        }
        
        .founder-note a {
            color: #d4af37;
            text-decoration: none;
            font-weight: bold;
        }
        
        .founder-note a:hover {
            text-decoration: underline;
        }
        
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        
        .product-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            background: white;
            transition: box-shadow 0.3s;
        }
        
        .product-card:hover {
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        
        .product-card img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 4px;
        }
        
        .product-card h3 {
            margin: 10px 0 5px;
            font-size: 16px;
        }
        
        .product-card p {
            margin: 5px 0;
            color: #666;
        }
        
        /* Mobile-Specific Styles */
        @media (max-width: 768px) {
            .hamburger-menu {
                display: block;
            }
            .mobile-nav {
                display: block;
            }
            .product-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
                padding: 10px;
            }
            .founder-note {
                margin: 10px;
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="hamburger-menu">☰</div>
        <nav class="mobile-nav">
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Shop</a></li>
                <li><a href="#">Cart</a></li>
            </ul>
        </nav>
        <input type="text" class="search-bar" placeholder="Search products...">
    </header>
    
    <div class="scrolling-banner">
        <div class="scrolling-text">
            <span>JOIN THE DISCORD FOR EXCLUSIVE WHOLESALE PRICING · <a href="https://discord.com/invite/ph4ehWXQAe" target="_blank">DISCORD.COM/INVITE/PH4EHWXQAE</a></span>
            <span>Just a single mom trying to make a dream happen. I’ve built this store from scratch.</span>
        </div>
    </div>
    
    <div class="founder-note">
        <h3>A Note From the Founder</h3>
        <p>Hi, I’m Dusty—a single mom building Pixie’s Pantry for my daughter’s future.</p>
        <p>Every purchase you make supports my family and fuels my mission to make wellness tools accessible to everyone. No corporate markup, no middlemen—just fair prices and products I stand behind.</p>
        <p>For the best deals, join our <a href="https://discord.com/invite/ph4ehWXQAe" target="_blank">Discord</a>.</p>
    </div>
    
    <div class="product-grid">
    """

    # Add products to HTML
    for product in products:
        html += f"""
        <div class="product-card">
            <img src="{product['image_url']}" alt="{product['title']}" loading="lazy" onerror="this.src='https://placehold.co/200x200?text=No+Image';">
            <h3>{product['title']}</h3>
            <p>${product['price']}</p>
        </div>
        """

    html += """
    </div>
</body>
</html>
    """

    # Save HTML
    output_path = os.path.expanduser("~/Desktop/Pixies_Vape_Shop/index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated storefront: {output_path}")


if __name__ == "__main__":
    generate_storefront()