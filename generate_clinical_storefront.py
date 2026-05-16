#!/usr/bin/env python3
"""
Generate the Pixie's Pantry clinical storefront HTML.
"""
import os
import csv
import json


def get_styles():
    """Return Tailwind CSS styles."""
    return """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

    :root {
        --bg: #fbfbf9;
        --ink: #111111;
        --muted: #6b6b66;
        --accent: #2563eb;
        --line: #e5e5e0;
    }

    body {
        background-color: var(--bg);
        color: var(--ink);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        line-height: 1.5;
    }

    .mono { font-family: 'JetBrains Mono', monospace; }
    .index-border { border: 1px solid var(--line); }

    .audit-tag {
        font-size: 10px;
        font-weight: 700;
        padding: 2px 8px;
        background: var(--ink);
        color: #fff;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .system-card {
        background: #fff;
        transition: all 0.2s ease;
    }

    .system-card:hover {
        border-color: var(--ink);
        transform: translateY(-2px);
    }

    .blueprint-bg {
        background-image: radial-gradient(var(--line) 0.5px, transparent 0.5px);
        background-size: 20px 20px;
    }
    """


def generate_header():
    """Generate the site header."""
    return """
    <header class="border-b border-gray-200">
        <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="/" class="text-2xl font-bold">Pixie's Pantry</a>
            <nav class="flex space-x-6">
                <a href="/" class="hover:text-blue-600">Clinical Index</a>
                <a href="/dme-standards.html" class="hover:text-blue-600">DME Standards</a>
            </nav>
        </div>
    </header>
    """


def generate_footer():
    """Generate the site footer."""
    return """
    <footer class="border-t border-gray-200 mt-16">
        <div class="max-w-6xl mx-auto px-4 py-8 text-center text-sm text-gray-500">
            <p>© 2026 Pixie's Pantry. All rights reserved.</p>
            <p class="mt-2">For clinical and research use only.</p>
        </div>
    </footer>
    """


