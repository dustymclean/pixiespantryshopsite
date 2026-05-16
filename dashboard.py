#!/usr/bin/env python3
"""
Pixie's Pantry Medical Storefront Dashboard
Features:
- Product management (add/edit/delete)
- Bundle management (create/edit/delete)
- Photo uploader
- Deploy to storefronts
"""

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import csv
import json
import shutil

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.expanduser("~/Desktop/Pixies_Vape_Shop/uploads")

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load data
def load_products():
    with open(os.path.expanduser("~/Desktop/Medical_Pivot_Master_Catalog.csv"), 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_bundles():
    with open(os.path.expanduser("~/Desktop/Pixies_Vape_Shop/bundles_medical.json"), 'r', encoding='utf-8') as f:
        return json.load(f)['bundles']

# Save data
def save_products(products):
    with open(os.path.expanduser("~/Desktop/Medical_Pivot_Master_Catalog.csv"), 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)

def save_bundles(bundles):
    with open(os.path.expanduser("~/Desktop/Pixies_Vape_Shop/bundles_medical.json"), 'w', encoding='utf-8') as f:
        json.dump({"bundles": bundles}, f, indent=2)

# Routes
@app.route("/")
def dashboard():
    products = load_products()
    bundles = load_bundles()
    return render_template(
        "dashboard.html",
        products=products,
        bundles=bundles,
        clinical_clusters=[
            "Cluster A: Active Electronic TEDs",
            "Cluster B: Passive/Manual TEDs",
            "Cluster C: Hydrated Filters",
            "Cluster D: Botanical Homogenizers",
            "Cluster E: Atmospheric Preservation Units",
            "Cluster F: Mass Verification Instruments",
            "Cluster G: Chemical Sterilization Agents",
            "Cluster H: Induction Heaters",
            "Cluster I: Pressure Regulation Hardware",
            "Cluster J: Clinical Extract Applicators",
        ]
    )


@app.route("/bulk_edit", methods=["GET", "POST"])
def bulk_edit():
    products = load_products()
    
    if request.method == "POST":
        # Apply bulk updates
        updated_count = 0
        for product in products:
            if product['SKU'] in request.form.getlist('selected_skus'):
                if 'price' in request.form:
                    product['Your Online Price'] = request.form['price']
                if 'cluster' in request.form:
                    product['Clinical Cluster'] = request.form['cluster']
                updated_count += 1
        save_products(products)
        return f"✅ Updated {updated_count} products!"
    
    return render_template("bulk_edit.html", products=products)

@app.route("/product/<sku>", methods=["GET", "POST"])
def edit_product(sku):
    products = load_products()
    product = next((p for p in products if p['SKU'] == sku), None)
    
    if request.method == "POST":
        # Update product
        for p in products:
            if p['SKU'] == sku:
                p.update({
                    "Medical Product Name": request.form.get("name"),
                    "Medical Description": request.form.get("description"),
                    "Your Online Price": request.form.get("price"),
                    "Clinical Cluster": request.form.get("cluster"),
                    "Medical SEO Tags": request.form.get("seo_tags"),
                })
                break
        save_products(products)
        return redirect(url_for("dashboard"))
    
    return render_template("edit_product.html", product=product)

@app.route("/product/<sku>/photo", methods=["POST"])
def upload_photo(sku):
    if 'photo' not in request.files:
        return redirect(url_for("edit_product", sku=sku))
    
    file = request.files['photo']
    if file.filename == '':
        return redirect(url_for("edit_product", sku=sku))
    
    # Save photo
    filename = f"product-{sku.lower().replace(' ', '-')}.jpg"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    # Update product image URL
    products = load_products()
    for p in products:
        if p['SKU'] == sku:
            p['Image URL'] = f"/uploads/{filename}"
            break
    save_products(products)
    
    return redirect(url_for("edit_product", sku=sku))

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/bundle/new", methods=["GET", "POST"])
def new_bundle():
    products = load_products()
    
    if request.method == "POST":
        selected_skus = request.form.getlist("selected_products")
        selected_products = [p for p in products if p['SKU'] in selected_skus]
        
        bundles = load_bundles()
        bundles.append({
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "products": [
                {
                    "name": p["Medical Product Name"],
                    "sku": p["SKU"],
                    "category": p["Clinical Cluster"]
                } for p in selected_products
            ],
            "price": float(request.form.get("price")),
            "savings": int(request.form.get("savings")),
            "brands": [request.form.get("brand")]
        })
        save_bundles(bundles)
        return redirect(url_for("dashboard"))
    
    return render_template("new_bundle.html", products=products)

@app.route("/deploy")
def deploy():
    # Regenerate storefront
    os.system("cd ~/Desktop/Pixies_Vape_Shop && python3 generate_clinical_storefront.py && python3 generate_bundle_pages.py && python3 generate_product_pages.py")
    
    # TODO: Add deployment to shop.pixiespantryshop.com and vapes.pixiespantryshop.com
    return "✅ Storefront regenerated! Ready to deploy to shop.pixiespantryshop.com and vapes.pixiespantryshop.com."


@app.route("/bundles")
def bundles():
    bundles = load_bundles()
    return render_template("bundles.html", bundles=bundles)


@app.route("/bundle/<int:index>", methods=["GET", "POST"])
def edit_bundle(index):
    bundles = load_bundles()
    bundle = bundles[index]
    
    if request.method == "POST":
        # Update bundle
        bundles[index].update({
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "price": float(request.form.get("price")),
            "savings": int(request.form.get("savings")),
        })
        save_bundles(bundles)
        return redirect(url_for("bundles"))
    
    return render_template("edit_bundle.html", bundle=bundle)


@app.route("/products")
def products():
    products = load_products()
    return render_template("products.html", products=products)


@app.route("/market_data")
def market_data():
    with open('market_data.json', 'r') as f:
        data = json.load(f)
    return render_template("market_data.html", data=data)

# Templates
@app.route("/templates/<path:filename>")
def template(filename):
    return send_from_directory(os.path.join(app.root_path, "templates"), filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)