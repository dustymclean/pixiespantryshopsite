#!/usr/bin/env python3
"""
Generate individual product pages for the medical storefront.
"""
import os
import csv
from generate_clinical_storefront import generate_header, generate_footer, get_styles


def generate_product_page(product, output_path):
    """Generate a page for a single product."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pixie's Pantry | {product['name']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>{get_styles()}</style>
</head>
<body>
    {generate_header()}
    <main class="max-w-6xl mx-auto px-4 py-12">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- Product Image -->
            <div>
                <img src="{product.get('image_url', 'https://via.placeholder.com/600x400?text=No+Image')}" 
                     alt="{product['name']}" 
                     class="w-full rounded-lg shadow-lg" />
            </div>
            
            <!-- Product Details -->
            <div>
                <h1 class="text-4xl font-bold">{product['name']}</h1>
                <p class="text-lg text-gray-600 mt-2">{product.get('description', 'Description not available.')}</p>
                
                <div class="mt-6">
                    <p class="text-3xl font-bold">${product.get('price', '0.00')}</p>
                </div>
                
                <button class="mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
                    Add to Cart
                </button>
                
                <!-- Compliance Badges -->
                <div class="mt-6 flex space-x-4">
                    <span class="audit-tag">USP Class VI Certified</span>
                    <span class="audit-tag">DME Compliant</span>
                    <span class="audit-tag">Sterilizable</span>
                </div>
            </div>
        </div>
        
        <!-- Clinical Use Cases -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold mb-4">Clinical Use Cases</h2>
            <div class="space-y-4">
                <div class="flex items-start">
                    <span class="font-bold mr-2">1.</span>
                    <p>Precision dosing for botanical administration.</p>
                </div>
                <div class="flex items-start">
                    <span class="font-bold mr-2">2.</span>
                    <p>Purified aerosol delivery for clinical research.</p>
                </div>
                <div class="flex items-start">
                    <span class="font-bold mr-2">3.</span>
                    <p>Sterilizable components for repeated use in medical settings.</p>
                </div>
            </div>
        </div>
        
        <!-- Customer Reviews (Placeholder) -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold mb-4">Customer Reviews</h2>
            <div class="space-y-4">
                <div class="border rounded-lg p-4">
                    <div class="flex items-center">
                        <span class="font-bold">★★★★★</span>
                        <span class="ml-2 font-semibold">Verified Clinical User</span>
                    </div>
                    <p class="mt-2">"This product meets all DME compliance standards. The sterilization process is straightforward and effective."</p>
                </div>
                <div class="border rounded-lg p-4">
                    <div class="flex items-center">
                        <span class="font-bold">★★★★☆</span>
                        <span class="ml-2 font-semibold">Wellness Professional</span>
                    </div>
                    <p class="mt-2">"The precision dosing is excellent, and the build quality is top-notch. Highly recommend for clinical settings."</p>
                </div>
            </div>
        </div>
        
        <!-- Related Products -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold mb-4">Related Products</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                    <img src="https://via.placeholder.com/300x200?text=Related+Product+1" 
                         alt="Related Product 1" 
                         class="w-full h-32 object-cover rounded" />
                    <h3 class="font-semibold mt-2">Related Product 1</h3>
                    <p class="text-gray-600 text-sm">$99.99</p>
                </div>
                <div class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                    <img src="https://via.placeholder.com/300x200?text=Related+Product+2" 
                         alt="Related Product 2" 
                         class="w-full h-32 object-cover rounded" />
                    <h3 class="font-semibold mt-2">Related Product 2</h3>
                    <p class="text-gray-600 text-sm">$129.99</p>
                </div>
            </div>
        </div>
    </main>
    {generate_footer()}
</body>
</html>"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def generate_product_pages():
    """Generate all product pages."""
    input_csv = os.path.expanduser("~/Desktop/Medical_Pivot_Master_Catalog.csv")
    output_dir = os.path.expanduser("~/Desktop/Pixies_Vape_Shop")
    
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for product in reader:
            if not product.get('SKU'):
                continue
            filename = f"product-{product['SKU'].lower().replace(' ', '-')}.html"
            generate_product_page(product, os.path.join(output_dir, filename))
    
    print(f"✅ Generated {len(list(csv.DictReader(open(input_csv))))} product pages.")


if __name__ == "__main__":
    generate_product_pages()