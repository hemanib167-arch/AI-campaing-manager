import { useState } from 'react';
import { Plane } from 'lucide-react';
import { Tabs, type TabType } from './components/Tabs';
import { SocialTab } from './components/SocialTab';
import { CopywritingTab } from './components/CopywritingTab';
import { BannerTab } from './components/BannerTab';
import { ImageEditTab } from './components/ImageEditTab';
import { ResultPanel } from './components/ResultPanel';
import { useStore } from './store/useStore';

const App = () => {
  const [activeTab, setActiveTab] = useState<TabType>('social');
  const [campaignType, setCampaignType] = useState('sale');
  const [description, setDescription] = useState('');

  const { createSocialJob, createCopyJob, createBannerJob, pollJobStatus, jobs } = useStore();

  const handleSocialSubmit = async (data: { campaign_type: string; description: string }) => {
    const jobId = await createSocialJob(data.campaign_type, data.description);
    pollJobStatus(jobId);
  };

  const handleCopySubmit = async (data: { channel: string; brief: string; tone: string }) => {
    const jobId = await createCopyJob(data.channel, data.brief, data.tone);
    pollJobStatus(jobId);
  };

  const handleBannerSubmit = async (data: { brief: string; aspect_ratio: string }) => {
    const jobId = await createBannerJob(data.brief, data.aspect_ratio);
    pollJobStatus(jobId);
  };

  const handleImageEditSubmit = async (data: any) => {
    const jobId = await createBannerJob(data.brief, '16:9');
    pollJobStatus(jobId);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="px-6 py-4">
          <div className="flex items-center gap-3">
            <Plane size={32} color="#1A1AAF" />
            <h1 className="text-2xl font-bold text-indigo-blue">6E Creative Studio</h1>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex" style={{ height: 'calc(100vh - 73px)' }}>
        {/* Left Sidebar - Campaign Details */}
        <aside className="w-96 bg-white border-r border-gray-200 overflow-y-auto">
          <div className="p-8">
            <h2 className="text-xl font-bold mb-6 text-indigo-dark">Campaign Details</h2>

            <div className="space-y-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-3">
                  Campaign Type *
                </label>
                <select
                  value={campaignType}
                  onChange={e => setCampaignType(e.target.value)}
                  className="input"
                >
                  <option value="sale">Flash Sale</option>
                  <option value="new_route">New Route Launch</option>
                  <option value="brand">Brand Awareness</option>
                  <option value="seasonal">Seasonal Campaign</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-3">
                  Description of my campaign *
                </label>
                <textarea
                  value={description}
                  onChange={e => setDescription(e.target.value)}
                  className="input"
                  rows={8}
                  placeholder="e.g. I want to launch a new summer collection for my household fashion brand. The goal is to drive sales among millennials. This same campaign will be publicized on all my social channels, including Facebook, Instagram, X, etc."
                />
              </div>

              <button
                className="btn-primary w-full"
                disabled={!description.trim()}
              >
                Generate Ideas
              </button>
            </div>
          </div>
        </aside>

        {/* Main Content Area */}
        <main className="flex-1 overflow-hidden flex flex-col bg-gray-50">
          {/* Tabs */}
          <div className="bg-white border-b border-gray-200 px-8 pt-4">
            <Tabs activeTab={activeTab} onTabChange={setActiveTab} />
          </div>

          {/* Tab Content */}
          <div className="flex-1 overflow-y-auto p-8">
            {activeTab === 'imageEdit' ? (
              <ImageEditTab onSubmit={handleImageEditSubmit} />
            ) : (
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 max-w-7xl mx-auto w-full">
                <div className="card">
                  {activeTab === 'social' && <SocialTab onSubmit={handleSocialSubmit} />}
                  {activeTab === 'copywriting' && <CopywritingTab onSubmit={handleCopySubmit} />}
                  {activeTab === 'banner' && <BannerTab onSubmit={handleBannerSubmit} />}
                </div>

                <ResultPanel jobs={jobs} />
              </div>
            )}
          </div>
        </main>
      </div>
    </div>
  );
};

export default App;
