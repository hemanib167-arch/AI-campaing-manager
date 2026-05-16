import type { FC } from 'react';
import { Calendar, FileText } from 'lucide-react';

interface ProjectCardProps {
  id: string;
  name: string;
  description: string;
  createdAt: string;
  onClick: () => void;
}

export const ProjectCard: FC<ProjectCardProps> = ({
  name,
  description,
  createdAt,
  onClick
}) => {
  return (
    <div
      onClick={onClick}
      className="card cursor-pointer hover:shadow-lg transition-shadow"
    >
      <div className="flex items-start gap-3 mb-3">
        <div className="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center">
          <FileText size={24} color="#1A1AAF" />
        </div>
        <div className="flex-1">
          <h3 className="font-bold text-lg text-indigo-dark">{name}</h3>
          <p className="text-sm text-gray-600 mt-1">{description}</p>
        </div>
      </div>
      <div className="flex items-center gap-2 text-xs text-gray-500 mt-3 pt-3 border-t">
        <Calendar size={14} />
        <span>{new Date(createdAt).toLocaleDateString()}</span>
      </div>
    </div>
  );
};
