import type { FC } from 'react';
import { Loader2, CheckCircle2, AlertCircle, Clock, Copy, Download, ExternalLink } from 'lucide-react';

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

  const renderSocialResult = (result: any) => {
    const platforms = ['instagram', 'facebook', 'linkedin'];
    return (
      <div className="space-y-6">
        {platforms.map(p => {
          const data = result[p];
          if (!data) return null;
          return (
            <div key={p} className="bg-white border border-gray-100 rounded-xl overflow-hidden shadow-sm">
              <div className="bg-gray-50 px-4 py-2 border-b border-gray-100 flex justify-between items-center">
                <span className="text-xs font-bold uppercase tracking-wider text-gray-500">{p}</span>
                <button className="text-indigo-blue hover:text-indigo-dark transition-colors">
                   <Copy size={14} />
                </button>
              </div>
              {data.image_url && (
                <div className="aspect-square bg-gray-200">
                  <img src={data.image_url} alt={p} className="w-full h-full object-cover" />
                </div>
              )}
              <div className="p-4">
                <p className="text-sm text-gray-800 whitespace-pre-wrap">{data.caption}</p>
                {data.hashtags && (
                  <div className="mt-2 flex flex-wrap gap-1">
                    {data.hashtags.map((h: string) => (
                      <span key={h} className="text-xs text-blue-600 font-medium">#{h}</span>
                    ))}
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    );
  };

  const renderCopyResult = (result: any) => {
    return (
      <div className="space-y-4">
        <div className="bg-indigo-50 p-4 rounded-xl border border-indigo-100">
          <h3 className="text-lg font-bold text-indigo-dark mb-2">{result.headline}</h3>
          <p className="text-sm italic text-indigo-600 mb-3">"{result.hook}"</p>
          <div className="text-sm text-gray-800 leading-relaxed whitespace-pre-wrap mb-4">
            {result.body}
          </div>
          <div className="bg-white p-3 rounded-lg border border-indigo-100 flex items-center justify-between">
             <span className="text-xs font-bold text-indigo-blue uppercase">CTA: {result.cta}</span>
             <button className="text-gray-400 hover:text-indigo-blue"><Copy size={16} /></button>
          </div>
        </div>
        {result.metadata && (
          <div className="flex gap-2 flex-wrap">
             {result.metadata.keywords?.map((k: string) => (
               <span key={k} className="px-2 py-1 bg-gray-100 text-gray-600 rounded text-[10px] font-bold uppercase">{k}</span>
             ))}
          </div>
        )}
      </div>
    );
  };

  const renderBannerResult = (result: any) => {
    return (
      <div className="space-y-4">
        {result.image_url && (
          <div className="rounded-xl overflow-hidden border border-gray-200 shadow-md">
            <img src={result.image_url} alt="Generated Banner" className="w-full h-auto" />
          </div>
        )}
        <div className="bg-gray-50 p-4 rounded-xl">
           <div className="flex items-center justify-between mb-2">
             <span className="text-xs font-bold text-gray-500 uppercase">Mood: {result.mood}</span>
             <a href={result.image_url} target="_blank" rel="noreferrer" className="text-indigo-blue flex items-center gap-1 text-xs font-bold hover:underline">
               <ExternalLink size={14} /> Open Full Res
             </a>
           </div>
           <p className="text-sm font-medium text-gray-800">Headline used in design: {result.headline_text}</p>
        </div>
      </div>
    );
  };

  return (
    <div className="card flex flex-col h-full">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-xl font-bold text-indigo-dark">Real-time Generations</h2>
        <span className="text-xs font-medium text-gray-400">{jobArray.length} requests</span>
      </div>

      {jobArray.length === 0 ? (
        <div className="flex-1 flex flex-col items-center justify-center py-12 text-gray-400">
          <Loader2 size={48} className="mb-4 opacity-10" />
          <p className="font-bold text-gray-300">Ready to create your campaign!</p>
          <p className="text-xs mt-1">Fill out the campaign details on the left to generate tailored content.</p>
        </div>
      ) : (
        <div className="space-y-6 overflow-y-auto pr-2 custom-scrollbar">
          {jobArray.map(job => (
            <div key={job.id} className="animate-fade-in border-b border-gray-100 pb-8 last:border-0">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <div className="w-2 h-2 rounded-full bg-indigo-blue" />
                  <span className="font-bold text-xs uppercase tracking-widest text-indigo-blue">
                    {job.type}
                  </span>
                </div>
                <div className="flex items-center gap-2">
                  {getStatusIcon(job.status)}
                  <span className={`text-[10px] font-bold uppercase tracking-wider ${
                    job.status === 'completed' ? 'text-green-600' : 
                    job.status === 'failed' ? 'text-red-600' : 'text-blue-600'
                  }`}>
                    {job.status}
                  </span>
                </div>
              </div>

              {job.status === 'processing' && (
                <div className="bg-blue-50/50 p-6 rounded-2xl border border-dashed border-blue-200 text-center">
                  <Loader2 size={24} className="mx-auto text-blue-600 animate-spin mb-3" />
                  <p className="text-sm font-medium text-blue-800">Generating with AI...</p>
                  <p className="text-xs text-blue-500 mt-1">Our models are crafting your content.</p>
                </div>
              )}

              {job.status === 'completed' && job.result && (
                <div className="mt-2">
                  {job.type === 'social' && renderSocialResult(job.result)}
                  {job.type === 'copywriting' && renderCopyResult(job.result)}
                  {job.type === 'banner' && renderBannerResult(job.result)}
                  {job.type === 'image_edit' && renderBannerResult(job.result)}
                </div>
              )}

              {job.status === 'failed' && (
                <div className="bg-red-50 p-4 rounded-xl border border-red-100">
                  <div className="flex items-center gap-2 text-red-700 font-bold text-sm mb-1">
                    <AlertCircle size={16} />
                    Failed to generate
                  </div>
                  <p className="text-xs text-red-600">{job.error || 'The AI provider is currently busy. Please try again.'}</p>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
