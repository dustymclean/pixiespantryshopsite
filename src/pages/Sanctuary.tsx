import { BookOpen, ThermometerSnowflake, Layers, ClipboardCheck, LifeBuoy, Mail, ExternalLink, ArrowRight, Shield, Award } from 'lucide-react';
import { motion } from 'motion/react';

export default function Sanctuary() {
  return (
    <div className="bg-[#FAFAFA] text-stone-800 selection:bg-rose-100 selection:text-rose-900">
      {/* Hero Section */}
      <header className="pt-48 pb-24 px-6 relative overflow-hidden bg-white border-b border-stone-100">
        <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-rose-50/30 rounded-full blur-[120px] -z-10"></div>
        <div className="max-w-4xl mx-auto text-center">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center gap-3 px-6 py-2 bg-stone-50 border border-stone-200 rounded-full mb-8 shadow-sm"
          >
            <BookOpen className="w-3 h-3 text-stone-400" />
            <span className="text-[10px] font-black text-stone-500 uppercase tracking-[0.4em]">The Sanctuary</span>
          </motion.div>
          <motion.h1 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="text-6xl md:text-8xl font-serif tracking-tighter text-stone-900 mb-8 leading-tight"
          >
            Intelligence <span className="italic text-stone-400 font-light">Hub.</span>
          </motion.h1>
          <motion.p 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="text-stone-500 text-xl font-serif italic max-w-2xl mx-auto leading-relaxed antialiased"
          >
            The centralized repository for hardware documentation, clinical guides, and the technical bridge between extraction technology and human health.
          </motion.p>
        </div>
      </header>

      {/* Anchor Navigation */}
      <div className="sticky top-24 w-full bg-white/60 backdrop-blur-md border-b border-stone-100 z-40 py-4">
        <div className="max-w-7xl mx-auto px-6 flex justify-center gap-8 md:gap-16">
          {['knowledge', 'logistics', 'warranty', 'support'].map((id) => (
            <a key={id} href={`#${id}`} className="text-[9px] font-black uppercase tracking-widest text-stone-400 hover:text-rose-600 transition-colors">
              {id}
            </a>
          ))}
        </div>
      </div>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-24 space-y-32">
        
        {/* Section: Knowledge */}
        <section id="knowledge" className="space-y-12 scroll-mt-40">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 border-b border-stone-100 pb-8">
            <div>
              <span className="text-[10px] font-black text-rose-500 uppercase tracking-[0.4em]">01 / FOUNDATIONS</span>
              <h2 className="text-4xl md:text-5xl font-serif mt-2 text-stone-900">Technical Registry</h2>
            </div>
            <p className="text-stone-400 font-serif italic max-w-xs leading-relaxed">Vetted guidance on device operation and surgical-grade material safety.</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="glass-card p-10 rounded-[2.5rem] hover:border-rose-200 transition-all group shadow-sm">
              <div className="w-12 h-12 bg-rose-50 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-rose-100 transition-colors">
                <ThermometerSnowflake className="w-6 h-6 text-rose-400" />
              </div>
              <h4 className="text-xl font-bold mb-4 tracking-tight text-stone-900 uppercase">Thermal Indexing</h4>
              <p className="text-sm text-stone-500 leading-relaxed font-serif italic antialiased">
                Comprehensive guide to precision temperature selection. We provide data-driven titration curves to ensure medicine is released without ever hitting the 451°F combustion threshold.
              </p>
            </div>
            <div className="glass-card p-10 rounded-[2.5rem] hover:border-rose-200 transition-all group shadow-sm">
              <div className="w-12 h-12 bg-stone-100 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-stone-200 transition-colors">
                <Layers className="w-6 h-6 text-stone-400" />
              </div>
              <h4 className="text-xl font-bold mb-4 tracking-tight text-stone-900 uppercase">Material Analysis</h4>
              <p className="text-sm text-stone-500 leading-relaxed font-serif italic antialiased">
                A rigorous audit of Borosilicate 3.3, Grade 2 Titanium, and 316L Stainless Steel. We verify certificates of conformance to ensure zero heavy metal leaching in high-heat zones.
              </p>
            </div>
            <div className="glass-card p-10 rounded-[2.5rem] hover:border-rose-200 transition-all group shadow-sm">
              <div className="w-12 h-12 bg-stone-100 rounded-2xl flex items-center justify-center mb-6 group-hover:bg-stone-200 transition-colors">
                <ClipboardCheck className="w-6 h-6 text-stone-400" />
              </div>
              <h4 className="text-xl font-bold mb-4 tracking-tight text-stone-900 uppercase">Sterilization</h4>
              <p className="text-sm text-stone-500 leading-relaxed font-serif italic antialiased">
                Maintenance protocols for respiratory safety. If a hardware component cannot withstand a 91% ISO soak or steam sterilization, it is reclassified as a liability.
              </p>
            </div>
          </div>
        </section>

        {/* Section: Logistics */}
        <section id="logistics" className="space-y-12 scroll-mt-40">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-end gap-6 border-b border-stone-100 pb-8">
            <div>
              <span className="text-[10px] font-black text-rose-500 uppercase tracking-[0.4em]">02 / FULFILLMENT</span>
              <h2 className="text-4xl md:text-5xl font-serif mt-2 text-stone-900">Hardware Logistics</h2>
            </div>
            <p className="text-stone-400 font-serif italic max-w-xs leading-relaxed">Total transparency regarding your device's physical chain of custody.</p>
          </div>
          
          <div className="bg-white border border-stone-200 rounded-[3rem] p-10 md:p-20 overflow-hidden relative shadow-sm">
            <div className="absolute bottom-0 right-0 w-80 h-80 bg-rose-50/40 rounded-full -mr-20 -mb-20 blur-3xl"></div>
            <div className="relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
              <div className="space-y-8">
                <h4 className="text-3xl font-bold tracking-tight text-stone-900 leading-tight">The Mississippi Node</h4>
                <p className="text-stone-500 leading-relaxed font-serif italic text-lg antialiased">
                  "I don't drop-ship. Every unit is physically received at my hub in Mississippi, personally inspected for material integrity, and serialized in the registry before it ships to you."
                </p>
                <div className="space-y-4">
                  {[
                    "Intake Teardown & Batch Verification",
                    "Electronic Thermal Calibration Check",
                    "Secure Clinical-Grade Sterilization Packaging"
                  ].map((step, i) => (
                    <div key={i} className="flex items-center gap-4 group">
                      <span className="w-10 h-10 rounded-full bg-stone-900 text-white flex items-center justify-center text-xs font-bold group-hover:scale-110 transition-transform">{i + 1}</span>
                      <p className="text-[10px] font-black uppercase tracking-widest text-stone-400">{step}</p>
                    </div>
                  ))}
                </div>
              </div>
              <div className="bg-stone-50 p-10 rounded-[2.5rem] border border-stone-100 space-y-6">
                <h5 className="text-[10px] font-black uppercase tracking-[0.3em] text-stone-400">Transit Standards</h5>
                <p className="text-sm text-stone-600 leading-relaxed">
                  Orders are processed within 24-48 business hours. We utilize specialized shipping buffers to ensure delicate quartz and titanium components remain calibrated during transit. <strong>Adult Signature (21+) is mandatory</strong> for all deliveries—no exceptions.
                </p>
                <a href="https://vapes.pixiespantryshop.com/account" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-[10px] font-black text-rose-600 uppercase tracking-widest border-b border-rose-200 pb-1 hover:text-rose-800 transition-colors">
                  Track Your Provision <ArrowRight className="w-3 h-3" />
                </a>
              </div>
            </div>
          </div>
        </section>

        {/* Section: Warranty */}
        <section id="warranty" className="space-y-12 bg-stone-900 text-white p-12 md:p-24 rounded-[3.5rem] shadow-2xl relative overflow-hidden scroll-mt-40">
          <div className="absolute top-0 right-0 w-96 h-96 bg-rose-500/10 rounded-full blur-[100px] -mr-32 -mt-32"></div>
          <div className="max-w-2xl relative z-10">
            <span className="text-[10px] font-black text-rose-400 uppercase tracking-[0.4em]">03 / ACCOUNTABILITY</span>
            <h2 className="text-4xl md:text-6xl font-serif mt-4 tracking-tighter leading-none italic">The Protection Policy</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-16 mt-12 relative z-10">
            <p className="text-stone-400 font-serif italic text-2xl leading-relaxed antialiased">
              "Standard hardware warranties are built to protect corporations. Ours is built to protect your titration schedule. If a device fails, your care stops—I make sure that gap is closed immediately."
            </p>
            <div className="space-y-10">
              <div className="border-l-2 border-stone-700 pl-8 space-y-3">
                <h5 className="font-bold text-xl tracking-tight text-white uppercase">Full Manufacturer Parity</h5>
                <p className="text-sm text-stone-500 leading-relaxed italic">As an authorized distribution node, we honor the full factory warranty on all extraction devices. We deal with the manufacturer so you don't have to.</p>
              </div>
              <div className="border-l-2 border-stone-700 pl-8 space-y-3">
                <h5 className="font-bold text-xl tracking-tight text-white uppercase">Continuity Guarantee</h5>
                <p className="text-sm text-stone-500 leading-relaxed italic">If your device suffers a terminal electronic failure within the first 90 days, verified clinical accounts are eligible for an immediate replacement unit to minimize therapy interruption.</p>
              </div>
            </div>
          </div>
        </section>

        {/* Section: Support */}
        <section id="support" className="text-center space-y-12 py-20 bg-rose-50/30 rounded-[3rem] border border-rose-100 shadow-sm scroll-mt-40">
          <div className="max-w-2xl mx-auto space-y-6">
            <div className="w-16 h-16 bg-white rounded-full shadow-sm flex items-center justify-center mx-auto mb-6">
              <LifeBuoy className="w-8 h-8 text-rose-400" />
            </div>
            <h2 className="text-4xl md:text-6xl font-serif tracking-tight text-stone-900 italic">Support Desk</h2>
            <p className="text-stone-500 font-serif italic text-lg leading-relaxed px-6 antialiased">
              Direct access to technical troubleshooting, cleaning protocols, and clinical hardware specifications. We treat support tickets as diagnostic requests.
            </p>
          </div>
          <div className="flex flex-col sm:flex-row justify-center gap-6 px-6">
            <a href="mailto:support@pixies-pantry.com" className="px-12 py-6 bg-stone-900 text-white rounded-full text-[11px] font-black uppercase tracking-[0.2em] hover:bg-black transition-all shadow-xl shadow-stone-200 flex items-center justify-center gap-3">
               <Mail className="w-4 h-4" /> Diagnostic Ticket
            </a>
            <a href="https://discord.gg/R98q86nm" target="_blank" rel="noopener noreferrer" className="px-12 py-6 bg-white border border-stone-200 text-stone-600 rounded-full text-[11px] font-black uppercase tracking-[0.2em] hover:border-stone-400 transition-all flex items-center justify-center gap-3">
               <ExternalLink className="w-4 h-4" /> Support Portal
            </a>
          </div>
        </section>

      </main>
    </div>
  );
}
