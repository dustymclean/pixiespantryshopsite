#!/usr/bin/env python3
"""
Generate the Toker Poker storefront HTML to match tokerpoker.com
"""
import os
import json


def generate_toker_poker_storefront():
    """Generate the Toker Poker storefront HTML."""
    # Load Toker Poker products
    products = []
    json_path = os.path.expanduser("~/Desktop/Pixies_Vape_Shop/tokerpoker_products.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            products = json.load(f)
    
    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Toker Poker - Premium Rolling Accessories</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 0;
            background: #1a1a1a;
            color: #fff;
        }}
        
        /* Hero Section */
        .hero {{
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://tokerpoker.com/wp-content/uploads/2022/05/tokers-banner-2-scaled.jpg');
            background-size: cover;
            background-position: center;
            padding: 100px 20px;
            text-align: center;
            color: #fff;
        }}
        
        .hero h1 {{
            font-size: 3em;
            margin: 0;
            color: #d4af37;
        }}
        
        .hero p {{
            font-size: 1.2em;
            margin: 20px 0 30px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        .btn {{
            background: #d4af37;
            color: #1a1a1a;
            padding: 12px 30px;
            border: none;
            border-radius: 4px;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
        }}
        
        /* Navigation */
        .nav {{
            background: #000;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            font-size: 1.5em;
            font-weight: bold;
            color: #d4af37;
        }}
        
        .nav-links {{
            display: flex;
            gap: 20px;
        }}
        
        .nav-links a {{
            color: #fff;
            text-decoration: none;
        }}
        
        /* Product Grid */
        .product-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            padding: 40px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .product-card {{
            background: #2a2a2a;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s;
        }}
        
        .product-card:hover {{
            transform: translateY(-5px);
        }}
        
        .product-card img {{
            width: 100%;
            height: 200px;
            object-fit: cover;
        }}
        
        .product-info {{
            padding: 15px;
        }}
        
        .product-info h3 {{
            margin: 0 0 10px;
            color: #d4af37;
        }}
        
        .product-info p {{
            margin: 0;
            color: #ccc;
        }}
        
        /* Footer */
        .footer {{
            background: #000;
            padding: 40px 20px;
            text-align: center;
        }}
        
        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }}
        
        .footer-links a {{
            color: #fff;
            text-decoration: none;
        }}
        
        .footer p {{
            color: #888;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <div class="nav">
        <div class="logo">Toker Poker</div>
        <div class="nav-links">
            <a href="#">Home</a>
            <a href="#">Shop</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
        </div>
    </div>
    
    <!-- Hero Section -->
    <div class="hero">
        <h1>Premium Rolling Accessories</h1>
        <p>Elevate your rolling experience with Toker Poker's high-quality lighters and tools.</p>
        <a href="#products" class="btn">Shop Now</a>
    </div>
    
    <!-- Product Grid -->
    <div class="product-grid" id="products">
    """

    # Add products to HTML
    for product in products:
        html += f"""
        <div class="product-card">
            <img src="{product.get('image_url', 'https://placehold.co/400x300/1a1a1a/d4af37?text=Toker+Poker')}" alt="{product.get('title', 'Product')}">
            <div class="product-info">
                <h3>{product.get('title', 'Product')}</h3>
                <p>${product.get('price', '10.99')}</p>
            </div>
        </div>
        """

    html += """
    </div>
    
    <!-- Footer -->
    <div class="footer">
        <div class="footer-links">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Contact Us</a>
        </div>
        <p>&copy; 2026 Toker Poker. All rights reserved.</p>
    </div>
</body>
</html>
    """

    # Save HTML
    output_path = os.path.expanduser("~/Desktop/Pixies_Vape_Shop/toker_poker.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Toker Poker storefront: {output_path}")


if __name__ == "__main__":
    generate_toker_poker_storefront()