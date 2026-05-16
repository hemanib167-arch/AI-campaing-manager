import type { FC } from 'react';
import { Loader2, CheckCircle2, AlertCircle, Clock } from 'lucide-react';

interface Job {
  id: string;
  type: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  result?: any;
  error?: string;
  createdAt?: string;
}

interface ResultPanelProps {
  jobs: Record<string, Job>;
}

export const ResultPanel: FC<ResultPanelProps> = ({ jobs }) => {
  const jobArray = Object.values(jobs).reverse();

  const getStatusIcon = (status: Job['status']) => {
    switch (status) {
      case 'completed':
        return <CheckCircle2 size={16} className="text-green-600" />;
      case 'failed':
        return <AlertCircle size={16} className="text-red-600" />;
      case 'processing':
        return <Loader2 size={16} className="text-blue-600 animate-spin" />;
      default:
        return <Clock size={16} className="text-yellow-600" />;
    }
  };

  return (
    <div className="card">
      <h2 className="text-xl font-bold mb-4">Results</h2>

      {jobArray.length === 0 ? (
        <div className="text-center py-12 text-gray-400">
          <p>No jobs yet</p>
          <p className="text-sm mt-1">Submit a form to generate content</p>
        </div>
      ) : (
        <div className="space-y-3 max-h-[600px] overflow-y-auto">
          {jobArray.map(job => (
            <div key={job.id} className="card border border-gray-200 animate-fade-in">
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-2">
                  <span className="font-bold text-sm text-indigo-dark">
                    {job.type.toUpperCase()}
                  </span>
                  <span className="text-xs text-gray-400">#{job.id.slice(0, 8)}</span>
                </div>
                <div className="flex items-center gap-2">
                  {getStatusIcon(job.status)}
                  <span className={`badge badge-${job.status}`}>
                    {job.status}
                  </span>
                </div>
              </div>

              {job.status === 'processing' && (
                <div className="bg-blue-50 p-3 rounded-lg">
                  <p className="text-sm text-blue-700">
                    Processing your request...
                  </p>
                </div>
              )}

              {job.status === 'completed' && job.result && (
                <div className="bg-gray-50 p-4 rounded-lg">
                  {typeof job.result === 'string' ? (
                    <p className="text-sm whitespace-pre-wrap">{job.result}</p>
                  ) : (
                    <pre className="text-xs overflow-x-auto">
                      {JSON.stringify(job.result, null, 2)}
                    </pre>
                  )}
                </div>
              )}

              {job.status === 'failed' && (
                <div className="bg-red-50 p-3 rounded-lg flex items-start gap-2">
                  <AlertCircle size={16} className="text-red-600 mt-0.5" />
                  <div>
                    <p className="text-sm font-medium text-red-800">Failed to generate</p>
                    <p className="text-xs text-red-600 mt-1">{job.error || 'Unknown error'}</p>
                  </div>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
