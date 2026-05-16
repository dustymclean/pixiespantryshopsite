# Product Description Guidelines: Front-End vs. Back-End

## **Objective**
Reframe product descriptions to:
1. **Front-End (Customer-Facing)**: Use benefit-driven, lifestyle-focused language.
2. **Back-End (Internal/Compliance)**: Retain clinical and compliance details for DME eligibility.

---

## **1. Front-End (Customer-Facing) Language**
### **Core Principles**
- **Avoid**: Clinical terms, HCPCS codes, compliance jargon.
- **Use**: Benefit-driven, lifestyle-focused, and material-excellence language.
- **Tone**: Premium, effortless, high-performance.

### **Terminology Mappings**
| **Avoid**                          | **Use Instead**                                      | **Example**                                                                 |
|------------------------------------|------------------------------------------------------|-----------------------------------------------------------------------------|
| Clinical terms (e.g., "HPF")     | Benefit-driven language             | "Advanced filtration for smoother, cleaner sessions."                     |
| HCPCS codes (e.g., "E1399")      | Implied quality                  | "Engineered for precision and reliability."                              |
| "Respiratory harm reduction"      | Lifestyle-focused outcomes        | "Designed for a premium, effortless experience."                         |
| "Medical-grade"                   | Material excellence               | "Ultra-durable, lab-tested materials."                                    |
| "Aseptic administration interface"| Hygiene-focused                  | "Easy-to-clean design for fresh, pure flavor every time."                 |
| "Vape / Vaporizer"               | Filtration/Extraction System      | "Precision extraction system for rich, flavorful sessions."              |
| "Bong / Water Pipe"              | Filtration Device                 | "Premium glass filtration system for smooth, clean sessions."             |
| "Dab Rig"                        | Extraction System                 | "High-performance extraction system for optimal flavor."                  |
| "Hand Pipe / Spoon Pipe"         | Filtration Pipe                   | "Sleek glass filtration pipe for effortless sessions."                    |
| "Chillum"                        | Direct Inhalation Device          | "Minimalist design for rapid, smooth sessions."                           |
| "510 Battery"                    | Power Supply                      | "Precision power supply for consistent performance."                      |

### **Example Transformations**
#### **Before (DME-Compliant)**
- **Product Name**: Pulsar CORE 10” Hydrated Particulate Filter
- **SEO Title**: Hydrated Particulate Filter | Medical-Grade Aerosol Filtration
- **Meta Description**: Medical-grade Hydrated Particulate Filter (HPF) for respiratory harm reduction. Inert Borosilicate 3.3 construction (SDS Section 11) with 45° aseptic administration interface (HCPCS E1399).

#### **After (Customer-Facing)**
- **Product Name**: Pulsar CORE 10” Premium Filtration System
- **SEO Title**: Premium Glass Filtration System | Smooth, Clean Sessions
- **Meta Description**: Experience unmatched smoothness with our premium glass filtration system. Lab-tested borosilicate construction ensures durability and pure flavor. Perfect for effortless, high-performance sessions.
- **Search Tags**: glass filtration, smooth hits, premium glass, durable, easy to clean, high-performance

---

## **2. Back-End (Internal/Compliance) Language**
### **Where to Hide Clinical Details**
| **Component**               | **Purpose**                                                                 | **Example**                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **SKU Metadata**            | Internal tracking of compliance data.                                       | `WP974-DME-E1399-ISO10993`                                                  |
| **Google Merchant Feed**    | Insurance/HSA/FSA eligibility.                                              | `<g:custom_label_0>DME</g:custom_label_0>`                                  |
| **Internal Docs**           | Staff training and compliance audits.                                       | `Pixies_Vape_Shop/docs/compliance_mappings.md`                             |
| **Shopify Metafields**      | Backend-only HCPCS codes and SDS references.                                | `metafield.hcpcs_code = "E1399"`                                            |
| **Dashboard Config**        | Auto-sanitize legacy terms for Google Merchant Center.                      | `safe_title = re.sub(r'vape', 'filtration system', title)`                  |

### **Compliance Mappings (Internal Use Only)**
| **SKU**   | **Product Name (Front-End)**          | **HCPCS Code** | **SDS Section** | **Clinical Term (Internal)**          |
|----------|---------------------------------------|---------------|-----------------|---------------------------------------|
| WP974   | Pulsar CORE 10” Premium Filtration    | E1399         | 11              | Hydrated Particulate Filter (HPF)     |
| WP975   | Pulsar CORE 9” Portable Filtration    | A4649         | 11              | Portable Aerosol Delivery Interface   |
| WP976   | Pulsar CORE 6” Precision Extraction   | E1399         | 11              | High-Viscosity Delivery System        |

---

## **3. Implementation Workflow**
### **Step 1: Update Product Descriptions (Front-End)**
- Use the **terminology mappings** to rewrite:
  - **Product Name**
  - **SEO Title**
  - **Meta Description**
  - **Search Tags**

### **Step 2: Store Compliance Data (Back-End)**
- **Shopify Metafields**: Add HCPCS codes, SDS sections, and clinical terms.
- **Internal Docs**: Maintain a compliance mapping file for staff.
- **Google Merchant Feed**: Auto-sanitize legacy terms (no clinical language).

### **Step 3: Validate**
- **Google Merchant Center**: Ensure no clinical terms appear in the XML feed.
- **Shopify Front-End**: Verify benefit-driven language is used.
- **Internal Audit**: Confirm compliance data is only in metafields/docs.

---

## **4. Tools & Automation**
### **CSV Template (Front-End)**
```csv
SKU,Product Name,SEO Title,Meta Description,Search Tags
WP974,Pulsar CORE 10” Premium Filtration System,"Premium Glass Filtration System | Smooth, Clean Sessions","Experience unmatched smoothness with our premium glass filtration system. Lab-tested borosilicate construction ensures durability and pure flavor. Perfect for effortless, high-performance sessions.","glass filtration, smooth hits, premium glass, durable, easy to clean, high-performance"
```

### **Shopify Metafields (Back-End)**
```json
{
  "namespace": "compliance",
  "key": "hcpcs_code",
  "value": "E1399",
  "value_type": "string"
}
```

### **Python Snippet for Google Merchant Feed**
```python
def sanitize_for_merchant(title, description):
    # Replace legacy terms (no clinical references)
    replacements = {
        r'(?i)\bvape(?:s|rs|ing)?\b': 'filtration system',
        r'(?i)\bbong\b': 'filtration device',
        r'(?i)\bdab rig\b': 'extraction system',
        r'(?i)\bwater pipe\b': 'filtration device',
        r'(?i)\bhand pipe\b': 'filtration pipe'
    }
    for old, new in replacements.items():
        title = re.sub(old, new, title)
        description = re.sub(old, new, description)
    return title, description
```