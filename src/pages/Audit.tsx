import { 
  Shield, 
  Search, 
  ArrowRight, 
  ChevronRight, 
  Info, 
  AlertCircle, 
  Check, 
  ChevronDown, 
  ChevronUp,
  Users,
  Scale,
  Activity,
  FileText,
  ShieldCheck,
  Thermometer,
  Dna,
  Droplets,
  BookOpen,
  Microscope,
  BarChart3,
  Cpu
} from 'lucide-react';
import { motion, AnimatePresence } from 'motion/react';
import { useState, useEffect, useRef } from 'react';
import DeviceComparison from '../components/audit/DeviceComparison';
import { devices, Device } from '../data/devices';

export default function Audit() {
  const [activeLab, setActiveLab] = useState<'teardown' | 'comparison'>('teardown');
  const [selectedComparisonIds, setSelectedComparisonIds] = useState<string[]>([]);

  const tier1Devices = devices.filter(d => d.tier === 1);
  const tier2Devices = devices.filter(d => d.tier === 2);
  const tier3Devices = devices.filter(d => d.tier === 3);

  const rosterTiers = [
    {
      tier: "Tier 1",
      title: "Clinical Gold Standard",
      description: "Devices with ISO 13485 certification and 100% isolated airpaths.",
      devices: tier1Devices,
      icon: ShieldCheck
    },
    {
      tier: "Tier 2",
      title: "High-Fidelity Consumer",
      description: "Exceptional material safety and thermal stability for daily therapy.",
      devices: tier2Devices,
      icon: Microscope
    },
    {
      tier: "Tier 3",
      title: "Specialized Extraction",
      description: "Manual or niche devices with verified bio-compatible paths.",
      devices: tier3Devices,
      icon: Thermometer
    }
  ];

  return (
    <div className="min-h-screen bg-[#FDFCFD]">
      {/* Hero Section */}
      <header className="pt-48 md:pt-64 pb-24 md:pb-32 px-6 relative overflow-hidden hero-glow">
        <div className="max-w-6xl mx-auto text-center">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="inline-flex items-center gap-3 px-6 py-2 bg-white border border-stone-200 rounded-full shadow-[0_2px_15px_-5px_rgba(0,0,0,0.05)] mb-10"
          >
            <span className="text-[10px] font-black text-stone-600 uppercase tracking-[0.4em]">CLINICAL VERIFICATION</span>
          </motion.div>

          <motion.h2 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="text-6xl md:text-8xl lg:text-[9rem] font-serif tracking-tighter text-stone-900 mb-10 leading-[0.9] md:leading-[0.85]"
          >
            The <span className="italic text-stone-500 font-medium pr-2">Audit.</span><br className="hidden md:block" />
            <span className="gold-text">Verified Integrity.</span>
          </motion.h2>

          <p className="max-w-3xl mx-auto text-stone-500 text-lg md:text-xl font-light leading-relaxed mb-14 font-serif italic antialiased px-4">
            We don't just review hardware; we audit it for clinical safety. Every device that enters our registry undergoes a complete teardown to verify material purity, thermal stability, and long-term bio-compatibility. If it fails our matrix, it never touches our shelf.
          </p>
        </div>
      </section>

      {/* Interactive Lab Section */}
      <section id="interactive-lab" className="py-24 md:py-32 bg-stone-50 border-y border-stone-100 scroll-mt-24">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col lg:flex-row justify-between items-start lg:items-end mb-20 gap-10">
            <div className="max-w-2xl">
              <span className="text-[10px] font-black text-stone-400 uppercase tracking-[0.5em] mb-6 block">INTERACTIVE LAB</span>
              <h3 className="text-4xl md:text-5xl font-serif text-stone-900 tracking-tight leading-tight">
                Clinical Comparison &<br className="hidden md:block"/>Audit Roster
              </h3>
            </div>
            <div className="max-w-md text-stone-500 font-serif italic leading-relaxed text-lg border-l-2 border-stone-200 pl-6">
              "Compare the clinical metrics of verified hardware to ensure your therapy meets the standard."
            </div>
          </div>

          <div className="space-y-12">
            {/* Comparison and Roster Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="bg-white rounded-[2rem] border border-stone-200 p-8 md:p-12">
                <DeviceComparison 
                  selectedIds={selectedComparisonIds} 
                  setSelectedIds={setSelectedComparisonIds} 
                />
              </div>
              
              <div className="bg-stone-900 rounded-[2rem] p-8 md:p-12 text-white flex flex-col justify-center">
                <div className="mb-12">
                  <span className="text-[10px] font-black text-rose-400 uppercase tracking-[0.4em] mb-6 block">AUDIT ROSTER</span>
                  <h4 className="text-3xl md:text-4xl font-serif tracking-tight leading-tight mb-6">Verified Device Classification</h4>
                  <p className="text-stone-400 font-serif italic text-lg leading-relaxed">
                    We categorize hardware into three tiers of clinical reliability.
                  </p>
                </div>

                <div className="space-y-8">
                  {rosterTiers.map((tier, i) => (
                    <div key={i} className="flex items-start gap-6 group">
                      <div className="w-12 h-12 rounded-full border border-rose-900/50 flex items-center justify-center text-rose-400 font-serif italic text-xl group-hover:bg-rose-900/20 transition-all">
                        {i === 0 ? 'I' : i === 1 ? 'II' : 'III'}
                      </div>
                      <div>
                        <h5 className="text-lg font-serif mb-1">{tier.title}</h5>
                        <p className="text-stone-500 text-sm">{tier.description}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Methodology Deep Dive */}
      <section className="py-24 md:py-40 max-w-7xl mx-auto px-6">
        <div className="text-center mb-24">
          <span className="text-[10px] font-black text-stone-400 uppercase tracking-[0.5em] mb-6 block">THE METHODOLOGY</span>
          <h3 className="text-4xl md:text-6xl font-serif text-stone-900 tracking-tight leading-tight mb-8">Four Pillars of Hardware Integrity</h3>
          <p className="max-w-2xl mx-auto text-stone-500 font-serif italic text-lg leading-relaxed">
            Our auditing process is binary. A device either meets the standard, or it is excluded from our registry.
          </p>
        </div>

        <div className="space-y-6">
          <PillarCard 
            icon={Shield}
            subtitle="01"
            title="Vapor Path Purity (TTI)"
            text={
              <>
                <p className="mb-4">
                  Total Thermal Isolation (TTI) is the requirement that inhaled air never comes into contact with electronics, adhesives, or non-certified polymers.
                </p>
                <div className="space-y-4 not-italic">
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">The Standard:</strong> Airpath must be ≥ 98% composed of Borosilicate, Ceramic, 316L Stainless, Grade 2+ Titanium, or PEEK.</p>
                  </div>
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">Failure Criteria:</strong> Any presence of internal glue, exposed circuit boards, or non-medical grade plastics in the heat zone.</p>
                  </div>
                </div>
              </>
            }
            layman="When hardware heats up, cheap materials undergo \"off-gassing\"—releasing volatile organic compounds (VOCs) directly into the aerosol. By mandating TTI, we ensure that the only thing you are inhaling is the intended plant profile, free from manufacturing byproducts."
            verifiedBy="VERIFIED BY TEARDOWN"
          />

          <PillarCard 
            icon={Thermometer}
            subtitle="02"
            title="Thermal Stability (PTC)"
            text={
              <>
                <p className="mb-4">
                  Precision Thermoregulation Control (PTC) ensures that the device maintains a consistent temperature during active inhalation.
                </p>
                <div className="space-y-4 not-italic">
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">The Standard:</strong> Real-time temperature fluctuations must remain ≤ ± 2°F during active draw.</p>
                  </div>
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">Failure Criteria:</strong> Thermal crash during draw or overheating that breaches the 455°F combustion threshold.</p>
                  </div>
                </div>
              </>
            }
            layman="Medical efficacy relies on consistent decarboxylation. If a heater cannot maintain its set point during a draw, the aerosol profile changes, leading to uneven dosing and potential respiratory irritation from combustion byproducts."
            verifiedBy="VERIFIED BY THERMOCOUPLE"
          />

          <PillarCard 
            icon={Dna}
            subtitle="03"
            title="Bio-Compatibility (SGC)"
            text={
              <>
                <p className="mb-4">
                  Surgical Grade Compliance (SGC) mandates that all contact surfaces meet international standards for long-term safety.
                </p>
                <div className="space-y-4 not-italic">
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">The Standard:</strong> Materials in contact with plant matter or mucosa must be ISO 10993 or USP Class VI compliant.</p>
                  </div>
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">Failure Criteria:</strong> Use of industrial-grade metals, non-certified silicone, or reactive coatings.</p>
                  </div>
                </div>
              </>
            }
            layman="Chronic exposure to non-biocompatible materials can lead to systemic toxicity. We ensure that every surface touching your plant or your body is as safe as a surgical instrument."
            verifiedBy="VERIFIED BY MATERIAL CERT"
          />

          <PillarCard 
            icon={Droplets}
            subtitle="04"
            title="Sanitization & Hygiene"
            text={
              <>
                <p className="mb-4">
                  For a device to be truly medical-grade, it must be capable of being fully sanitized without degradation.
                </p>
                <div className="space-y-4 not-italic">
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">The Standard:</strong> Device must be ≥ 90% submersible in 91% ISO or withstand 250°F steam sterilization.</p>
                  </div>
                  <div className="flex items-start gap-4">
                    <div className="w-1.5 h-1.5 rounded-full bg-rose-400 mt-2"></div>
                    <p className="text-stone-500 text-sm"><strong className="text-stone-900">Failure Criteria:</strong> Non-removable vapor paths, porous materials that trap bacteria, or warping under heat.</p>
                  </div>
                </div>
              </>
            }
            layman="Bio-film accumulation is a major risk in long-term therapy. If a device cannot be returned to a \"factory clean\" state easily, it poses a long-term respiratory health risk."
            verifiedBy="VERIFIED BY CLEANING TEST"
          />
        </div>
      </section>

      {/* Clinical Bridge Section */}
      <section className="py-24 md:py-40 bg-stone-950 text-white relative overflow-hidden">
        <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-rose-900/10 rounded-full blur-[120px]"></div>
        <div className="max-w-7xl mx-auto px-6 relative z-10">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-20 items-center">
            <div>
              <span className="text-[10px] font-black text-rose-400 uppercase tracking-[0.5em] mb-8 block">THE CLINICAL BRIDGE</span>
              <h3 className="text-4xl md:text-6xl font-serif tracking-tight leading-tight mb-10">From Consumer Tech to Medical Device.</h3>
              <p className="text-stone-400 font-serif italic text-xl leading-relaxed mb-12">
                We are bridging the gap between "boutique hardware" and "durable medical equipment." Our goal is to provide the data necessary for healthcare providers to prescribe these units with confidence.
              </p>
              
              <div className="space-y-8">
                <div className="flex items-start gap-6">
                  <div className="w-12 h-12 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center shrink-0">
                    <FileText className="w-6 h-6 text-rose-400" />
                  </div>
                  <div>
                    <h5 className="text-lg font-serif mb-2 text-white">HCPCS Reclassification</h5>
                    <p className="text-stone-500 text-sm">Mapping hardware to existing medical coding for future insurance reimbursement.</p>
                  </div>
                </div>
                <div className="flex items-start gap-6">
                  <div className="w-12 h-12 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center shrink-0">
                    <Activity className="w-6 h-6 text-rose-400" />
                  </div>
                  <div>
                    <h5 className="text-lg font-serif mb-2 text-white">Titrated Delivery Data</h5>
                    <p className="text-stone-500 text-sm">Verifying that hardware can deliver precise, repeatable aerosol dosages for clinical study.</p>
                  </div>
                </div>
              </div>
            </div>
            <div className="bg-white/5 border border-white/10 rounded-[3rem] p-12 backdrop-blur-sm">
              <h4 className="text-2xl font-serif mb-8 text-rose-100 italic">Lexicon Reclassification</h4>
              <div className="space-y-6">
                <div className="p-6 rounded-2xl bg-white/5 border border-white/5">
                  <span className="text-[10px] font-black text-stone-500 uppercase tracking-widest block mb-2">CONSUMER TERM</span>
                  <p className="text-lg font-serif line-through text-stone-600 mb-4">"Vaporizer"</p>
                  <span className="text-[10px] font-black text-rose-400 uppercase tracking-widest block mb-2">CLINICAL TERM</span>
                  <p className="text-xl font-serif text-white">Precision Thermal Extraction Unit</p>
                </div>
                <div className="p-6 rounded-2xl bg-white/5 border border-white/5">
                  <span className="text-[10px] font-black text-stone-500 uppercase tracking-widest block mb-2">CONSUMER TERM</span>
                  <p className="text-lg font-serif line-through text-stone-600 mb-4">"Hitting it"</p>
                  <span className="text-[10px] font-black text-rose-400 uppercase tracking-widest block mb-2">CLINICAL TERM</span>
                  <p className="text-xl font-serif text-white">Titrated Aerosol Inhalation</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FOOTER SIGNATURE */}
      <footer className="py-32 bg-stone-50 border-t border-stone-100 relative overflow-hidden text-center">
        <div className="max-w-4xl mx-auto px-6 relative z-10">
          <div className="w-20 h-[1px] bg-rose-200 mx-auto mb-10"></div>
          <p className="text-4xl font-serif italic text-stone-700 leading-tight mb-12 antialiased">
            "Transparency isn't a feature—it's the foundation."
          </p>
          <div className="flex flex-col items-center">
            <span className="text-[12px] font-black text-rose-500 uppercase tracking-[0.6em] mb-2">— DUSTY LYN MCLEAN</span>
            <span className="text-[9px] font-bold text-stone-400 uppercase tracking-widest">FOUNDER & CHIEF AUDITOR</span>
          </div>
        </div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-[15vw] font-serif italic opacity-[0.03] select-none pointer-events-none whitespace-nowrap">
          Pixie's Pantry
        </div>
      </footer>
    </div>
  );
}

