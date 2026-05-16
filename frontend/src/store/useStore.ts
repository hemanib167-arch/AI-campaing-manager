import { create } from 'zustand';
import axios from 'axios';

interface Job {
  id: string;
  type: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  result?: any;
  error?: string;
}

interface State {
  jobs: Record<string, Job>;
  loading: boolean;
  createSocialJob: (campaign_type: string, description: string) => Promise<string>;
  createCopyJob: (channel: string, brief: string, tone: string) => Promise<string>;
  createBannerJob: (brief: string, aspect_ratio: string) => Promise<string>;
  pollJobStatus: (jobId: string) => Promise<void>;
}

export const useStore = create<State>((set, get) => ({
  jobs: {},
  loading: false,

  createSocialJob: async (campaign_type, description) => {
    const res = await axios.post('http://localhost:8000/api/campaigns/social', { campaign_type, description });
    const job = res.data;
    set((state) => ({ jobs: { ...state.jobs, [job.id]: job } }));
    return job.id;
  },

  createCopyJob: async (channel, brief, tone) => {
    const res = await axios.post('http://localhost:8000/api/campaigns/copy', { channel, brief, tone });
    const job = res.data;
    set((state) => ({ jobs: { ...state.jobs, [job.id]: job } }));
    return job.id;
  },

  createBannerJob: async (brief, aspect_ratio) => {
    const res = await axios.post('http://localhost:8000/api/campaigns/banner', { brief, aspect_ratio });
    const job = res.data;
    set((state) => ({ jobs: { ...state.jobs, [job.id]: job } }));
    return job.id;
  },

  pollJobStatus: async (jobId) => {
    const res = await axios.get(`http://localhost:8000/api/jobs/${jobId}`);
    const updatedJob = res.data;
    set((state) => ({ jobs: { ...state.jobs, [jobId]: updatedJob } }));
    
    if (updatedJob.status === 'pending' || updatedJob.status === 'processing') {
      setTimeout(() => get().pollJobStatus(jobId), 2000);
    }
  }
}));
