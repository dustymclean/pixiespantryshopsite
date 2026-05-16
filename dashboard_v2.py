#!/usr/bin/env python3
"""
Pixie's Pantry Unified Dashboard - Three Store Control
Dyspensr + Synergy + Thermodyne all in one dashboard
"""
import http.server
import socketserver
import json
import os
import csv
import re
import hashlib
from datetime import datetime
from pathlib import Path
import urllib.parse
import subprocess

# Configuration
PORT = 8080
DIRECTORY = os.path.expanduser("~/Desktop")

# Store Paths
STORES = {
    "dyspensr": {
        "name": "Dyspensr Store",
        "url": "vapes.pixiespantryshop.com",
        "dir": os.path.expanduser("~/Desktop/Pixies_Vape_Shop"),
        "csv": os.path.expanduser("~/Desktop/Dyspensr_Master_Catalog_Priced.csv"),
        "json": None,
        "description": "Master catalog - all products",
        "enabled": True
    },
    "synergy": {
        "name": "Synergy Imports",
        "url": "vapes.pixiespantryshop.com",
        "dir": os.path.expanduser("~/Desktop/Synergy_Shop"),
        "csv": None,
        "json": os.path.expanduser("~/Desktop/Synergy_Scraper/synergy_products.json"),
        "description": "DaVinci & Eyce products",
        "enabled": True
    },
    "thermodyne": {
        "name": "Thermodyne Systems",
        "url": "thermodyne.pixiespantryshop.com",
        "dir": os.path.expanduser("~/Desktop/Thermodyne_Catalog"),
        "csv": os.path.expanduser("~/Desktop/Thermodyne_Catalog/Thermodyne_Products.csv"),
        "json": os.path.expanduser("~/Desktop/Thermodyne_Catalog/Thermodyne_Products.json"),
        "description": "Thermodyne Systems hardware",
        "enabled": True
    },
    "tokerpoker": {
        "name": "Toker Poker",
        "url": "tokerpoker.pixiespantryshop.com",
        "dir": os.path.expanduser("~/Desktop/Pixies_Vape_Shop"),
        "csv": None,
        "json": os.path.expanduser("~/Desktop/Pixies_Vape_Shop/tokerpoker_products.json"),
        "description": "Rolling accessories & tools",
        "enabled": True
    }
}

# Product data stores
products_data = {
    "dyspensr": {},
    "tokerpoker": {}
}

# Config data for each store
store_config = {
    "dyspensr": {"picks": [], "sales": {"items": [], "global_discount": 10}, "featured": [], "bundles": {}},
    "tokerpoker": {"picks": [], "sales": {"items": [], "global_discount": 10}, "featured": [], "bundles": {}}
}


def load_dyspensr_products():
    """Load Dyspensr master catalog CSV - ALL products"""
    global products_data
    products = {}

    csv_path = STORES["dyspensr"]["csv"]
    if not os.path.exists(csv_path):
        return

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sku = row.get("SKU", "").strip()
            if not sku or sku.lower() == "none":
                sku = "GEN-" + hashlib.md5((row.get("Product Name", "") + row.get("Variant", "")).encode()).hexdigest()[:8].upper()

            products[sku] = {
                "sku": sku,
                "store": "dyspensr",
                "brand": row.get("Brand", "Premium").strip(),
                "title": row.get("Product Name", "").strip(),
                "category": row.get("Product Type", "Accessories").strip() or "Accessories",
                "price": row.get("Your Retail Price", "0").strip(),
                "msrp": row.get("MSRP", "").strip(),
                "description": row.get("Meta Description", "").strip()[:500] if row.get("Meta Description") else "",
                "image_url": row.get("Image URL", "").strip(),
                "status": row.get("Status", "Active").strip(),
                "tags": row.get("Search Tags", "").strip()
            }

    products_data["dyspensr"] = products
    print(f"  ✓ Dyspensr: {len(products)} products")


