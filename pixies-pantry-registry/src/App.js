import React, { useMemo, useState } from "react";
import { 
  Search, 
  ShoppingCart, 
  ShieldCheck, 
  Wrench, 
  X, 
  Info,
  MessageSquare,
  ChevronDown,
  ChevronUp,
  FileText,
  Zap,
  Layers,
  Settings,
  Thermometer,
  Droplets,
  Package,
  Activity,
  ArrowRight,
  Grid,
  ClipboardCheck,
  RefreshCw,
  Box,
  // Brand placeholders: Lucide removed brand logos in v1.0
  Camera as Instagram, 
  Play as Youtube
} from "lucide-react";

/**
 * PIXIE'S PANTRY: CLINICAL HARDWARE REGISTRY v2.6.2
 * * AUDITOR NOTES:
 * - Resolved 'Instagram' and 'Youtube' export errors by aliasing generic Lucide icons.
 * - Eliminated all 'unused-vars' warnings (Database, ExternalLink, Filter, Truck, useEffect).
 * - Fixed Line 496 accessibility error (converted empty <a> to <button>).
 * - Component ready for production build.
 */

const STORE_POSITION = "WE ARE NOT A HEADSHOP. WE ARE A PRECISION HARDWARE PROVIDER.";

const clusters = [
  { id: 'A', icon: Zap, title: "Active Electronic Systems", desc: "Precision-engineered thermal extraction devices with integrated heat control." },
  { id: 'B', icon: Thermometer, title: "Passive Systems", desc: "Manual thermal extraction systems requiring external heat sources." },
  { id: 'C', icon: Droplets, title: "Filtration Systems", desc: "Water-based filtration systems for cooled aerosol routing." },
  { id: 'D', icon: Settings, title: "Botanical Homogenizers", desc: "Preparation tools for consistent botanical particle size." },
  { id: 'E', icon: Box, title: "Preservation Units", desc: "Storage systems for humidity stability and material protection." },
  { id: 'F', icon: Activity, title: "Mass Verification Instruments", desc: "Precision tools for weighing, dosing, and repeatable preparation." },
  { id: 'G', icon: Layers, title: "Filtration Accessories", desc: "Downstems, percolators, and ash catchers for enhanced filtration." },
  { id: 'H', icon: Wrench, title: "Interface Hardware", desc: "Adapters, connectors, and seal-integrity components." },
  { id: 'I', icon: RefreshCw, title: "Maintenance & Care", desc: "Clinical cleaning tools and material-path recovery kits." },
  { id: 'J', icon: ShieldCheck, title: "Compliance & Safety", desc: "PPE, lab apparel, and documentation protocols." },
];

const sampleProducts = [
  {
    id: "stripe_price_prism_foundation",
    sku: "PP-C-PRISM-001",
    name: "Prism Foundation Kit",
    cluster: "C",
    category: "Filtration Systems",
    badge: "Base Unit",
    price: 54.00,
    materialPath: "Borosilicate glass / Medical Grade Silicone",
    jointStandard: "14mm Female",
    description: "A foundation-level modular system selected for repeatable assembly, stable component alignment, and clear material-path documentation.",
  },
  {
    id: "stripe_price_halo_connector",
    sku: "PP-H-HALO-002",
    name: "Halo Connector Set",
    cluster: "H",
    category: "Interface Hardware",
    badge: "Control Point",
    price: 32.00,
    materialPath: "316 Stainless Steel / Glass",
    jointStandard: "14mm Male-to-Male",
    description: "A connector set selected for controlled fitment, seal integrity, and modular expansion.",
  },
  {
    id: "stripe_price_homogenizer",
    sku: "PP-D-HOMO-003",
    name: "Precision Botanical Mill",
    cluster: "D",
    category: "Homogenizers",
    badge: "Registry Grade",
    price: 85.00,
    materialPath: "Anodized Aluminum / Tool Steel",
    jointStandard: "Internal Threading",
    description: "Engineered for consistent particle size distribution to ensure repeatable thermal extraction.",
  },
  {
    id: "stripe_price_starter_bundle",
    sku: "PP-BNDL-HYDRATED-001",
    name: "Hydrated Filtration Starter System",
    cluster: "C",
    category: "Prebuilt Bundle",
    badge: "Compatibility Guaranteed",
    price: 129.00,
    msrp_was: 143.00,
    materialPath: "Borosilicate & Clinical Silicone",
    jointStandard: "System-Locked",
    description: "Compatibility-checked hydrated system with foundation, connector, and maintenance support.",
  }
];

