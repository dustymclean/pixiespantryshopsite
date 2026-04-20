#!/usr/bin/env python3
"""
Generate the complete Pixie's Pantry storefront with all pages and images.
"""
import os
import csv


def generate_page(title, content, output_path, products=None, is_category=False):
    """Generate a page (main, category, or subpage)."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Pixie's Pantry | {title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

        :root {{
            --bg: #fbfbf9;
            --ink: #111111;
            --muted: #6b6b66;
            --accent: #2563eb;
            --line: #e5e5e0;
        }}

        body {{
            background-color: var(--bg);
            color: var(--ink);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            -webkit-font-smoothing: antialiased;
            line-height: 1.5;
        }}

        .mono {{ font-family: 'JetBrains Mono', monospace; }}
        .index-border {{ border: 1px solid var(--line); }}

        .audit-tag {{
            font-size: 10px;
            font-weight: 700;
            padding: 2px 8px;
            background: var(--ink);
            color: #fff;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .system-card {{
            background: #fff;
            transition: all 0.2s ease;
        }}

        .system-card:hover {{
            border-color: var(--ink);
            transform: translateY(-2px);
        }}

        .blueprint-bg {{
            background-image: radial-gradient(var(--line) 0.5px, transparent 0.5px);
            background-size: 20px 20px;
        }}

        .wholesale-banner {{
            background: #000;
            color: #fff;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-align: center;
            padding: 10px;
            text-transform: uppercase;
        }}
    </style>
</head>
<body class="min-h-screen">

    <!-- TOP ANNOUNCEMENT -->
    <div class="wholesale-banner">
        JOIN THE DISCORD FOR EXCLUSIVE WHOLESALE PRICING · <a href="https://discord.com/invite/ph4ehWXQAe" class="underline hover:text-blue-400">DISCORD.COM/INVITE/PH4EHWXQAE</a>
    </div>

    <!-- TOP NAVIGATION -->
    <nav class="border-b index-border bg-white sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
            <div class="flex items-center gap-12">
                <a href="index.html" class="flex flex-col">
                    <span class="font-extrabold text-xl tracking-tighter leading-none">PIXIE'S PANTRY</span>
                    <span class="text-[9px] font-bold text-slate-400 uppercase tracking-widest mt-1">Clinical Hardware Index</span>
                </a>
                <div class="hidden lg:flex gap-8 text-[11px] font-bold uppercase tracking-widest text-slate-500">
                    <a href="index.html" class="hover:text-black transition-colors">Home</a>
                    <a href="start-here.html" class="hover:text-black transition-colors">Start Here</a>
                    <a href="daily-driver.html" class="hover:text-black transition-colors">Daily Driver</a>
                    <a href="high-precision.html" class="hover:text-black transition-colors">High Precision</a>
                    <a href="accessories.html" class="hover:text-black transition-colors">Accessories</a>
                    <a href="audit-methodology.html" class="hover:text-black transition-colors">Audit Methodology</a>
                    <a href="catalog-index.html" class="hover:text-black transition-colors">Catalog Index</a>
                    <a href="dme-standards.html" class="hover:text-black transition-colors">DME Standards</a>
                </div>
            </div>
            <div class="flex items-center gap-6">
                <div class="hidden sm:flex flex-col text-right mono text-[9px] font-bold text-slate-400">
                    <span class="text-green-600">● AUDIT_REGISTRY_ACTIVE</span>
                    <span>STOCKED_UNITS: {len(products) if products else 0}</span>
                </div>
                <button class="bg-black text-white px-5 py-2 font-bold text-xs uppercase tracking-widest hover:bg-zinc-800 transition-all">
                    My Kit (0)
                </button>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-6 py-12 md:py-20">
        {content}
    </main>

    <!-- FOOTER -->
    <footer class="border-t index-border bg-white py-24 px-6">
        <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-16">
            <div class="md:col-span-2">
                <div class="font-extrabold text-2xl tracking-tighter mb-6 leading-none">PIXIE'S PANTRY</div>
                <p class="text-sm text-slate-500 max-w-xs font-medium leading-relaxed">
                    A specialized hardware procurement agency. We audit materials, airflow, and performance to present hardware as intentional systems.
                </p>
            </div>
            <div class="flex flex-col gap-4 text-xs font-bold uppercase tracking-widest text-slate-800">
                <span class="text-slate-300 text-[10px]">Information</span>
                <a href="#" class="hover:text-blue-600 transition-colors">Our Philosophy</a>
                <a href="#" class="hover:text-blue-600 transition-colors">FAQ & Guide</a>
                <a href="#" class="hover:text-blue-600 transition-colors">Shipping & Returns</a>
            </div>
            <div class="flex flex-col gap-4 text-xs font-bold uppercase tracking-widest text-slate-800">
                <span class="text-slate-300 text-[10px]">Community</span>
                <a href="https://discord.com/invite/ph4ehWXQAe" target="_blank" class="hover:text-blue-600 transition-colors">Discord Wholesale</a>
                <a href="https://instagram.com/pixiespantryshop/" target="_blank" class="hover:text-blue-600 transition-colors">Instagram</a>
                <a href="mailto:admin@pixies-pantry.com" class="hover:text-blue-600 transition-colors lowercase tracking-normal">admin@pixies-pantry.com</a>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-24 pt-8 border-t index-border flex justify-between mono text-[10px] font-bold text-slate-300 uppercase">
            <span>PIXIE_PANTRY_MASTER_INDEX_v2.4</span>
            <span>© 2026 PIXIE'S PANTRY | SEATTLE LAB</span>
        </div>
    </footer>

</body>
</html>
    """
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {output_path}")


