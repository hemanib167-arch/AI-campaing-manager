import { useEffect, useState, type FC } from 'react';
import { Plus, Search } from 'lucide-react';
import { Layout } from '../components/Layout';
import { ProjectCard } from '../components/ProjectCard';
import axios from 'axios';

interface Project {
  id: string;
  name: string;
  description: string;
  created_at: string;
}

interface ProjectsPageProps {
  onProjectSelect: (projectId: string) => void;
}

export const ProjectsPage: FC<ProjectsPageProps> = ({ onProjectSelect }) => {
  const [projects, setProjects] = useState<Project[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [loading, setLoading] = useState(true);

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

  const handleNewProject = async () => {
    const name = prompt('Enter project name:');
    if (!name) return;

    const description = prompt('Enter project description:') || '';

    try {
      const res = await axios.post('http://localhost:8000/api/projects', { name, description });
      setProjects(prev => [res.data, ...prev]);
    } catch (err) {
      console.error('Failed to create project:', err);
      alert('Failed to create project');
    }
  };

  const filteredProjects = projects.filter(p =>
    p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    p.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <Layout>
      <div className="mb-6">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h2 className="text-3xl font-bold text-indigo-dark">Projects</h2>
            <p className="text-gray-600 mt-1">Manage your creative campaigns</p>
          </div>
          <button
            onClick={handleNewProject}
            className="btn-primary flex items-center gap-2"
          >
            <Plus size={18} />
            New Project
          </button>
        </div>

        <div className="relative">
          <Search size={20} className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
          <input
            type="text"
            placeholder="Search projects..."
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            className="input pl-10"
          />
        </div>
      </div>

      {loading ? (
        <div className="text-center py-12">
          <p className="text-gray-400">Loading projects...</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredProjects.map(project => (
            <ProjectCard
              key={project.id}
              id={project.id}
              name={project.name}
              description={project.description}
              createdAt={project.created_at}
              onClick={() => onProjectSelect(project.id)}
            />
          ))}
        </div>
      )}

      {!loading && filteredProjects.length === 0 && (
        <div className="text-center py-12">
          <p className="text-gray-400">
            {searchQuery ? 'No projects match your search' : 'No projects yet'}
          </p>
        </div>
      )}
    </Layout>
  );
};