def generate_category_page(products, category_name, category_description, output_path):
    """Generate a category-specific page with pagination."""
    category_products = [p for p in products if p.get("category", "").lower() == category_name.lower()]
    
    # Pagination settings
    products_per_page = 50
    total_pages = (len(category_products) + products_per_page - 1) // products_per_page
    
    # Generate product grid for page 1
    product_grid = ''
    for product in category_products[:products_per_page]:
        product_grid += f'''
        <div class="system-card border rounded-lg p-6 shadow-sm">
            <img src="{product.get('image_url', 'https://via.placeholder.com/300x200?text=No+Image')}" 
                 alt="{product.get('name', 'Product')}" 
                 class="w-full h-48 object-cover mb-4" />
            <h2 class="text-xl font-semibold">{product.get('name', 'Product')}</h2>
            <p class="text-gray-600 mt-2">{product.get('description', 'Description not available.')[:150]}...</p>
            <div class="mt-4 flex justify-between items-center">
                <span class="font-bold">${product.get('price', '0.00')}</span>
                <a href="#" class="text-blue-600 hover:underline">Details</a>
            </div>
        </div>
        '''
    
    # Generate pagination links
    pagination_links = ''
    if total_pages > 1:
        pagination_links = '<div class="mt-8 flex justify-center space-x-2">'
        for page in range(1, total_pages + 1):
            active = 'bg-blue-600 text-white' if page == 1 else 'bg-gray-200'
            pagination_links += f'''
            <a href="{output_path.replace('.html', f'-page-{page}.html')}" 
               class="px-4 py-2 rounded {active}">{page}</a>
            '''
        pagination_links += '</div>'
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pixie's Pantry | {category_name}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>{get_styles()}</style>
</head>
<body>
    {generate_header()}
    <main class="max-w-6xl mx-auto px-4 py-12">
        <h1 class="text-4xl font-bold mb-4">{category_name}</h1>
        <p class="text-lg text-gray-600 mb-8">{category_description}</p>
        
        <!-- Products Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {product_grid}
        </div>
        
        <!-- Pagination -->
        {pagination_links}
        
        <!-- Relevant Bundles -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold mb-6">Recommended Bundles</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {''.join([
                    f'''<a href="{bundle['link']}" class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                        <h3 class="font-semibold">{bundle['name']}</h3>
                        <p class="text-gray-600 text-sm">{bundle['description']}</p>
                        <p class="font-bold mt-2">${bundle['price']} <span class="text-sm text-gray-500 line-through">${bundle['original_price']}</span></p>
                    </a>''' for bundle in {
                        'Cluster A: Active Electronic TEDs': [
                            {'name': 'Wellness Starter Kit', 'link': 'bundle-wellness-starter-kit.html', 'description': 'Thermal Extraction Device + Dosing Pods + Homogenizer', 'price': '299.00', 'original_price': '349.00'},
                            {'name': 'Thermal Extraction Pro Bundle', 'link': 'bundle-thermal-extraction-pro-bundle.html', 'description': 'Portable TED + Extracts + Sterilization Agent', 'price': '279.00', 'original_price': '340.00'},
                            {'name': 'DaVinci IQ3 + Accessories', 'link': 'bundle-davinci-iq3-accessories.html', 'description': 'IQ3 TED + Stainless Pods + Dosage Grinder', 'price': '329.00', 'original_price': '399.00'},
                            {'name': 'PAX 3 Complete Kit', 'link': 'bundle-pax-3-complete.html', 'description': 'PAX 3 TED + Concentrate Insert + Cleaning Kit', 'price': '249.00', 'original_price': '299.00'}
                        ],
                        'Cluster B: Passive/Manual TEDs': [
                            {'name': 'Clinical Extract Bundle', 'link': 'bundle-clinical-extract-bundle.html', 'description': 'Concentrate Console + Extracts + Sterilization Agent', 'price': '249.00', 'original_price': '311.00'},
                            {'name': 'ARTIQ + Groove Cara', 'link': 'bundle-artiq-groove-cara.html', 'description': 'ARTIQ Console + Dual-Use Attachment', 'price': '549.00', 'original_price': '649.00'}
                        ],
                        'Cluster C: Hydrated Filters': [
                            {'name': 'Hydrated Filtration System', 'link': 'bundle-hydrated-filtration-system.html', 'description': 'Hydro-Filtration Vessel + Downstem + Percolator', 'price': '129.00', 'original_price': '143.00'},
                            {'name': 'Eyce Silicone Bong + Extract Kit', 'link': 'bundle-eyce-bong-extract-kit.html', 'description': 'Silicone Hydro-Filtration Vessel + Essential Extracts', 'price': '159.00', 'original_price': '189.00'}
                        ],
                        'Cluster F: Mass Verification Instruments': [
                            {'name': 'Precision Dosing Kit', 'link': 'bundle-precision-dosing-kit.html', 'description': 'Mass Verification Instrument + Dosing Pods + Preservation Unit', 'price': '89.00', 'original_price': '101.00'},
                            {'name': 'Toker Poker Pro Kit', 'link': 'bundle-toker-poker-pro.html', 'description': 'Thermal Initiator + Mass Verification Instrument + Preservation Unit', 'price': '79.00', 'original_price': '99.00'}
                        ]
                    }.get(category_name, [])
                ])}
            </div>
        </div>
    </main>
    {generate_footer()}
