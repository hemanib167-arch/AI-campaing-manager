import { useEffect, useState, type FC, type FormEvent } from 'react';
import { Plus, Search, Folder, Clock, Plane, MessageSquare, PenTool, Image, ArrowRight } from 'lucide-react';
import axios from 'axios';

interface Project {
  id: string;
  name: string;
  description: string;
  created_at: string;
}

interface LandingPageProps {
  onProjectSelect: (projectId: string, initialTab?: string) => void;
}

export const LandingPage: FC<LandingPageProps> = ({ onProjectSelect }) => {
  const [projects, setProjects] = useState<Project[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [newName, setNewName] = useState('');
  const [newDesc, setNewDesc] = useState('');

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    try {
      const res = await axios.get('http://localhost:8000/api/projects');
      setProjects(res.data);
    } catch (err) {
      console.error('Failed to load projects:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = async (e: FormEvent) => {
    e.preventDefault();
    if (!newName.trim()) return;
    try {
      const res = await axios.post('http://localhost:8000/api/projects', {
        name: newName,
        description: newDesc || 'No description provided',
      });
      setProjects(prev => [res.data, ...prev]);
      setShowModal(false);
      setNewName('');
      setNewDesc('');
      // Navigate to the new project immediately
      onProjectSelect(res.data.id);
    } catch (err) {
      console.error('Failed to create project:', err);
    }
  };

  const services = [
    { id: 'social', label: 'Social Media', icon: MessageSquare, color: '#1A1AAF', desc: 'Generate platform-specific images & captions.' },
    { id: 'copywriting', label: 'Copywriting', icon: PenTool, color: '#7C3AED', desc: 'Detailed professional marketing copy.' },
    { id: 'banner', label: 'Ad Banners', icon: Image, color: '#D97706', desc: 'High-res banners with embedded text.' },
  ];

  const filteredProjects = projects.filter(p =>
    p.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#F8F9FD', fontFamily: 'inherit', color: '#0a0a4a' }}>
      {/* Header */}
      <header style={{ backgroundColor: 'white', borderBottom: '1px solid #eef2ff', padding: '1rem 2rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between', position: 'sticky', top: 0, zIndex: 10 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <Plane size={32} color="#1A1AAF" />
          <h1 style={{ fontSize: '1.4rem', fontWeight: 800, color: '#1A1AAF', margin: 0, letterSpacing: '-0.02em' }}>6E Creative Studio</h1>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
           <button onClick={() => setShowModal(true)} className="btn-primary" style={{ padding: '0.6rem 1.2rem' }}>
             + New Project
           </button>
        </div>
      </header>

      <main style={{ maxWidth: '1400px', margin: '0 auto', padding: '3rem 2rem' }}>
        {/* Service Highlights */}
        <section style={{ marginBottom: '5rem' }}>
          <h2 style={{ fontSize: '2rem', fontWeight: 800, marginBottom: '2rem', textAlign: 'center' }}>What would you like to create today?</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '1.5rem' }}>
            {services.map(s => (
              <div 
                key={s.id} 
                onClick={() => projects.length > 0 ? onProjectSelect(projects[0].id, s.id) : setShowModal(true)}
                className="card" 
                style={{ cursor: 'pointer', padding: '2.5rem', display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center', transition: 'all 0.3s ease' }}
              >
                <div style={{ width: '4rem', height: '4rem', borderRadius: '1.25rem', backgroundColor: `${s.color}15`, color: s.color, display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1.5rem' }}>
                  <s.icon size={32} />
                </div>
                <h3 style={{ fontSize: '1.25rem', fontWeight: 800, marginBottom: '0.5rem' }}>{s.label}</h3>
                <p style={{ color: '#64748b', fontSize: '0.9rem', marginBottom: '1.5rem', lineHeight: 1.5 }}>{s.desc}</p>
                <div style={{ color: s.color, display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.85rem', fontWeight: 700 }}>
                  Start Creating <ArrowRight size={16} />
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Project List */}
        <section>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '2.5rem' }}>
            <h2 style={{ fontSize: '1.75rem', fontWeight: 800 }}>Recent Projects</h2>
            <div style={{ position: 'relative', width: '300px' }}>
              <Search size={18} style={{ position: 'absolute', left: '0.85rem', top: '50%', transform: 'translateY(-50%)', color: '#94a3b8' }} />
              <input 
                type="text" 
                placeholder="Search projects..." 
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
                className="input" 
                style={{ paddingLeft: '2.75rem', borderRadius: '12px', border: '1px solid #e2e8f0', backgroundColor: 'white' }} 
              />
            </div>
          </div>

          {loading ? (
            <div style={{ textAlign: 'center', padding: '5rem', color: '#94a3b8' }}>Loading your creative space...</div>
          ) : (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '1.5rem' }}>
              {filteredProjects.map((p, i) => (
                <div 
                  key={p.id} 
                  onClick={() => onProjectSelect(p.id)}
                  className="card" 
                  style={{ cursor: 'pointer', padding: '1.5rem', display: 'flex', gap: '1rem', alignItems: 'center' }}
                >
                  <div style={{ width: '3rem', height: '3rem', borderRadius: '10px', backgroundColor: '#F1F5F9', color: '#64748b', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                    <Folder size={20} />
                  </div>
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <h4 style={{ fontWeight: 800, fontSize: '1rem', marginBottom: '0.15rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{p.name}</h4>
                    <p style={{ fontSize: '0.75rem', color: '#94a3b8', display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                      <Clock size={12} /> {new Date(p.created_at).toLocaleDateString()}
                    </p>
                  </div>
                  <ArrowRight size={18} color="#CBD5E1" />
                </div>
              ))}

              <div 
                onClick={() => setShowModal(true)}
                className="card" 
                style={{ cursor: 'pointer', padding: '1.5rem', display: 'flex', gap: '1rem', alignItems: 'center', border: '2px dashed #E2E8F0', backgroundColor: 'transparent' }}
              >
                <div style={{ width: '3rem', height: '3rem', borderRadius: '10px', backgroundColor: '#F8FAFC', color: '#94a3b8', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                  <Plus size={20} />
                </div>
                <span style={{ fontWeight: 800, color: '#94a3b8' }}>New Project</span>
              </div>
            </div>
          )}
        </section>
      </main>

      {/* Modal - exact same logic as before */}
      {showModal && (
        <div style={{ position: 'fixed', inset: 0, backgroundColor: 'rgba(15, 23, 42, 0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100, backdropFilter: 'blur(4px)' }}>
          <div style={{ backgroundColor: 'white', borderRadius: '24px', padding: '2.5rem', width: '100%', maxWidth: '500px', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)' }}>
            <h3 style={{ fontSize: '1.5rem', fontWeight: 800, marginBottom: '0.5rem' }}>Create New Project</h3>
            <p style={{ color: '#64748b', fontSize: '0.9rem', marginBottom: '2rem' }}>Every campaign starts with a project. Give it a name to begin.</p>
            <form onSubmit={handleCreate}>
              <div style={{ marginBottom: '1.5rem' }}>
                <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 700, color: '#475569', marginBottom: '0.5rem' }}>PROJECT NAME *</label>
                <input className="input" value={newName} onChange={e => setNewName(e.target.value)} placeholder="e.g. London Route Launch" required autoFocus />
              </div>
              <div style={{ marginBottom: '2rem' }}>
                <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 700, color: '#475569', marginBottom: '0.5rem' }}>DESCRIPTION</label>
                <textarea className="input" value={newDesc} onChange={e => setNewDesc(e.target.value)} placeholder="What is this campaign about?" rows={3} />
              </div>
              <div style={{ display: 'flex', gap: '1rem' }}>
                <button type="button" onClick={() => setShowModal(false)} style={{ flex: 1, padding: '0.85rem', borderRadius: '12px', border: '1px solid #E2E8F0', backgroundColor: 'white', fontWeight: 700, cursor: 'pointer' }}>Cancel</button>
                <button type="submit" className="btn-primary" style={{ flex: 1, padding: '0.85rem' }} disabled={!newName.trim()}>Create Project</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
