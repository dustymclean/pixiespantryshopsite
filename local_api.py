#!/usr/bin/env python3
"""
Local API for Pixie's Pantry clinical storefront.
"""
import http.server
import socketserver
import json
import os
import csv

PORT = 8000

class APIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/products":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            # Load products from CSV
            products = []
            csv_path = os.path.expanduser("~/Desktop/Dyspensr_Master_Catalog_Priced.csv")
            if os.path.exists(csv_path):
                with open(csv_path, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
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
            
            self.wfile.write(json.dumps(products).encode())
            return
        
        # Serve static files
        super().do_GET()


def run_api():
    with socketserver.TCPServer(("", PORT), APIHandler) as httpd:
        print(f"Local API running at http://localhost:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    run_api()