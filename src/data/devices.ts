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
  tier: 1 | 2 | 3;
  teardown: TeardownStep[];
}

export const devices: Device[] = [
  {
    id: 'mighty-plus',
    name: 'Mighty+',
    brand: 'Storz & Bickel',
    image: 'https://picsum.photos/seed/mighty/400/400',
    auditScore: 95,
    metrics: {
      vaporPathPurity: 92,
      thermalStability: 96,
      bioCompatibility: 98,
      sanitization: 94,
      traceability: 100
    },
    specs: {
      materials: ['PEEK Polymer', 'Stainless Steel', 'Ceramic (Coated)', 'Medical Grade Silicone'],
      heatingType: 'Hybrid Convection/Conduction',
      tempRange: '104°F - 410°F',
      battery: 'Internal Dual Li-Ion'
    },
    tier: 1,
    teardown: [
      {
        title: 'Cooling Unit Disassembly',
        description: 'The cooling unit features a long labyrinth path to cool vapor, made of heat-resistant PEEK.',
        material: 'PEEK Polymer',
        auditRelevance: 'Ensures vapor temperature is reduced to safe levels for respiratory comfort.',
        technicalTerm: {
          term: 'PEEK',
          definition: 'Polyether ether ketone; a high-performance engineering thermoplastic used in medical implants.'
        }
      },
      {
        title: 'Ceramic Filling Chamber',
        description: 'The updated Mighty+ features a ceramic-coated chamber for easier cleaning and better flavor purity.',
        material: 'Ceramic Coating',
        auditRelevance: 'Improves sanitization standards and reduces residue buildup.'
      }
    ]
  },
  {
    id: 'venty',
    name: 'Venty',
    brand: 'Storz & Bickel',
    image: 'https://picsum.photos/seed/venty/400/400',
    auditScore: 97,
    metrics: {
      vaporPathPurity: 94,
      thermalStability: 99,
      bioCompatibility: 98,
      sanitization: 92,
      traceability: 100
    },
    specs: {
      materials: ['PEEK Polymer', 'Medical Grade Silicone', 'Stainless Steel'],
      heatingType: 'Convection/Conduction Hybrid',
      tempRange: '104°F - 410°F',
      battery: 'Internal Li-Ion (USB-C Supercharge)'
    },
    tier: 1,
    teardown: [
      {
        title: 'Adjustable Airflow Manifold',
        description: 'The Venty features a unique adjustable airflow dial that allows for precise control over draw resistance.',
        material: 'Medical Grade PEEK',
        auditRelevance: 'Allows for customized respiratory comfort and aerosol density.',
        technicalTerm: {
          term: 'Flow Rate',
          definition: 'The volume of fluid (or air) that passes through a given surface per unit time.'
        }
      },
      {
        title: 'High-Power Heater',
        description: 'A newly designed heater that reaches temperature in record time while maintaining extreme stability.',
        material: 'Stainless Steel / Ceramic',
        auditRelevance: 'Precision Thermoregulation Control (PTC) ensures consistent titration.'
      }
    ]
  },
  {
    id: 'tinymight-2',
    name: 'Tinymight 2',
    brand: 'Tinymight',
    image: 'https://picsum.photos/seed/tinymight/400/400',
    auditScore: 97,
    metrics: {
      vaporPathPurity: 98,
      thermalStability: 95,
      bioCompatibility: 98,
      sanitization: 96,
      traceability: 90
    },
    specs: {
      materials: ['Stainless Steel', 'Quartz Glass', 'American Walnut', 'Aluminum'],
      heatingType: 'Convection (On-Demand)',
      tempRange: '250°F - 460°F',
      battery: 'Replaceable 18650 Li-Ion'
    },
    tier: 2,
    teardown: [
      {
        title: 'Quartz Glass Vapor Path',
        description: 'The vapor travels through a thick quartz glass tube, ensuring zero metallic or plastic taste.',
        material: 'Quartz Glass',
        auditRelevance: 'High thermal resistance and inertness. Superior to standard borosilicate in high-heat zones.',
        technicalTerm: {
          term: 'Quartz Glass',
          definition: 'A type of glass with high thermal shock resistance and chemical purity.'
        }
      },
      {
        title: 'Stainless Steel Heater Housing',
        description: 'The massive convection heater is housed in a precision-machined stainless steel chamber.',
        material: '316L Stainless Steel',
        auditRelevance: 'Ensures structural integrity and prevents oxidation during rapid heating cycles.'
      }
    ]
  },
  {
    id: 'anvil',
    name: 'Anvil',
    brand: 'Vestratto',
    image: 'https://picsum.photos/seed/anvil/400/400',
    auditScore: 98,
    metrics: {
      vaporPathPurity: 100,
      thermalStability: 99,
      bioCompatibility: 100,
      sanitization: 100,
      traceability: 95
    },
    specs: {
      materials: ['Copper', 'Stainless Steel', 'Grade 2 Titanium'],
      heatingType: 'Manual (Copper Core Convection)',
      tempRange: 'Variable (User Controlled)',
      battery: 'None (Battery-Free)'
    },
    tier: 3,
    teardown: [
      {
        title: 'Copper Core Heat Sink',
        description: 'A massive copper core provides unparalleled thermal mass and heat distribution.',
        material: 'Oxygen-Free Copper',
        auditRelevance: 'Ensures total thermal extraction in a single cycle without combustion.',
        technicalTerm: {
          term: 'Thermal Conductivity',
          definition: 'The property of a material to conduct heat.'
        }
      },
      {
        title: 'Titanium Herb Chamber',
        description: 'The herb is held in a medical-grade titanium chamber for maximum purity.',
        material: 'Grade 2 Titanium',
        auditRelevance: 'Bio-inert material ensures no metallic off-gassing.'
      }
    ]
  },
  {
    id: 'tempest',
    name: 'Tempest',
    brand: 'Mad Heaters',
    image: 'https://picsum.photos/seed/tempest/400/400',
    auditScore: 96,
    metrics: {
      vaporPathPurity: 100,
      thermalStability: 92,
      bioCompatibility: 100,
      sanitization: 98,
      traceability: 88
    },
    specs: {
      materials: ['Titanium', 'Zirconia', 'Stainless Steel'],
      heatingType: 'Manual (Ball-Vape Inspired)',
      tempRange: 'Variable (User Controlled)',
      battery: 'None (Battery-Free)'
    },
    tier: 3,
    teardown: [
      {
        title: 'Zirconia Ball Matrix',
        description: 'The heater uses zirconia balls to store and distribute heat evenly.',
        material: 'Zirconia Ceramic',
        auditRelevance: 'Provides massive surface area for convection heating.',
        technicalTerm: {
          term: 'Convection',
          definition: 'Heat transfer by the movement of fluids or gases.'
        }
      },
      {
        title: 'Titanium Cooling Spiral',
        description: 'An internal titanium spiral cools the vapor before it reaches the user.',
        material: 'Grade 5 Titanium',
        auditRelevance: 'Ensures respiratory comfort through effective heat exchange.'
      }
    ]
  },
  {
    id: 'terp-hammer',
    name: 'Terp Hammer',
    brand: 'Old Head',
    image: 'https://picsum.photos/seed/terphammer/400/400',
    auditScore: 95,
    metrics: {
      vaporPathPurity: 98,
      thermalStability: 94,
      bioCompatibility: 96,
      sanitization: 92,
      traceability: 85
    },
    specs: {
      materials: ['Stainless Steel', 'Wood', 'Ceramic'],
      heatingType: 'Wireless Convection',
      tempRange: '400°F - 800°F (Base Station)',
      battery: 'Internal Li-Ion (Wireless Charging)'
    },
    tier: 2,
    teardown: [
      {
        title: 'Wireless Induction Interface',
        description: 'The device is heated wirelessly via an induction base station.',
        material: 'Stainless Steel / Ceramic',
        auditRelevance: 'Eliminates cords and potential electrical interference in the vapor path.',
        technicalTerm: {
          term: 'Induction Heating',
          definition: 'The process of heating an electrically conducting object by electromagnetic induction.'
        }
      },
      {
        title: 'Open-Air Convection Path',
        description: 'The air path is completely open, allowing for massive airflow and rapid cooling.',
        material: '316L Stainless Steel',
        auditRelevance: 'Ensures clean, un-obstructed aerosol delivery.'
      }
    ]
  },
  {
    id: 'volcano-hybrid',
    name: 'Volcano Hybrid',
    brand: 'Storz & Bickel',
    image: 'https://picsum.photos/seed/volcano/400/400',
    auditScore: 98,
    metrics: {
      vaporPathPurity: 99,
      thermalStability: 99,
      bioCompatibility: 98,
      sanitization: 96,
      traceability: 100
    },
    specs: {
      materials: ['Stainless Steel', 'PEEK Polymer', 'Medical Grade Silicone', 'Borosilicate Glass'],
      heatingType: 'Convection',
      tempRange: '104°F - 446°F',
      battery: 'Mains Powered (AC)'
    },
    tier: 1,
    teardown: [
      {
        title: 'Medical-Grade Air Pump',
        description: 'The internal diaphragm pump is built to medical standards, ensuring a constant, filtered air stream for balloon inflation.',
        material: 'High-Performance Elastomers',
        auditRelevance: 'ISO 13485 compliance ensures the air source is free from mechanical lubricants or particulate shedding.',
        technicalTerm: {
          term: 'ISO 13485',
          definition: 'An international standard that outlines the requirements for a quality management system specific to the medical devices industry.'
        }
      },
      {
        title: 'Stainless Steel Heat Exchanger',
        description: 'A massive aluminum heat exchanger is encapsulated in stainless steel to prevent metallic leaching while maintaining extreme thermal mass.',
        material: '316L Stainless Steel',
        auditRelevance: 'Ensures the air is heated to precise temperatures without contact with heating elements or electronics.',
        technicalTerm: {
          term: 'Thermal Mass',
          definition: 'The ability of a material to absorb and store heat energy.'
        }
      },
      {
        title: 'Valve & Balloon System',
        description: 'The Easy Valve system uses medical-grade PET balloons and heat-resistant plastics for aerosol storage.',
        material: 'Medical Grade PET / PEEK',
        auditRelevance: 'Allows for titrated dosage delivery and aerosol cooling before inhalation.',
        safetyWarning: 'Balloons should be replaced regularly to prevent bio-film accumulation.'
      }
    ]
  },
  {
    id: 'arizer-solo-3',
    name: 'Solo 3',
    brand: 'Arizer',
    image: 'https://picsum.photos/seed/solo3/400/400',
    auditScore: 96,
    metrics: {
      vaporPathPurity: 100,
      thermalStability: 94,
      bioCompatibility: 98,
      sanitization: 98,
      traceability: 92
    },
    specs: {
      materials: ['Borosilicate Glass', 'Stainless Steel', 'Ceramic', 'Aluminum'],
      heatingType: 'Hybrid (Convection/Conduction)',
      tempRange: '122°F - 428°F',
      battery: 'Internal Li-Ion (High Capacity)'
    },
    tier: 1,
    teardown: [
      {
        title: 'All-Glass Vapor Path',
        description: 'The vapor travels exclusively through a borosilicate glass aroma tube, from the herb chamber to the mouthpiece.',
        material: 'Borosilicate Glass 3.3',
        auditRelevance: 'Total Thermal Isolation (TTI). Zero contact with plastics, metals, or electronics in the vapor path.',
        technicalTerm: {
          term: 'Leachate',
          definition: 'Chemicals that migrate from a material into a liquid or gas, potentially causing contamination.'
        }
      },
      {
        title: 'Ceramic Heating Element',
        description: 'A high-purity ceramic heater provides rapid, stable heat without the risk of oxidation found in metal coils.',
        material: 'Alumina Ceramic',
        auditRelevance: 'Bio-inert heating interface ensures no metallic off-gassing at operational temperatures.'
      },
      {
        title: 'Isolated Airpath',
        description: 'The intake air is physically separated from the internal electronics and battery compartment.',
        material: 'Stainless Steel / Glass',
        auditRelevance: 'Prevents inhalation of VOCs from circuit boards or battery components.',
        technicalTerm: {
          term: 'VOCs',
          definition: 'Volatile Organic Compounds; organic chemicals that have a high vapor pressure at ordinary room temperature.'
        }
      }
    ]
  },
  {
    id: 'puffco-peak-pro-v2',
    name: 'Peak Pro (V2)',
    brand: 'Puffco',
    image: 'https://picsum.photos/seed/peakpro/400/400',
    auditScore: 94,
    metrics: {
      vaporPathPurity: 92,
      thermalStability: 98,
      bioCompatibility: 95,
      sanitization: 90,
      traceability: 94
    },
    specs: {
      materials: ['Ceramic', 'Borosilicate Glass', 'Silicone', 'Aluminum'],
      heatingType: 'Conduction (3D Chamber)',
      tempRange: '400°F - 644°F',
      battery: 'Internal Li-Ion (USB-C)'
    },
    tier: 2,
    teardown: [
      {
        title: '3D Heating Chamber',
        description: 'The 3D chamber heats from the side walls, not just the bottom, preventing oil from pooling and burning.',
        material: 'Ceramic / Gold-Plated Contacts',
        auditRelevance: 'Precision Thermoregulation Control (PTC) via embedded sensors in the chamber walls.',
        technicalTerm: {
          term: 'PID Loop',
          definition: 'A control loop mechanism that uses feedback to maintain a set temperature with high precision.'
        }
      },
      {
        title: 'Water Filtration Manifold',
        description: 'The glass attachment provides hydrated particulate filtration, cooling the aerosol and removing heavy particles.',
        material: 'Hand-Blown Borosilicate Glass',
        auditRelevance: 'Hydrated filtration reduces respiratory irritation and improves aerosol delivery.',
        safetyWarning: 'Ensure water level is below the intake hole to prevent damage to the base electronics.'
      },
      {
        title: 'Oculus Carb Cap',
        description: 'A press-fit silicone and glass cap that creates a directional air stream within the chamber.',
        material: 'USP Class VI Silicone',
        auditRelevance: 'Medical-grade silicone ensures no off-gassing in the high-heat zone.',
        technicalTerm: {
          term: 'USP Class VI',
          definition: 'One of the most stringent testing protocols for medical-grade plastics and polymers.'
        }
      }
    ]
  },
  {
    id: 'dynavap-m-plus',
    name: 'The "M" Plus',
    brand: 'DynaVap',
    image: 'https://picsum.photos/seed/dynavap/400/400',
    auditScore: 92,
    metrics: {
      vaporPathPurity: 100,
      thermalStability: 85,
      bioCompatibility: 100,
      sanitization: 100,
      traceability: 90
    },
    specs: {
      materials: ['Medical Grade Stainless Steel'],
      heatingType: 'Manual (External Heat Source)',
      tempRange: 'Variable (User Controlled)',
      battery: 'None (Battery-Free)'
    },
    tier: 3,
    teardown: [
      {
        title: 'Single-Piece Construction',
        description: 'The device is constructed from 100% medical-grade stainless steel, with no electronics or batteries.',
        material: '316L Stainless Steel',
        auditRelevance: 'Zero risk of electronic off-gassing or battery failure. Total material purity.',
        technicalTerm: {
          term: 'Bio-Compatibility',
          definition: 'The quality of not being harmful to living tissue.'
        }
      },
      {
        title: 'Captive Cap Mechanism',
        description: 'A temperature-sensitive bimetal cap clicks when the optimal extraction temperature is reached.',
        material: 'Stainless Steel / Bimetal',
        auditRelevance: 'Provides a mechanical feedback loop for thermal control without sensors.'
      }
    ]
  }
];