def get_config_paths(store):
    """Get config file paths for a store"""
    base = STORES[store]["dir"]
    return {
        "picks": os.path.join(base, "pixies_picks.json"),
        "sales": os.path.join(base, "sales.json"),
        "featured": os.path.join(base, "featured.json"),
        "bundles": os.path.join(base, "bundles.json")
    }


def load_json_file(path, default=None):
    """Load a JSON file safely"""
    if default is None:
        default = {}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return default
    return default


def load_store_config(store):
    """Load configuration for a store"""
    paths = get_config_paths(store)
    
    store_config[store] = {
        "picks": load_json_file(paths["picks"], {"items": []}).get("items", []),
        "sales": load_json_file(paths["sales"], {"items": [], "global_discount": 10}),
        "featured": load_json_file(paths["featured"], {"items": []}).get("items", []),
        "bundles": load_json_file(paths["bundles"], {})
    }
    return store_config[store]


def load_toker_poker_products():
    """Load Toker Poker products from JSON"""
    global products_data
    products = {}

    json_path = STORES["tokerpoker"]["json"]
    if not os.path.exists(json_path):
        print(f"  ⚠ Toker Poker: No product file found at {json_path}")
        return

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        products_list = data if isinstance(data, list) else data.get("products", [])
        for p in products_list:
            sku = p.get("sku", "").strip() or p.get("handle", "").strip()
            if not sku:
                sku = "TP-" + hashlib.md5(p.get("title", "").encode()).hexdigest()[:8].upper()

            title = p.get("title", "").strip()
            if not title:
                continue

            products[sku] = {
                "sku": sku,
                "store": "tokerpoker",
                "brand": p.get("brand", "Toker Poker").strip(),
                "title": title,
                "category": p.get("product_type", "Rolling Accessories").strip() or "Rolling Accessories",
                "price": p.get("price", "10.99"),
                "msrp": p.get("msrp", "10.99"),
                "description": (p.get("description", "") or "")[:500],
                "image_url": p.get("image_url", ""),
                "status": "Active" if p.get("published", True) else "Hidden",
                "tags": p.get("tags", "")
            }

        products_data["tokerpoker"] = products
        print(f"  ✓ Toker Poker: {len(products)} products")

    except Exception as e:
        print(f"  ! Toker Poker JSON error: {e}")


def load_all_products():
    """Load all store products"""
    load_dyspensr_products()
    load_toker_poker_products()


