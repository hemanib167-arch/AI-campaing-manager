import { useState, type FC } from 'react';
import { ArrowLeft } from 'lucide-react';
import { Layout } from '../components/Layout';
import { Tabs, type TabType } from '../components/Tabs';
import { SocialTab } from '../components/SocialTab';
import { CopywritingTab } from '../components/CopywritingTab';
import { BannerTab } from '../components/BannerTab';
import { ImageEditTab } from '../components/ImageEditTab';
import { ResultPanel } from '../components/ResultPanel';
import { useStore } from '../store/useStore';

interface CampaignPageProps {
  projectId: string;
  onBack: () => void;
}

export const CampaignPage: FC<CampaignPageProps> = ({ onBack }) => {
  const [activeTab, setActiveTab] = useState<TabType>('social');
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
    // For now, use banner endpoint
    const jobId = await createBannerJob(data.brief, '16:9');
    pollJobStatus(jobId);
  };

  return (
    <Layout>
      <button
        onClick={onBack}
        className="flex items-center gap-2 text-gray-600 hover:text-indigo-blue mb-6"
      >
        <ArrowLeft size={20} />
        Back to Projects
      </button>

      <div className="mb-6">
        <h2 className="text-2xl font-bold text-indigo-dark mb-2">Campaign Details</h2>
        <p className="text-gray-600">Create and manage campaign content</p>
      </div>

      <Tabs activeTab={activeTab} onTabChange={setActiveTab} />

      {activeTab === 'imageEdit' ? (
        <ImageEditTab onSubmit={handleImageEditSubmit} />
      ) : (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="card">
            {activeTab === 'social' && <SocialTab onSubmit={handleSocialSubmit} />}
            {activeTab === 'copywriting' && <CopywritingTab onSubmit={handleCopySubmit} />}
            {activeTab === 'banner' && <BannerTab onSubmit={handleBannerSubmit} />}
          </div>

          <ResultPanel jobs={jobs} />
        </div>
      )}
    </Layout>
  );
};