</body>
</html>"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def generate_index_page(products, output_dir):
    """Generate the index page."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pixie's Pantry | Clinical Index</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>{get_styles()}</style>
</head>
<body>
    {generate_header()}
    <main class="max-w-6xl mx-auto px-4 py-12">
        <h1 class="text-4xl font-bold mb-8">Clinical Hardware Index</h1>
        <p class="text-lg text-gray-600 mb-12">
            Medical-grade hardware for botanical administration and extract delivery.
        </p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Clinical Clusters -->
            <a href="cluster-a-active-electronic-teds.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster A: Active Electronic TEDs</h2>
                <p class="text-gray-600 mt-2">Precision-engineered thermal extraction devices.</p>
            </a>
            <a href="cluster-b-passive-manual-teds.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster B: Passive/Manual TEDs</h2>
                <p class="text-gray-600 mt-2">Manual systems requiring external heat sources.</p>
            </a>
            <a href="cluster-c-hydrated-filters.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster C: Hydrated Filters</h2>
                <p class="text-gray-600 mt-2">Water-based filtration for purified aerosol delivery.</p>
            </a>
            <a href="cluster-d-botanical-homogenizers.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster D: Botanical Homogenizers</h2>
                <p class="text-gray-600 mt-2">Tools for preparing loose leaf botanicals.</p>
            </a>
            <a href="cluster-e-atmospheric-preservation-units.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster E: Atmospheric Preservation Units</h2>
                <p class="text-gray-600 mt-2">Containers for optimal botanical/extract storage.</p>
            </a>
            <a href="cluster-f-mass-verification-instruments.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster F: Mass Verification Instruments</h2>
                <p class="text-gray-600 mt-2">Precision tools for dosing and ignition.</p>
            </a>
            <a href="cluster-g-chemical-sterilization-agents.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster G: Chemical Sterilization Agents</h2>
                <p class="text-gray-600 mt-2">Solvents and cleaners for maintaining hygiene.</p>
            </a>
            <a href="cluster-h-induction-heaters.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster H: Induction Heaters</h2>
                <p class="text-gray-600 mt-2">Electronic devices for heating quartz/ceramic elements.</p>
            </a>
            <a href="cluster-i-pressure-regulation-hardware.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster I: Pressure Regulation Hardware</h2>
                <p class="text-gray-600 mt-2">Accessories for controlling airflow and pressure.</p>
            </a>
            <a href="cluster-j-clinical-extract-applicators.html" class="system-card border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
                <h2 class="text-2xl font-bold">Cluster J: Clinical Extract Applicators</h2>
                <p class="text-gray-600 mt-2">Tools for administering purified extracts.</p>
            </a>
            
            <!-- Bundles Section -->
            <div class="system-card border rounded-lg p-6 shadow-sm md:col-span-2 lg:col-span-3">
                <h2 class="text-2xl font-bold">Clinical Bundles</h2>
                <p class="text-gray-600 mt-2">Curated kits for clinical botanical administration.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mt-6">
                    <a href="bundle-wellness-starter-kit.html" class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                        <h3 class="font-semibold">Wellness Starter Kit</h3>
                        <p class="text-gray-600 text-sm">Thermal Extraction Device + Dosing Pods + Homogenizer</p>
                        <p class="font-bold mt-2">$299 <span class="text-sm text-gray-500 line-through">$349</span></p>
                    </a>
                    <a href="bundle-clinical-extract-bundle.html" class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                        <h3 class="font-semibold">Clinical Extract Bundle</h3>
                        <p class="text-gray-600 text-sm">Concentrate Console + Extracts + Sterilization Agent</p>
                        <p class="font-bold mt-2">$249 <span class="text-sm text-gray-500 line-through">$311</span></p>
                    </a>
                    <a href="bundle-hydrated-filtration-system.html" class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                        <h3 class="font-semibold">Hydrated Filtration System</h3>
                        <p class="text-gray-600 text-sm">Hydro-Filtration Vessel + Downstem + Percolator</p>
                        <p class="font-bold mt-2">$129 <span class="text-sm text-gray-500 line-through">$143</span></p>
                    </a>
                    <a href="bundle-precision-dosing-kit.html" class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                        <h3 class="font-semibold">Precision Dosing Kit</h3>
                        <p class="text-gray-600 text-sm">Mass Verification Instrument + Dosing Pods + Preservation Unit</p>
                        <p class="font-bold mt-2">$89 <span class="text-sm text-gray-500 line-through">$101</span></p>
                    </a>
                    <a href="bundle-thermal-extraction-pro-bundle.html" class="border rounded-lg p-4 hover:shadow-md transition-shadow">
                        <h3 class="font-semibold">Thermal Extraction Pro Bundle</h3>
                        <p class="text-gray-600 text-sm">Portable TED + Extracts + Sterilization Agent</p>
                        <p class="font-bold mt-2">$279 <span class="text-sm text-gray-500 line-through">$340</span></p>
                    </a>
                </div>
            </div>
        </div>
    </main>
    {generate_footer()}
</body>
</html>"""
    
    with open(os.path.join(output_dir, "index.html"), 'w', encoding='utf-8') as f:
        f.write(html)


