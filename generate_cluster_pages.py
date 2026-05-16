#!/usr/bin/env python3
"""
Generate cluster pages for Pixie's Pantry storefront.
"""
import pandas as pd
import os

# Load the master catalog
df = pd.read_csv("~/Desktop/Dyspensr_Master_Catalog_Priced.csv")

# Define clusters
clusters = {
    "a": {
        "name": "Active Electronic Systems",
        "description": "Precision-engineered thermal systems with integrated heat control.",
        "filter": lambda row: "Cluster A" in str(row.get("Category", ""))
    },
    "b": {
        "name": "Passive Systems",
        "description": "Manual systems requiring external heat sources.",
        "filter": lambda row: "Cluster B" in str(row.get("Category", ""))
    },
    "c": {
        "name": "Filtration Systems",
        "description": "Water-based systems for cooled aerosol routing.",
        "filter": lambda row: "Cluster C" in str(row.get("Category", ""))
    },
    "d": {
        "name": "Botanical Homogenizers",
        "description": "Tools for consistent botanical particle size.",
        "filter": lambda row: "Cluster D" in str(row.get("Category", ""))
    },
    "e": {
        "name": "Preservation Units",
        "description": "Storage systems for humidity stability.",
        "filter": lambda row: "Cluster E" in str(row.get("Category", ""))
    },
    "f": {
        "name": "Mass Verification Instruments",
        "description": "Precision tools for weighing and dosing.",
        "filter": lambda row: "Cluster F" in str(row.get("Category", ""))
    },
    "g": {
        "name": "Filtration Accessories",
        "description": "Downstems, percolators, and ash catchers.",
        "filter": lambda row: "Cluster G" in str(row.get("Category", ""))
    },
    "h": {
        "name": "Cleaning Systems",
        "description": "Brushes, solutions, and maintenance tools.",
        "filter": lambda row: "Cluster H" in str(row.get("Category", ""))
    },
    "i": {
        "name": "Ignition Sources",
        "description": "Lighters, hemp wick, and torches.",
        "filter": lambda row: "Cluster I" in str(row.get("Category", ""))
    },
    "j": {
        "name": "Apparel & Education",
        "description": "T-shirts, guides, and rolling trays.",
        "filter": lambda row: "Cluster J" in str(row.get("Category", ""))
    }
}

# Generate cluster pages
for cluster_id, cluster in clusters.items():
    cluster_products = df[df.apply(cluster["filter"], axis=1)]
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cluster {cluster_id.upper()} - {cluster['name']} | Pixie's Pantry</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="topbar">
        <div class="wrap nav">
            <a class="brand" href="index.html">Pixie's Pantry<small>{cluster['name']}</small></a>
            <nav class="links">
                <a href="shop.html">Shop</a>
                <a href="bundles.html">Bundles</a>
                <a href="compliance.html">Compliance</a>
            </nav>
        </div>
    </header>
    
    <main>
        <section class="hero">
            <div class="wrap">
                <h1>Cluster {cluster_id.upper()}: {cluster['name']}</h1>
                <p>{cluster['description']}</p>
            </div>
        </section>
        
        <section class="section">
            <div class="wrap">
                <div class="product-grid">
    """
    
    # Add products
    for _, row in cluster_products.iterrows():
        if row["Status"] != "Active":
            continue
        
        html += f"""
                    <div class="product-card">
                        <img src="{row['Image URL']}" alt="{row['Clean Product Name']}">
                        <div class="product-info">
                            <h3>{row['Clean Product Name']}</h3>
                            <div class="price">${row['Your Online Price']}</div>
                        </div>
                    </div>
        """
    
    html += """
                </div>
            </div>
        </section>
    </main>
    
    <footer class="footer">
        <div class="wrap">
            <p>&copy; 2026 Pixie's Pantry. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
    """
    
    # Save the file
    with open(f"cluster-{cluster_id}.html", "w") as f:
        f.write(html)
    print(f"✓ Generated cluster-{cluster_id}.html")