function money(value) {
  return `$${Number(value || 0).toFixed(2)}`;
}

function ProductCard({ product, onAdd, onInspect, isSelected }) {
  const isBundle = product.msrp_was !== undefined;

  return (
    <article className={`flex h-full flex-col border transition-all duration-300 bg-white ${isSelected ? 'border-black ring-1 ring-black shadow-xl' : 'border-black/10 hover:border-black/30 shadow-sm'}`}>
      <button
        type="button"
        onClick={() => onInspect(isSelected ? null : product)}
        className="group relative flex aspect-square items-center justify-center bg-[#ebe6dc] p-6 text-center text-[10px] uppercase tracking-[0.35em] text-black/35 overflow-hidden"
      >
        <span className="relative z-10">{isBundle ? "Registry Bundle Asset" : "Product SKU Asset"}</span>
        <div className="absolute inset-0 bg-black/5 opacity-0 transition-opacity group-hover:opacity-100" />
      </button>
      
      <div className="flex flex-1 flex-col p-5">
        <div className="mb-4 flex items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <span className="bg-black text-white px-2 py-0.5 text-[8px] font-sans font-black">CLUSTER {product.cluster}</span>
            <p className="text-[9px] uppercase tracking-[0.15em] text-black/45 font-sans font-bold">{product.category}</p>
          </div>
          <span className="border border-black/20 px-2 py-0.5 text-[8px] uppercase tracking-[0.1em] bg-[#fbfaf7]">
            {product.badge}
          </span>
        </div>
        
        <h3 className="text-xl leading-tight font-serif italic mb-1">{product.name}</h3>
        <p className="text-[10px] uppercase tracking-[0.18em] text-black/40 font-mono">SKU {product.sku}</p>
        
        <div className="mt-4 border-t border-black/5 pt-4">
          <button 
            type="button"
            onClick={() => onInspect(isSelected ? null : product)}
            className="flex items-center justify-between w-full text-[9px] uppercase tracking-widest font-sans font-bold text-black/60 hover:text-black transition-colors"
          >
            <span className="flex items-center gap-2">
              <ClipboardCheck size={12} />
              The Audit Details
            </span>
            {isSelected ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
          </button>
          
          {isSelected && (
            <div className="mt-4 space-y-3 animate-in slide-in-from-top-2 duration-300 overflow-hidden">
               <p className="text-[11px] leading-relaxed text-black/60 italic pb-2 border-b border-black/5">
                {product.description}
              </p>
              <div className="space-y-1.5 text-[10px] leading-5 text-black/55 font-sans">
                <div className="flex justify-between border-b border-black/5 pb-1">
                  <span className="font-bold opacity-50 uppercase tracking-tighter">Material Path</span> 
                  <span className="text-right ml-2">{product.materialPath}</span>
                </div>
                <div className="flex justify-between border-b border-black/5 pb-1">
                  <span className="font-bold opacity-50 uppercase tracking-tighter">Interface</span> 
                  <span className="text-right ml-2">{product.jointStandard}</span>
                </div>
                <div className="flex justify-between font-bold text-black pt-1">
                  <span className="uppercase tracking-tighter">Thermal Status</span> 
                  <span className="text-right ml-2 text-green-600">MAPPED</span>
                </div>
              </div>
            </div>
          )}
        </div>
        
        <div className="mt-auto pt-6">
          <div className="mb-4 flex items-end justify-between">
            <div className="flex flex-col">
              <span className="text-[8px] uppercase tracking-widest text-black/40 font-sans font-bold mb-1">Registry MSRP</span>
              <div className="flex items-center gap-2">
                <span className="text-2xl font-serif">{money(product.price)}</span>
                {isBundle && <span className="text-sm text-black/30 line-through font-sans">{money(product.msrp_was)}</span>}
              </div>
            </div>
          </div>
          <button
            type="button"
            onClick={(e) => { e.stopPropagation(); onAdd(product); }}
            className="w-full bg-black px-4 py-4 text-[10px] uppercase tracking-[0.25em] text-white transition hover:bg-black/80 font-sans font-bold"
          >
            {isBundle ? "Initiate Bundle Intake" : "Add to Registry"}
          </button>
        </div>
      </div>
    </article>
  );
}

export default function App() {
  const [view, setView] = useState('landing');
  const [activeCluster, setActiveCluster] = useState('ALL');
  const [cartOpen, setCartOpen] = useState(false);
  const [payloadOpen, setPayloadOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [cart, setCart] = useState([]);

  const filteredProducts = useMemo(() => {
    let list = sampleProducts;
    if (activeCluster !== 'ALL') {
      list = list.filter(p => p.cluster === activeCluster);
    }
    const q = query.trim().toLowerCase();
    if (q) {
      list = list.filter((p) => [p.name, p.sku, p.category].join(" ").toLowerCase().includes(q));
    }
    return list;
  }, [query, activeCluster]);

  const subtotal = useMemo(() => cart.reduce((sum, item) => sum + item.price * item.quantity, 0), [cart]);
  const itemCount = useMemo(() => cart.reduce((sum, item) => sum + item.quantity, 0), [cart]);

  function addToCart(product) {
    setCart((current) => {
      const existing = current.find((item) => item.id === product.id);
      if (existing) return current.map((item) => item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item);
      return [...current, { ...product, quantity: 1 }];
    });
    setCartOpen(true);
  }

  function updateQuantity(id, direction) {
    setCart((current) => current.map((item) => item.id === id ? { ...item, quantity: Math.max(0, item.quantity + direction) } : item).filter((item) => item.quantity > 0));
  }

  const navigateToRegistry = (cluster = 'ALL') => {
    setActiveCluster(cluster);
    setView('registry');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-[#f7f4ef] text-[#111111] font-serif selection:bg-black selection:text-white">
      <header className="sticky top-0 z-40 border-b border-black bg-[#f7f4ef]/95 backdrop-blur-md">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-5 py-3 md:px-8">
          <div className="flex items-center gap-10">
            <div className="cursor-pointer group" onClick={() => setView('landing')}>
              <p className="text-[8px] uppercase tracking-[0.4em] text-black font-sans font-bold leading-none mb-1">Hardware Audit Layer</p>
              <h1 className="text-xl tracking-[0.05em] md:text-2xl font-serif font-black">PIXIE'S PANTRY</h1>
            </div>
            <nav className="hidden lg:flex gap-6 text-[9px] uppercase tracking-[0.2em] font-sans font-bold text-black/50">
              <button type="button" onClick={() => navigateToRegistry()} className={`hover:text-black transition-colors ${view === 'registry' ? 'text-black underline underline-offset-4' : ''}`}>Registry Index</button>
              <button type="button" className="hover:text-black transition-colors">Prebuilt Systems</button>
              <button type="button" className="hover:text-black transition-colors">The Audit</button>
              <button type="button" className="hover:text-black transition-colors">Standards</button>
              <button type="button" className="hover:text-black transition-colors">Support</button>
            </nav>
          </div>
          <div className="flex gap-2">
            <button type="button" onClick={() => setPayloadOpen(true)} className="hidden md:flex h-10 items-center px-4 border border-black/20 text-[9px] uppercase font-sans font-bold tracking-widest hover:bg-black hover:text-white transition-all">
              Audit Payload
            </button>
            <button type="button" onClick={() => setCartOpen(true)} className="flex h-10 items-center gap-3 bg-black px-5 text-[9px] uppercase font-sans font-bold tracking-widest text-white hover:bg-black/80 transition-all">
              <ShoppingCart size={14} /> Checkout ({itemCount})
            </button>
          </div>
        </div>
      </header>

      {view === 'landing' ? (
        <main className="animate-in fade-in duration-700">
          <section className="mx-auto grid max-w-7xl items-center gap-16 px-5 py-16 md:grid-cols-[1.2fr_0.8fr] md:px-8 md:py-28">
            <div className="space-y-10">
              <div className="space-y-4">
                 <p className="text-[10px] uppercase tracking-[0.4em] text-black/50 font-sans font-bold">CLINICAL HARDWARE REGISTRY</p>
                 <h2 className="text-5xl leading-[0.85] tracking-tighter md:text-8xl italic">
                  Clinical hardware for <span className="text-black/30">botanical administration.</span>
                </h2>
              </div>
              <p className="max-w-xl text-xl leading-relaxed text-black/70 border-l-8 border-black pl-8 italic">
                Engineered systems. Verified materials. No guesswork. Pixie’s Pantry organizes hardware by function, compatibility, cleaning access, and complete-system logic.
              </p>
              <div className="flex flex-wrap gap-4 pt-4">
                <button type="button" onClick={() => navigateToRegistry()} className="bg-black text-white px-8 py-5 text-[10px] uppercase tracking-[0.3em] font-sans font-bold hover:shadow-2xl transition-all flex items-center gap-3 group">
                  Enter Hardware Registry <ArrowRight size={16} className="group-hover:translate-x-1 transition-transform" />
                </button>
                <button type="button" onClick={() => navigateToRegistry('C')} className="border-2 border-black px-8 py-5 text-[10px] uppercase tracking-[0.3em] font-sans font-bold hover:bg-black hover:text-white transition-all">
                  Shop Prebuilt Systems
                </button>
              </div>
            </div>
            <div className="bg-white border-2 border-black p-10 shadow-2xl space-y-8 relative">
              <div className="absolute top-0 right-0 bg-black text-white px-4 py-2 text-[9px] font-sans font-bold tracking-widest">AUDITOR NOTE</div>
              <h3 className="text-2xl italic font-serif">Every page has one job.</h3>
              <div className="space-y-6 font-sans font-bold text-[10px] uppercase tracking-[0.3em]">
                <div className="flex justify-between border-b border-black/10 pb-4 text-green-700">
                  <span className="text-black/40">Material pathway</span>
                  <span className="flex items-center gap-2"><ShieldCheck size={12} /> Reviewed</span>
                </div>
                <div className="flex justify-between border-b border-black/10 pb-4 text-green-700">
                  <span className="text-black/40">Thermal behavior</span>
                  <span className="flex items-center gap-2"><Zap size={12} /> Mapped</span>
                </div>
                <div className="flex justify-between border-b border-black/10 pb-4">
                  <span className="text-black/40">Cleaning access</span>
                  <span className="text-black italic">Required Access</span>
                </div>
                <div className="flex justify-between text-blue-800">
                  <span className="text-black/40">Compatibility</span>
                  <span className="flex items-center gap-2">Enforced Logic</span>
                </div>
              </div>
              <div className="pt-6 border-t border-black/5 italic text-xs text-black/50 leading-relaxed font-sans font-bold uppercase tracking-tight">
                {STORE_POSITION}
              </div>
            </div>
          </section>

          <section className="bg-black text-white py-24">
            <div className="mx-auto max-w-7xl px-5 md:px-8">
              <div className="mb-16 space-y-4">
                <p className="text-[10px] uppercase tracking-[0.4em] font-sans font-bold opacity-40">Choose your path.</p>
                <h2 className="text-4xl md:text-6xl italic font-serif leading-tight max-w-4xl">The storefront is organized around decisions, not clutter.</h2>
              </div>
              <div className="grid gap-8 md:grid-cols-3">
                {[
                  { title: "Browse Hardware", desc: "Products organized by clinical hardware cluster and system role.", icon: Package, action: () => navigateToRegistry() },
                  { title: "Build a System", desc: "Compatibility-checked bundles that remove guesswork.", icon: Wrench, action: () => navigateToRegistry() },
                  { title: "Learn the Standards", desc: "The audit framework behind every product and page.", icon: FileText, action: () => {} }
                ].map((path, i) => (
                  <div key={i} onClick={path.action} className="border border-white/10 p-10 hover:border-white/40 transition-all group cursor-pointer bg-white/5">
                    <path.icon className="mb-8 text-white/20 group-hover:text-white transition-colors" size={32} />
                    <h3 className="text-2xl font-serif italic mb-4">{path.title}</h3>
                    <p className="text-sm leading-relaxed text-white/50">{path.desc}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>

          <section className="mx-auto max-w-7xl px-5 py-24 md:px-8">
            <div className="mb-16 space-y-4">
              <p className="text-[10px] uppercase tracking-[0.4em] text-black font-sans font-bold">Registry Index.</p>
              <h2 className="text-4xl md:text-6xl italic">Ten operating clusters for a scalable catalog.</h2>
            </div>
            <div className="grid gap-px bg-black/10 border border-black/10 md:grid-cols-2 lg:grid-cols-3">
              {clusters.map((cluster) => (
                <div key={cluster.id} onClick={() => navigateToRegistry(cluster.id)} className="bg-[#f7f4ef] p-10 hover:bg-white transition-colors cursor-pointer group">
                  <div className="flex items-center gap-4 mb-6">
                    <div className="h-10 w-10 flex items-center justify-center bg-black text-white text-[10px] font-sans font-bold group-hover:scale-110 transition-transform">{cluster.id}</div>
                    <cluster.icon size={20} className="text-black/30 group-hover:text-black transition-colors" />
                  </div>
                  <h4 className="text-xl font-serif italic mb-3">{cluster.title}</h4>
                  <p className="text-sm leading-relaxed text-black/50 group-hover:text-black/70 transition-colors">{cluster.desc}</p>
                </div>
              ))}
              <div onClick={() => navigateToRegistry()} className="bg-black text-white p-10 flex flex-col justify-between items-start group cursor-pointer transition-colors hover:bg-black/90">
                <h4 className="text-2xl italic font-serif">Enter Full Registry Index</h4>
                <ArrowRight size={32} className="group-hover:translate-x-2 transition-transform" />
              </div>
            </div>
          </section>
        </main>
      ) : (
        <main className="animate-in slide-in-from-bottom-4 duration-500">
          <div className="bg-black text-white py-12">
            <div className="mx-auto max-w-7xl px-5 md:px-8">
              <div className="flex flex-col md:flex-row justify-between items-end gap-8">
                <div className="space-y-4">
                  <button type="button" onClick={() => setView('landing')} className="text-[9px] uppercase tracking-widest font-sans font-bold text-white/40 hover:text-white flex items-center gap-2 mb-2">
                    <X size={12} /> Back to Landing
                  </button>
                  <h2 className="text-4xl md:text-6xl italic font-serif">Registry Archive</h2>
                  <p className="text-sm text-white/50 max-w-xl italic">Currently auditing Cluster {activeCluster === 'ALL' ? 'Indices' : activeCluster}. All hardware listed is verified for material path integrity.</p>
                </div>
                <div className="relative w-full max-w-md">
                  <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-white/30" size={18} />
                  <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Filter registry by SKU..." className="w-full border border-white/20 bg-white/5 px-12 py-4 text-sm outline-none font-sans text-white focus:border-white transition-colors" />
                </div>
              </div>
            </div>
          </div>

          <div className="mx-auto max-w-7xl px-5 py-8 md:px-8 grid md:grid-cols-[280px_1fr] gap-12">
            <aside className="space-y-10 sticky top-28 h-fit hidden md:block">
              <div>
                <h5 className="text-[10px] uppercase tracking-[0.4em] font-sans font-bold border-b border-black/10 pb-4 mb-6 text-black/40">Operating Clusters</h5>
                <ul className="space-y-1">
                  <li onClick={() => setActiveCluster('ALL')} className={`p-3 text-[10px] font-sans font-bold uppercase tracking-widest cursor-pointer transition-colors ${activeCluster === 'ALL' ? 'bg-black text-white' : 'hover:bg-black/5'}`}>All Systems</li>
                  {clusters.map(c => (
                    <li key={c.id} onClick={() => setActiveCluster(c.id)} className={`p-3 text-[10px] font-sans font-bold uppercase tracking-widest cursor-pointer transition-colors flex items-center gap-3 ${activeCluster === c.id ? 'bg-black text-white' : 'hover:bg-black/5'}`}>
                      <span className="opacity-40">{c.id}</span>{c.title}
                    </li>
                  ))}
                </ul>
              </div>
              <div className="p-6 bg-black text-white space-y-4">
                <Info size={24} className="text-white/30" />
                <h6 className="text-lg font-serif italic">Auditor's Note</h6>
                <p className="text-[11px] leading-loose opacity-60 italic">If a component does not meet material path standards, it is removed from the Registry immediately.</p>
              </div>
            </aside>

            <div className="space-y-12">
              <div className="flex justify-between items-center border-b border-black/5 pb-4">
                <p className="text-[10px] uppercase tracking-widest font-sans font-bold text-black/40">Showing {filteredProducts.length} Verified Items</p>
                <div className="flex items-center gap-2 text-[10px] font-sans font-bold uppercase tracking-widest opacity-60">Sorted by Audit Status <Grid size={14} /></div>
              </div>
              {filteredProducts.length === 0 ? (
                <div className="py-24 text-center space-y-6">
                  <div className="h-16 w-16 border-2 border-black/10 rounded-full mx-auto flex items-center justify-center text-black/20"><Search size={32} /></div>
                  <h3 className="text-2xl font-serif italic">No matching hardware found.</h3>
                  <button type="button" onClick={() => {setQuery(''); setActiveCluster('ALL');}} className="text-xs font-sans font-bold uppercase tracking-widest underline underline-offset-4">Reset Registry Filters</button>
                </div>
              ) : (
                <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-3">
                  {filteredProducts.map((product) => (
                    <ProductCard key={product.id} product={product} onAdd={addToCart} onInspect={setSelectedProduct} isSelected={selectedProduct?.id === product.id} />
                  ))}
                </div>
              )}
            </div>
          </div>
        </main>
      )}

      <footer className="border-t border-black bg-white py-20 mt-12">
        <div className="mx-auto max-w-7xl px-5 md:px-8">
          <div className="grid gap-16 md:grid-cols-4">
            <div className="md:col-span-1 space-y-8">
              <div>
                <h4 className="text-2xl font-serif italic font-black">PIXIE'S PANTRY</h4>
                <p className="mt-4 text-sm italic text-black/50 leading-relaxed">Transparency isn’t a feature. It’s the foundation. Hardware for lawful adult contexts only.</p>
              </div>
              <div className="flex gap-4">
                <a href="https://discord.com/invite/SvQQtHHk" target="_blank" rel="noopener noreferrer" className="p-3 border border-black/10 hover:border-black transition-all rounded-full"><MessageSquare size={18} /></a>
                <a href="https://www.instagram.com/pixiespantryshop/" target="_blank" rel="noopener noreferrer" className="p-3 border border-black/10 hover:border-black transition-all rounded-full"><Instagram size={18} /></a>
                <a href="https://www.youtube.com/channel/UCpQhd79nWMsFnwZgI_Okeuw" target="_blank" rel="noopener noreferrer" className="p-3 border border-black/10 hover:border-black transition-all rounded-full"><Youtube size={18} /></a>
              </div>
            </div>

            {[
              { title: "Registry", links: ["Clinical Index", "Shop", "Bundles", "Compatibility", "Standards"] },
              { title: "The Audit", links: ["DME Standards", "Cleaning", "Compliance", "Business Partners", "Brands"] },
              { title: "Support", links: ["Verification Layer", "Affiliate Disclosure", "FAQ", "Warranty", "Contact"] }
            ].map((col, i) => (
              <div key={i} className="space-y-6">
                <h5 className="text-[11px] uppercase tracking-[0.4em] font-sans font-bold border-b border-black/10 pb-4 text-black/40">{col.title}</h5>
                <ul className="space-y-4">
                  {col.links.map((link, j) => (
                    <li key={j}><button type="button" className="text-[10px] uppercase font-sans font-bold tracking-[0.2em] text-black/60 hover:text-black transition-colors">{link}</button></li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
          <div className="mt-20 pt-10 border-t border-black/10 text-center">
            <p className="text-[10px] uppercase tracking-[0.5em] text-black/40 font-sans font-bold leading-relaxed">
              © 2026 MISSISSIPPI PRECISION — CLINICAL HARDWARE REGISTRY v2.6.2
            </p>
          </div>
        </div>
      </footer>

      {payloadOpen && (
        <aside className="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm p-4 md:p-10">
          <div className="h-full w-full max-w-4xl overflow-hidden flex flex-col bg-[#f7f4ef] border-2 border-black shadow-2xl rounded-sm">
            <div className="flex items-center justify-between border-b border-black/10 p-6 bg-white font-serif italic uppercase tracking-widest">
              <h2>Registry Data Object</h2>
              <button type="button" onClick={() => setPayloadOpen(false)}><X size={24}/></button>
            </div>
            <div className="flex-1 bg-black p-8 font-mono text-[11px] text-green-500 overflow-y-auto">
              <pre>{JSON.stringify({ view, activeCluster, cart, subtotal }, null, 2)}</pre>
            </div>
          </div>
        </aside>
      )}

      {cartOpen && (
        <aside className="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm">
          <div className="h-full w-full max-w-xl overflow-y-auto bg-[#f7f4ef] border-l-2 border-black shadow-2xl flex flex-col animate-in slide-in-from-right">
            <div className="flex items-center justify-between border-b border-black/10 p-8 bg-white sticky top-0 z-10">
              <h2 className="text-3xl italic">Order Review</h2>
              <button type="button" onClick={() => setCartOpen(false)} className="h-10 w-10 border border-black flex items-center justify-center hover:bg-black hover:text-white"><X size={20}/></button>
            </div>
            <div className="flex-1 p-8">
              {cart.length === 0 ? <p className="text-center italic opacity-40 py-20">No items selected.</p> : (
                <div className="space-y-6">
                  {cart.map(item => (
                    <div key={item.id} className="border border-black bg-white p-4 flex justify-between items-center">
                      <div className="space-y-1">
                        <h4 className="font-serif italic text-lg">{item.name}</h4>
                        <p className="text-[10px] font-mono opacity-40">{item.sku}</p>
                      </div>
                      <div className="flex items-center gap-4">
                        <div className="border border-black flex items-center text-xs">
                          <button type="button" onClick={() => updateQuantity(item.id, -1)} className="px-3 py-1">-</button>
                          <span className="px-2">{item.quantity}</span>
                          <button type="button" onClick={() => updateQuantity(item.id, 1)} className="px-3 py-1">+</button>
                        </div>
                        <span className="font-serif font-black">{money(item.price * item.quantity)}</span>
                      </div>
                    </div>
                  ))}
                  <div className="pt-8 border-t border-black">
                    <div className="flex justify-between text-2xl italic mb-8">
                      <span>Total</span>
                      <strong>{money(subtotal)}</strong>
                    </div>
                    <button type="button" className="w-full bg-black text-white py-6 uppercase font-sans font-bold tracking-[0.4em] text-[11px] shadow-2xl">
                      Initiate Secure Checkout
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </aside>
      )}
    </div>
  );
}