def generate_subpage(title, content, output_path):
    """Generate a subpage (e.g., DME standards)."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pixie's Pantry | {title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>{get_styles()}</style>
</head>
<body>
    {generate_header()}
    <main class="max-w-6xl mx-auto px-4 py-12">
        <h1 class="text-4xl font-bold mb-8">{title}</h1>
        <div class="prose prose-lg max-w-none">
            {content}
        </div>
    </main>
    {generate_footer()}
</body>
</html>"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def generate_subpages(output_dir):
    """Generate all subpages (DME standards, etc.)."""
    subpages = [
        {
            "title": "Durable Medical Equipment (DME) Standards",
            "content": """
            <p>Our hardware meets or exceeds DME standards for respiratory devices, ensuring safety and durability.</p>
            <ul>
                <li><strong>Biocompatibility:</strong> All materials are USP Class VI certified.</li>
                <li><strong>Sterilization:</strong> Products withstand repeated cleaning cycles without degradation.</li>
                <li><strong>Airflow:</strong> Validated for consistent performance across use cycles.</li>
            </ul>
            <p>Updated quarterly to reflect new compliance data.</p>
            """,
            "output": "dme-standards.html"
        }
    ]
    
    for subpage in subpages:
        generate_subpage(subpage["title"], subpage["content"], os.path.join(output_dir, subpage["output"]))


def generate_clinical_storefront():
    """Generate the full clinical storefront from Medical_Pivot_Master_Catalog.csv."""
    input_csv = os.path.expanduser("~/Desktop/Medical_Pivot_Master_Catalog.csv")
    output_dir = os.path.expanduser("~/Desktop/Pixies_Vape_Shop")
    
    # Load products
    products = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "name": row.get("Medical Product Name", row.get("Product Name", "")),
                "description": row.get("Medical Description", ""),
                "sku": row.get("SKU", ""),
                "price": row.get("Your Online Price", "0.00"),
                "image_url": row.get("Image URL", ""),
                "category": row.get("Clinical Cluster", "Uncategorized"),
                "seo_tags": row.get("Medical SEO Tags", ""),
                "brand": row.get("Brand", ""),
            })
    
    # Generate category pages
    categories = {
        "Cluster A: Active Electronic TEDs": "Precision-engineered thermal extraction devices for clinical botanical administration.",
        "Cluster B: Passive/Manual TEDs": "Manual thermal extraction systems requiring external heat sources.",
        "Cluster C: Hydrated Filters": "Water-based filtration for purified aerosol delivery.",
        "Cluster D: Botanical Homogenizers": "Tools for preparing loose leaf botanicals and extracts.",
        "Cluster E: Atmospheric Preservation Units": "Containers for optimal botanical/extract storage.",
        "Cluster F: Mass Verification Instruments": "Precision tools for dosing and ignition.",
        "Cluster G: Chemical Sterilization Agents": "Solvents and cleaners for maintaining hygiene.",
        "Cluster H: Induction Heaters": "Electronic devices for heating quartz/ceramic elements.",
        "Cluster I: Pressure Regulation Hardware": "Accessories for controlling airflow and pressure.",
        "Cluster J: Clinical Extract Applicators": "Tools for administering purified extracts.",
    }
    
    for category, description in categories.items():
        # Replace slashes and colons for filenames
        filename = category.lower().replace(':', '').replace('/', '-').replace(' ', '-')
        generate_category_page(products, category, description, os.path.join(output_dir, f"{filename}.html"))
    
    # Generate index page
    generate_index_page(products, output_dir)
    
    # Generate subpages (DME standards, etc.)
    generate_subpages(output_dir)
    
    print(f"✅ Clinical storefront generated in {output_dir}")


if __name__ == "__main__":
    generate_clinical_storefront()