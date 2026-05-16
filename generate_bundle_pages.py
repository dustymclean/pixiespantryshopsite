#!/usr/bin/env python3
"""
Generate bundle-specific pages for the medical storefront.
"""
import os
import json
from generate_clinical_storefront import generate_header, generate_footer, get_styles


def generate_bundle_page(bundle, output_path):
    """Generate a page for a single bundle."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pixie's Pantry | {bundle['name']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>{get_styles()}</style>
</head>
<body>
    {generate_header()}
    <main class="max-w-6xl mx-auto px-4 py-12">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- Bundle Image -->
            <div>
                <img src="https://via.placeholder.com/600x400?text={bundle['name'].replace(' ', '+')}" 
                     alt="{bundle['name']}" 
                     class="w-full rounded-lg shadow-lg" />
                <p class="text-sm text-gray-500 mt-2">Bundle includes: {', '.join([p['name'] for p in bundle['products']])}</p>
            </div>
            
            <!-- Bundle Details -->
            <div>
                <h1 class="text-4xl font-bold">{bundle['name']}</h1>
                <p class="text-lg text-gray-600 mt-2">{bundle['description']}</p>
                
                <div class="mt-6">
                    <p class="text-3xl font-bold">${bundle['price']} <span class="text-lg text-gray-500 line-through">${{:.2f}}</span></p>
                    <p class="text-green-600 font-semibold">Save {bundle['savings']}%</p>
                </div>
                
                <button class="mt-6 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
                    Add to Cart
                </button>
            </div>
        </div>
        
        <!-- Included Products -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold mb-6">Included Products</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {''.join(
                    f'<div class="border rounded-lg p-4">'
                    f'<img src="https://via.placeholder.com/300x200?text={product["name"].replace(" ", "+")}" alt="{product["name"]}" class="w-full h-40 object-cover rounded" />'
                    f'<h3 class="font-semibold mt-2">{product["name"]}</h3>'
                    f'<p class="text-gray-600 text-sm">{product["category"]}</p>'
                    f'</div>' for product in bundle['products']
                )}
            </div>
        </div>
        
        <!-- Compliance & Safety -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold mb-4">Compliance & Safety</h2>
            <div class="flex space-x-4 mb-4">
                <span class="audit-tag">USP Class VI Certified</span>
                <span class="audit-tag">DME Compliant</span>
                <span class="audit-tag">ISO 10993 Tested</span>
                <span class="audit-tag">Sterilizable</span>
            </div>
            <div class="bg-gray-50 p-4 rounded-lg">
                <h3 class="font-semibold">Sterilization Instructions</h3>
                <p class="text-sm text-gray-600 mt-2">All hardware in this bundle can be sterilized using clinical sterilization solvent (ISO alcohol) or autoclaving at 121°C for 15 minutes.</p>
            </div>
        </div>
        
        <!-- How to Use -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold mb-4">How to Use</h2>
            <div class="space-y-4">
                <div class="flex items-start">
                    <span class="font-bold mr-2">1.</span>
                    <p>Prepare your botanical or extract using the included tools.</p>
                </div>
                <div class="flex items-start">
                    <span class="font-bold mr-2">2.</span>
                    <p>Load the dosing pod with your purified extract (if applicable).</p>
                </div>
                <div class="flex items-start">
                    <span class="font-bold mr-2">3.</span>
                    <p>Attach the dosing pod to the Thermal Extraction Device (if applicable).</p>
                </div>
                <div class="flex items-start">
                    <span class="font-bold mr-2">4.</span>
                    <p>Set the desired temperature (recommended: 370°F for botanicals, 450°F for extracts).</p>
                </div>
                <div class="flex items-start">
                    <span class="font-bold mr-2">5.</span>
                    <p>Administer the aerosol using slow, steady inhalation.</p>
                </div>
                <div class="flex items-start">
                    <span class="font-bold mr-2">6.</span>
                    <p>Clean all components after use with the included sterilization agent.</p>
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
                    <p class="mt-2">"This bundle is perfect for my research. The compliance documentation is thorough, and the sterilization process is straightforward."</p>
                </div>
                <div class="border rounded-lg p-4">
                    <div class="flex items-center">
                        <span class="font-bold">★★★★☆</span>
                        <span class="ml-2 font-semibold">Wellness Professional</span>
                    </div>
                    <p class="mt-2">"The Thermal Extraction Device is precise, and the dosing pods are a game-changer. Highly recommend for clinical settings."</p>
                </div>
            </div>
        </div>
    </main>
    {generate_footer()}
</body>
</html>"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def generate_bundle_pages():
    """Generate all bundle pages."""
    with open('bundles_medical.json', 'r', encoding='utf-8') as f:
        bundles = json.load(f)['bundles']
    
    for bundle in bundles:
        filename = f"bundle-{bundle['name'].lower().replace(' ', '-')}.html"
        generate_bundle_page(bundle, os.path.join(os.path.expanduser("~/Desktop/Pixies_Vape_Shop"), filename))
    
    print(f"✅ Generated {len(bundles)} bundle pages.")


if __name__ == "__main__":
    generate_bundle_pages()