class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def sync_to_medusa(self, product_data):
        """Push product data to Medusa Admin API"""
        medusa_url = "https://medusa.pixiespantryshop.com/admin/products"
        headers = {
            "Authorization": "Bearer YOUR_MEDUSA_API_KEY",
            "Content-Type": "application/json"
        }
        # Convert Pixie's schema to Medusa's format
        medusa_product = {
            "title": product_data.get("title"),
            "description": product_data.get("description"),
            "images": [product_data.get("image_url")] if product_data.get("image_url") else [],
            "variants": [{
                "title": "Default",
                "prices": [{
                    "currency_code": "usd",
                    "amount": int(float(product_data.get("price", 0)) * 100)
                }],
                "sku": product_data.get("sku"),
                "inventory_quantity": 100  # Default stock
            }]
        }
        try:
            response = requests.post(medusa_url, json=medusa_product, headers=headers)
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Medusa sync failed: {e}")
            return False

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.get_dashboard_html().encode("utf-8"))
            return

        # Product endpoints
        for store in ["dyspensr", "tokerpoker"]:
            if path == f"/api/{store}/products":
                self.send_json_response(list(products_data[store].values()))
                return

        self.send_error(404, "Page not found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else ""

        try:
            data = json.loads(post_data) if post_data else {}
        except:
            data = {}

        # Handle product creation
        for store in ["dyspensr", "tokerpoker"]:
            if f"/{store}/products/create" in path:
                # Auto-generate SKU if missing
                sku = data.get("sku") or f"PX-{hashlib.md5(data.get('title', '').encode()).hexdigest()[:6].upper()}"
                
                overrides_path = os.path.join(STORES[store]["dir"], "custom_products.json")
                overrides = load_json_file(overrides_path, {})
                
                new_product = {
                    "sku": sku,
                    "store": store,
                    "brand": data.get("brand", "Pixie's Pantry"),
                    "title": data.get("title"),
                    "category": data.get("category", "General"),
                    "price": str(data.get("price", "0")),
                    "msrp": str(data.get("msrp", data.get("price", "0"))),
                    "wholesale": str(data.get("wholesale", "0")),
                    "image_url": data.get("image_url", ""),
                    "description": data.get("description", ""),
                    "status": "Active"
                }
                
                # Save to local file system for persistence
                overrides[sku] = new_product
                save_json_file(overrides_path, overrides)
                
                # Update active dashboard memory
                products_data[store][sku] = new_product
                
                # Trigger storefront regeneration
                subprocess.Popen(f"cd {STORES[store]['dir']} && python3 generate_storefront.py", shell=True)
                
                # Sync to Medusa if requested
                if data.get("sync_medusa"):
                    self.sync_to_medusa(new_product)
                
                self.send_json_response({"success": True, "sku": sku})
                return

        self.send_error(404, "Endpoint not found")

    def send_json_response(self, data):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def get_dashboard_html(self):
        """Generate the dashboard HTML"""
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pixie's Pantry Dashboard</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f9f9f9;
            color: #333;
        }}
        .store-tabs {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }}
        .store-tab {{
            padding: 10px 20px;
            background: #333;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }}
        .store-tab.active {{
            background: #d4af37;
        }}
        .product-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
        }}
        .product-card {{
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            background: white;
        }}
        .product-card img {{
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 4px;
        }}
    </style>
</head>
<body>
    <h1>Pixie's Pantry Dashboard</h1>
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div class="store-tabs">
            <div class="store-tab active" onclick="loadStore('dyspensr')">Dyspensr</div>
            <div class="store-tab" onclick="loadStore('tokerpoker')">Toker Poker</div>
        </div>
        <button onclick="openCreateProductModal()" style="background: #d4af37; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer;">+ Add Product</button>
    </div>
    <div class="product-grid" id="productGrid">Loading...</div>
    
    <script>
        let allProducts = [];
        
        async function loadStore(store) {
            document.querySelectorAll('.store-tab').forEach(tab => tab.classList.remove('active'));
            event.target.classList.add('active');
            
            const response = await fetch(`/api/${{store}}/products`);
            allProducts = await response.json();
            renderProducts(allProducts);
        }
        
        function renderProducts(products) {
            const grid = document.getElementById('productGrid');
            grid.innerHTML = products.map(p => `
                <div class="product-card">
                    <img src="${{p.image_url}}" alt="${{p.title}}">
                    <h3>${{p.title}}</h3>
                    <p>${{p.price}}</p>
                </div>
            `).join('');
        }
        
        // Load Dyspensr by default
        loadStore('dyspensr');
    </script>
</body>
</html>
        """


def main():
    print("\n🦾 Pixie's Pantry Unified Dashboard")
    print("=" * 50)
    print("\nLoading product catalogs...")
    
    # Load all products
    load_dyspensr_products()
    load_toker_poker_products()
    
    # Load configs
    print("\nLoading configurations...")
    for store in ["dyspensr", "tokerpoker"]:
        load_store_config(store)
    
    # Start server
    print(f"\n🌐 Dashboard starting at http://localhost:{PORT}")
    print("📊 All products loaded - no limits!")
    print("\nPress Ctrl+C to stop.\n")
    
    # Use allow_reuse_address to prevent "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        httpd.serve_forever()


if __name__ == "__main__":
    main()