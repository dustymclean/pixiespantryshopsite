export interface TeardownStep {
  title: string;
  description: string;
  material: string;
  auditRelevance: string;
  safetyWarning?: string;
  technicalTerm?: {
    term: string;
    definition: string;
  };
}

export interface Device {
  id: string;
  name: string;
  brand: string;
  image: string;
  auditScore: number;
  metrics: {
    vaporPathPurity: number;
    thermalStability: number;
    bioCompatibility: number;
    sanitization: number;
    traceability: number;
  };
  specs: {
    materials: string[];
    heatingType: string;
    tempRange: string;
    battery: string;
  };
  teardown: TeardownStep[];
}

export const devices: Device[] = [
  {
    id: 'tinymight-2',
    name: 'TinyMight 2',
    brand: 'TinyMight',
    image: 'https://picsum.photos/seed/tm2/400/400',
    auditScore: 94,
    metrics: {
      vaporPathPurity: 98,
      thermalStability: 92,
      bioCompatibility: 95,
      sanitization: 90,
      traceability: 96
    },
    specs: {
      materials: ['American Walnut', 'Grade 2 Titanium', 'Borosilicate Glass', 'Stainless Steel'],
      heatingType: 'On-demand Convection',
      tempRange: '250°F - 460°F',
      battery: 'Replaceable 18650'
    },
    teardown: [
      {
        title: 'Outer Chassis Removal',
        description: 'The outer shell is crafted from solid American Walnut, providing natural insulation and a bio-inert exterior.',
        material: 'Solid American Walnut',
        auditRelevance: 'Natural materials reduce the need for synthetic polymers and industrial coatings on the exterior.',
        technicalTerm: {
          term: 'Bio-inert',
          definition: 'A material that does not initiate a response or interact with biological tissue.'
        }
      },
      {
        title: 'Titanium Cylinder Extraction',
        description: 'The heart of the device is a Grade 2 Titanium heating chamber, ensuring rapid heat transfer without metallic off-gassing.',
        material: 'Grade 2 Titanium',
        auditRelevance: 'Meets MGV-1 standards for high-heat zone stability and zero heavy metal leaching.',
        safetyWarning: 'Titanium retains heat significantly; ensure device is fully cooled before handling internal components.'
      },
      {
        title: 'Glass Vapor Path Inspection',
        description: 'The vapor travels through a pure borosilicate glass tube, completely isolated from all electronic components.',
        material: 'Borosilicate Glass 3.3',
        auditRelevance: 'Hermetically isolated airpath ensures zero contact with PCBs or solder.',
        technicalTerm: {
          term: 'Hermetic Isolation',
          definition: 'A complete, airtight seal that prevents any exchange of gases or particles between two environments.'
        }
      },
      {
        title: 'Stainless Steel Cooling Unit',
        description: 'A multi-stage stainless steel cooling unit sits atop the glass path to dissipate heat before inhalation.',
        material: '316L Stainless Steel',
        auditRelevance: 'Medical-grade steel ensures durability and ease of sanitization via ISO immersion.'
      }
    ]
  },
  {
    id: 'venty',
    name: 'Venty',
    brand: 'Storz & Bickel',
    image: 'https://picsum.photos/seed/venty/400/400',
    auditScore: 96,
    metrics: {
      vaporPathPurity: 95,
      thermalStability: 99,
      bioCompatibility: 96,
      sanitization: 94,
      traceability: 98
    },
    specs: {
      materials: ['PEEK Polymer', 'Aluminum (Heatsink)', 'Ceramic (Coated)', 'Medical Grade Silicone'],
      heatingType: 'Hybrid Convection/Conduction',
      tempRange: '104°F - 410°F',
      battery: 'Internal Dual Li-Ion'
    },
    teardown: [
      {
        title: 'Adjustable Airflow Manifold',
        description: 'The top unit features a PEEK polymer manifold with adjustable dial for precise pneumatic control.',
        material: 'PEEK (Polyether ether ketone)',
        auditRelevance: 'High-performance thermoplastic with excellent thermal stability and chemical resistance.',
        technicalTerm: {
          term: 'Pneumatic Control',
          definition: 'The management of pressurized air flow to regulate draw resistance and aerosol density.'
        }
      },
      {
        title: 'Ceramic-Coated Filling Chamber',
        description: 'The filling chamber uses a ceramic coating over aluminum for improved hygiene and non-stick properties.',
        material: 'Ceramic-Coated Aluminum',
        auditRelevance: 'Ceramic interface prevents direct metal-to-botanical contact at high temperatures.',
        safetyWarning: 'Ceramic coatings can chip if cleaned with abrasive tools; use only soft brushes or ISO soaks.'
      },
      {
        title: 'Convection Heater Core',
        description: 'A newly designed high-power heater core capable of reaching temperature in 20 seconds with ±1°F stability.',
        material: 'Medical Grade Alloys',
        auditRelevance: 'Precision Thermoregulation Control (PTC) prevents accidental combustion.'
      }
    ]
  },
  {
    id: 'mighty-plus',
    name: 'Mighty+',
    brand: 'Storz & Bickel',
    image: 'https://picsum.photos/seed/mighty/400/400',
    auditScore: 92,
    metrics: {
      vaporPathPurity: 90,
      thermalStability: 95,
      bioCompatibility: 94,
      sanitization: 92,
      traceability: 98
    },
    specs: {
      materials: ['PEEK Polymer', 'Stainless Steel', 'Ceramic (Coated)', 'Medical Grade Silicone'],
      heatingType: 'Hybrid Convection/Conduction',
      tempRange: '104°F - 410°F',
      battery: 'Internal Dual Li-Ion'
    },
    teardown: [
      {
        title: 'Cooling Unit Disassembly',
        description: 'The cooling unit features a long labyrinth path to cool vapor, made of heat-resistant PEEK.',
        material: 'PEEK Polymer',
        auditRelevance: 'Ensures vapor temperature is reduced to safe levels for respiratory comfort.'
      },
      {
        title: 'Ceramic Filling Chamber',
        description: 'The updated Mighty+ features a ceramic-coated chamber for easier cleaning and better flavor purity.',
        material: 'Ceramic Coating',
        auditRelevance: 'Improves sanitization standards and reduces residue buildup.'
      }
    ]
  }
];
