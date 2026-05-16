import { useEffect, useState, type FC, type FormEvent } from 'react';
import { Plus, Search, Folder, Clock, Plane } from 'lucide-react';
import axios from 'axios';

interface Project {
  id: string;
  name: string;
  description: string;
  created_at: string;
}

interface LandingPageProps {
  onProjectSelect: (projectId: string) => void;
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
    } catch (err) {
      console.error('Failed to create project:', err);
    }
  };

  const filteredProjects = projects.filter(p =>
    p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    p.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const cardColors = [
    { bg: '#FEF3C7', fg: '#D97706' },
    { bg: '#EDE9FE', fg: '#7C3AED' },
    { bg: '#DBEAFE', fg: '#2563EB' },
    { bg: '#D1FAE5', fg: '#059669' },
  ];

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#f9fafb', fontFamily: 'inherit' }}>
      {/* Header - matches workspace header style */}
      <header style={{ backgroundColor: 'white', borderBottom: '1px solid #e5e7eb', padding: '1rem 1.5rem', boxShadow: '0 1px 2px 0 rgb(0 0 0 / 0.05)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <Plane size={32} color="#1A1AAF" />
            <h1 style={{ fontSize: '1.5rem', fontWeight: 700, color: '#1A1AAF', margin: 0 }}>6E Creative Studio</h1>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2.5rem 1.5rem' }}>
        {/* Title + New Project */}
        <div style={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', marginBottom: '2rem' }}>
          <div>
            <h2 style={{ fontSize: '1.875rem', fontWeight: 700, color: '#0a0a4a', margin: 0 }}>Projects</h2>
            <p style={{ color: '#6b7280', marginTop: '0.25rem', fontSize: '0.9rem' }}>
              {projects.length} project{projects.length !== 1 ? 's' : ''} &middot; Manage your creative campaigns
            </p>
          </div>
          <button
            onClick={() => setShowModal(true)}
            className="btn-primary"
            style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}
          >
            <Plus size={18} /> New Project
          </button>
        </div>

        {/* Search */}
        <div style={{ position: 'relative', maxWidth: '400px', marginBottom: '2rem' }}>
          <Search size={18} style={{ position: 'absolute', left: '0.75rem', top: '50%', transform: 'translateY(-50%)', color: '#9ca3af' }} />
          <input
            type="text"
            placeholder="Search projects..."
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            className="input"
            style={{ paddingLeft: '2.5rem' }}
          />
        </div>

        {/* Grid */}
        {loading ? (
          <div style={{ textAlign: 'center', padding: '4rem 0', color: '#9ca3af' }}>Loading projects...</div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: '1.5rem' }}>
            {filteredProjects.map((project, i) => {
              const color = cardColors[i % cardColors.length];
              return (
                <div
                  key={project.id}
                  onClick={() => onProjectSelect(project.id)}
                  className="card"
                  style={{ cursor: 'pointer' }}
                >
                  <div style={{ width: '2.5rem', height: '2.5rem', borderRadius: '0.5rem', backgroundColor: color.bg, display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1rem' }}>
                    <Folder size={18} color={color.fg} />
                  </div>
                  <h3 style={{ fontWeight: 700, color: '#0a0a4a', margin: '0 0 0.25rem 0', fontSize: '1rem' }}>{project.name}</h3>
                  <p style={{ fontSize: '0.85rem', color: '#9ca3af', margin: '0 0 1rem 0', minHeight: '2.5rem' }}>{project.description}</p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem', color: '#9ca3af', fontSize: '0.75rem' }}>
                    <Clock size={12} />
                    {new Date(project.created_at).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })}
                  </div>
                </div>
              );
            })}

            {/* New Project card */}
            <div
              onClick={() => setShowModal(true)}
              className="card"
              style={{ cursor: 'pointer', border: '2px dashed #e5e7eb', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '200px' }}
            >
              <div style={{ width: '3rem', height: '3rem', borderRadius: '50%', backgroundColor: '#f9fafb', display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '0.75rem', color: '#9ca3af' }}>
                <Plus size={24} />
              </div>
              <span style={{ fontWeight: 600, color: '#9ca3af' }}>New Project</span>
            </div>
          </div>
        )}

        {!loading && filteredProjects.length === 0 && (
          <div style={{ textAlign: 'center', padding: '4rem 0', color: '#9ca3af' }}>
            {searchQuery ? 'No projects match your search' : 'No projects yet. Create one to get started!'}
          </div>
        )}
      </div>

      {/* Create Project Modal */}
      {showModal && (
        <div style={{ position: 'fixed', inset: 0, backgroundColor: 'rgba(0,0,0,0.4)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100 }}>
          <div style={{ backgroundColor: 'white', borderRadius: '16px', padding: '2rem', width: '100%', maxWidth: '480px', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)' }}>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#0a0a4a', marginBottom: '1.5rem' }}>Create New Project</h3>
            <form onSubmit={handleCreate}>
              <div style={{ marginBottom: '1rem' }}>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: 500, color: '#374151', marginBottom: '0.5rem' }}>Project Name *</label>
                <input
                  className="input"
                  value={newName}
                  onChange={e => setNewName(e.target.value)}
                  placeholder="e.g. Summer Sale 2025"
                  required
                  autoFocus
                />
              </div>
              <div style={{ marginBottom: '1.5rem' }}>
                <label style={{ display: 'block', fontSize: '0.875rem', fontWeight: 500, color: '#374151', marginBottom: '0.5rem' }}>Description</label>
                <textarea
                  className="input"
                  value={newDesc}
                  onChange={e => setNewDesc(e.target.value)}
                  placeholder="Brief description of your campaign..."
                  rows={3}
                />
              </div>
              <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'flex-end' }}>
                <button type="button" onClick={() => setShowModal(false)} style={{ padding: '0.75rem 1.5rem', borderRadius: '10px', border: '1px solid #e5e7eb', backgroundColor: 'white', fontWeight: 600, cursor: 'pointer', fontSize: '0.9rem' }}>
                  Cancel
                </button>
                <button type="submit" className="btn-primary" disabled={!newName.trim()}>
                  Create Project
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