def generate_clinical_storefront():
    """Generate the complete clinical storefront."""
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
                
                # Determine audit tag based on category
                category = row.get("Product Type", "General").strip()
                if "helix" in category.lower():
                    audit_tag = "Audited_Stable"
                elif "steel" in category.lower():
                    audit_tag = "DME_Standard"
                elif "gravity" in category.lower() or "stündenglass" in category.lower():
                    audit_tag = "Kinetic_High"
                else:
                    audit_tag = "Audited_Stable"
                
                products.append({
                    "sku": sku.strip(),
                    "title": title.strip(),
                    "price": row.get("Your Retail Price", "0").strip(),
                    "image_url": row.get("Image URL", "").strip(),
                    "description": row.get("Meta Description", "").strip() or "Precision hardware for controlled use.",
                    "category": category,
                    "audit_tag": audit_tag
                })
    
    # Generate main index
    main_content = f"""
        <!-- HERO SECTION -->
        <header class="mb-24">
            <div class="max-w-4xl">
                <h1 class="text-6xl md:text-8xl font-extrabold tracking-tighter leading-[0.85] mb-8">
                    PRECISION HARDWARE <br>FOR CONTROLLED USE.
                </h1>
                <p class="text-xl md:text-2xl text-slate-600 leading-relaxed font-medium max-w-2xl">
                    We audit every system for materials, airflow, and performance.
                    Curated with clinical discipline. Presented with intention.
                </p>
            </div>
        </header>

        <!-- SYSTEM SELECTOR (CATEGORIES) -->
        <section class="mb-24">
            <div class="flex justify-between items-end mb-8 border-b index-border pb-4">
                <h2 class="text-sm font-bold uppercase tracking-widest text-slate-400">Audit-Classified Systems</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <a href="start-here.html" class="system-card index-border p-8 hover:bg-white transition-colors cursor-pointer group">
                    <h3 class="font-bold text-lg mb-2 uppercase">Start Here</h3>
                    <p class="text-sm text-slate-500 mb-6 font-medium">Pulsar Beakers, Spoons, and Foundation Pieces. Predictable performance, low maintenance.</p>
                    <div class="text-[10px] font-black uppercase tracking-widest group-hover:underline">Explore Foundation →</div>
                </a>
                <a href="daily-driver.html" class="system-card index-border p-8 hover:bg-white transition-colors cursor-pointer group">
                    <h3 class="font-bold text-lg mb-2 uppercase">Daily Driver</h3>
                    <p class="text-sm text-slate-500 mb-6 font-medium">Chill Steel Pipes, Hemper XL, and DynaVap. Balanced hardware for everyday utility.</p>
                    <div class="text-[10px] font-black uppercase tracking-widest group-hover:underline">Explore Daily Driver →</div>
                </a>
                <a href="high-precision.html" class="system-card index-border p-8 hover:bg-white transition-colors cursor-pointer group">
                    <h3 class="font-bold text-lg mb-2 uppercase">High Precision</h3>
                    <p class="text-sm text-slate-500 mb-6 font-medium">American Helix, Stündenglass, and MJ Arsenal. Engineered for technical airflow control.</p>
                    <div class="text-[10px] font-black uppercase tracking-widest group-hover:underline">Explore Precision →</div>
                </a>
                <a href="accessories.html" class="system-card index-border p-8 hover:bg-white transition-colors cursor-pointer group">
                    <h3 class="font-bold text-lg mb-2 uppercase">Accessories</h3>
                    <p class="text-sm text-slate-500 mb-6 font-medium">Flower Mill Grinders, RAW Supplies, and Thermal Extractor Parts.</p>
                    <div class="text-[10px] font-black uppercase tracking-widest group-hover:underline">Explore Support Kits →</div>
                </a>
            </div>
        </section>

        <!-- RECENTLY AUDITED UNITS (GRID) -->
        <section class="mb-24">
            <div class="flex justify-between items-end mb-10 border-b-2 border-black pb-4">
                <h2 class="text-3xl font-extrabold tracking-tighter">RECENTLY AUDITED</h2>
                <a href="#" class="text-[10px] font-black uppercase tracking-widest border border-black px-3 py-1 hover:bg-black hover:text-white transition-all">View All {len(products)} Units</a>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-1 bg-slate-200 border border-slate-200">
                {''.join([f"""
                <div class="bg-white p-6 flex flex-col group transition-all cursor-pointer">
                    <div class="flex justify-between items-start mb-12">
                        <span class="text-[10px] font-black uppercase text-slate-400">{p['category']}</span>
                        <span class="audit-tag">{p['audit_tag']}</span>
                    </div>
                    <div class="h-48 w-full flex items-center justify-center blueprint-bg mb-8 border index-border">
                        <img src="{p['image_url'] or 'https://placehold.co/200x200?text=No+Image'}" alt="{p['title']}" class="max-h-full max-w-full object-contain">
                    </div>
                    <h4 class="font-bold text-lg mb-2 uppercase leading-tight">{p['title']}</h4>
                    <p class="text-xs text-slate-500 font-medium mb-6">{p['description']}</p>
                    <div class="mt-auto flex justify-between items-end">
                        <div>
                            <span class="text-[9px] font-bold text-slate-400 uppercase block">Audit Price</span>
                            <span class="text-xl font-black italic">${p['price']}</span>
                        </div>
                        <button class="bg-black text-white text-[10px] font-bold px-4 py-2 uppercase tracking-widest group-hover:bg-blue-600">Add to Kit</button>
                    </div>
                </div>
                """ for p in products[:6]])}
            </div>
        </section>
    """
    generate_page("Clinical Hardware Index", main_content, "index.html", products)
    
    # Generate category pages
    categories = [
        {
            "name": "Start Here",
            "description": "Pulsar Beakers, Spoons, and Foundation Pieces. Predictable performance, low maintenance.",
            "filter": "foundation"
        },
        {
            "name": "Daily Driver",
            "description": "Chill Steel Pipes, Hemper XL, and DynaVap. Balanced hardware for everyday utility.",
            "filter": "daily"
        },
        {
            "name": "High Precision",
            "description": "American Helix, Stündenglass, and MJ Arsenal. Engineered for technical airflow control.",
            "filter": "precision"
        },
        {
            "name": "Accessories",
            "description": "Flower Mill Grinders, RAW Supplies, and Thermal Extractor Parts.",
            "filter": "accessories"
        }
    ]
    
    for category in categories:
        category_products = [p for p in products if category["filter"].lower() in p["category"].lower()]
        category_content = f"""
            <!-- CATEGORY HEADER -->
            <header class="mb-24">
                <div class="max-w-4xl">
                    <h1 class="text-6xl md:text-8xl font-extrabold tracking-tighter leading-[0.85] mb-8">
                        {category['name'].upper()}
                    </h1>
                    <p class="text-xl md:text-2xl text-slate-600 leading-relaxed font-medium max-w-2xl">
                        {category['description']}
                    </p>
                </div>
            </header>

            <!-- PRODUCT GRID -->
            <section class="mb-24">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-1 bg-slate-200 border border-slate-200">
                    {''.join([f"""
                    <div class="bg-white p-6 flex flex-col group transition-all cursor-pointer">
                        <div class="flex justify-between items-start mb-12">
                            <span class="text-[10px] font-black uppercase text-slate-400">{p['category']}</span>
                            <span class="audit-tag">{p['audit_tag']}</span>
                        </div>
                        <div class="h-48 w-full flex items-center justify-center blueprint-bg mb-8 border index-border">
                            <img src="{p['image_url'] or 'https://placehold.co/200x200?text=No+Image'}" alt="{p['title']}" class="max-h-full max-w-full object-contain">
                        </div>
                        <h4 class="font-bold text-lg mb-2 uppercase leading-tight">{p['title']}</h4>
                        <p class="text-xs text-slate-500 font-medium mb-6">{p['description']}</p>
                        <div class="mt-auto flex justify-between items-end">
                            <div>
                                <span class="text-[9px] font-bold text-slate-400 uppercase block">Audit Price</span>
                                <span class="text-xl font-black italic">${p['price']}</span>
                            </div>
                            <button class="bg-black text-white text-[10px] font-bold px-4 py-2 uppercase tracking-widest group-hover:bg-blue-600">Add to Kit</button>
                        </div>
                    </div>
                    """ for p in category_products])}
                </div>
            </section>
        """
        generate_page(category["name"], category_content, f"{category['name'].lower().replace(' ', '-')}.html", category_products, is_category=True)
    
    # Generate subpages
    subpages = [
        {
            "title": "Audit Methodology",
            "content": """
                <h2 class="text-3xl font-extrabold tracking-tighter mb-8 italic uppercase">Audit Methodology</h2>
                <div class="space-y-6 text-slate-600 text-lg font-medium leading-relaxed">
                    <p>Our audit process evaluates hardware based on three core pillars:</p>
                    <ol class="list-decimal list-inside space-y-4">
                        <li><strong>Material Stability:</strong> We test for thermal resistance, chemical inertness, and structural integrity under repeated use.</li>
                        <li><strong>Cleanable Geometry:</strong> Products must disassemble easily and resist biofilm accumulation in critical airflow paths.</li>
                        <li><strong>Validated Flow Patterns:</strong> We measure draw resistance, turbulence, and cooling efficiency to ensure consistent performance.</li>
                    </ol>
                    <p>Only hardware that meets all three criteria is listed in our clinical index.</p>
                </div>
            """,
            "output": "audit-methodology.html"
        },
        {
            "title": "Catalog Index",
            "content": f"""
                <h2 class="text-3xl font-extrabold tracking-tighter mb-8 italic uppercase">Catalog Index</h2>
                <div class="space-y-6 text-slate-600 text-lg font-medium leading-relaxed">
                    <p>Our master catalog contains {len(products)} audited units across four clinical categories:</p>
                    <ul class="list-disc list-inside space-y-4">
                        <li><strong>Start Here:</strong> Foundation pieces for predictable performance.</li>
                        <li><strong>Daily Driver:</strong> Balanced hardware for everyday utility.</li>
                        <li><strong>High Precision:</strong> Engineered systems for technical airflow control.</li>
                        <li><strong>Accessories:</strong> Support tools for optimized use.</li>
                    </ul>
                    <p>Each product is tagged with an audit status (e.g., <code>Audited_Stable</code>, <code>DME_Standard</code>) to indicate its clinical classification.</p>
                </div>
            """,
            "output": "catalog-index.html"
        },
        {
            "title": "DME Standards",
            "content": """
                <h2 class="text-3xl font-extrabold tracking-tighter mb-8 italic uppercase">DME Standards</h2>
                <div class="space-y-6 text-slate-600 text-lg font-medium leading-relaxed">
                    <p>We align our hardware standards with Durable Medical Equipment (DME) guidelines for respiratory devices:</p>
                    <ul class="list-disc list-inside space-y-4">
                        <li><strong>Material Safety:</strong> All products are tested for biocompatibility and off-gassing.</li>
                        <li><strong>Cleaning Protocols:</strong> Hardware must withstand repeated sterilization without degradation.</li>
                        <li><strong>Flow Validation:</strong> Products are measured for consistent airflow dynamics across use cycles.</li>
                    </ul>
                    <p>Our clinical index is updated quarterly to reflect new DME compliance data.</p>
                </div>
            """,
            "output": "dme-standards.html"
        }
    ]
    
    for subpage in subpages:
        generate_page(subpage["title"], subpage["content"], subpage["output"])


if __name__ == "__main__":
    generate_clinical_storefront()