const PillarCard = ({ icon: Icon, subtitle, title, text, layman, verifiedBy }: any) => {
  const [isExpanded, setIsExpanded] = useState(false);
  return (
    <div 
      className={`bg-white border rounded-[2rem] overflow-hidden transition-all duration-500 ${isExpanded ? 'border-rose-500 shadow-2xl' : 'border-stone-200 hover:border-rose-200'}`}
    >
      <button 
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full px-8 md:px-12 py-10 flex justify-between items-center text-left group"
      >
        <div className="flex items-center gap-6">
          <div className={`w-12 h-12 rounded-2xl flex items-center justify-center transition-colors ${isExpanded ? 'bg-rose-500 text-white' : 'bg-stone-50 text-stone-400 group-hover:bg-rose-50 group-hover:text-rose-500'}`}>
            <Icon className="w-6 h-6" />
          </div>
          <div>
            <span className="text-[9px] font-black text-stone-400 uppercase tracking-widest block mb-1">{subtitle}</span>
            <h4 className="text-xl md:text-2xl font-serif text-stone-900">{title}</h4>
          </div>
        </div>
        <div className={`w-8 h-8 rounded-full border border-stone-100 flex items-center justify-center transition-transform duration-500 ${isExpanded ? 'rotate-180 bg-rose-50 border-rose-200' : ''}`}>
          <ChevronDown className="w-4 h-4 text-stone-400" />
        </div>
      </button>
      
      <AnimatePresence>
        {isExpanded && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.4, ease: "circOut" }}
          >
            <div className="px-8 md:px-12 pb-12 pt-4 border-t border-stone-50">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
                <div className="space-y-6">
                  <div className="text-stone-600 font-serif italic text-lg leading-relaxed">
                    {text}
                  </div>
                </div>
                <div className="bg-stone-50 p-8 rounded-2xl border border-stone-100">
                  <h5 className="text-[10px] font-black text-stone-900 uppercase tracking-widest mb-6">WHY IT MATTERS</h5>
                  <p className="text-stone-500 text-sm leading-relaxed mb-6">
                    {layman}
                  </p>
                  <div className="flex items-center gap-3 text-rose-500">
                    <ShieldCheck className="w-5 h-5" />
                    <span className="text-[10px] font-bold uppercase tracking-widest">{verifiedBy}</span>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};
d text-sm md:text-base italic">
      {answer}
    </p>
  </div>
);
