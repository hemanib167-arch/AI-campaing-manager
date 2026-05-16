import React, { useState } from 'react';
import { useStore } from './store/useStore';
import { Plane, MessageSquare, Image as ImageIcon, Send, Loader2, CheckCircle2, AlertCircle } from 'lucide-react';

const App = () => {
  const [activeTab, setActiveTab] = useState<'social' | 'copy' | 'banner'>('social');
  const { createSocialJob, createCopyJob, createBannerJob, pollJobStatus, jobs } = useStore();
  
  // Form States
  const [socialForm, setSocialForm] = useState({ type: 'sale', desc: '' });
  const [copyForm, setCopyForm] = useState({ channel: 'email', brief: '', tone: 'professional' });
  const [bannerForm, setBannerForm] = useState({ brief: '', aspect: '16:9' });
  
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    let jobId = '';
    
    try {
      if (activeTab === 'social') {
        jobId = await createSocialJob(socialForm.type, socialForm.desc);
      } else if (activeTab === 'copy') {
        jobId = await createCopyJob(copyForm.channel, copyForm.brief, copyForm.tone);
      } else {
        jobId = await createBannerJob(bannerForm.brief, bannerForm.aspect);
      }
      
      pollJobStatus(jobId);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '3rem' }}>
        <Plane size={40} color="#1A1AAF" />
        <h1 style={{ fontSize: '2.5rem', color: '#1A1AAF' }}>6E Creative Studio</h1>
      </header>

      <div style={{ display: 'flex', gap: '1rem', marginBottom: '2rem' }}>
        {(['social', 'copy', 'banner'] as const).map(tab => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab)}
            className="btn-primary"
            style={{ 
              backgroundColor: activeTab === tab ? '#1A1AAF' : '#eee',
              color: activeTab === tab ? 'white' : '#666'
            }}
          >
            {tab.charAt(0).toUpperCase() + tab.slice(1)}
          </button>
        ))}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
        {/* Input Side */}
        <div className="card">
          <h2>Create New {activeTab.charAt(0).toUpperCase() + activeTab.slice(1)} Content</h2>
          <form onSubmit={handleSubmit} style={{ marginTop: '1.5rem' }}>
            {activeTab === 'social' && (
              <>
                <label>Campaign Type</label>
                <select 
                  className="input" 
                  value={socialForm.type} 
                  onChange={e => setSocialForm({...socialForm, type: e.target.value})}
                >
                  <option value="sale">Flash Sale</option>
                  <option value="new_route">New Route Launch</option>
                  <option value="brand">Brand Awareness</option>
                </select>
                <label>Description</label>
                <textarea 
                  className="input" 
                  rows={4}
                  value={socialForm.desc}
                  onChange={e => setSocialForm({...socialForm, desc: e.target.value})}
                  placeholder="e.g. 15% off on all domestic flights for 48 hours"
                />
              </>
            )}

            {activeTab === 'copy' && (
              <>
                <label>Channel</label>
                <input 
                  className="input" 
                  value={copyForm.channel}
                  onChange={e => setCopyForm({...copyForm, channel: e.target.value})}
                  placeholder="e.g. Email, SMS, App Notification"
                />
                <label>Brief</label>
                <textarea 
                  className="input" 
                  rows={4}
                  value={copyForm.brief}
                  onChange={e => setCopyForm({...copyForm, brief: e.target.value})}
                />
              </>
            )}

            {activeTab === 'banner' && (
              <>
                <label>Visual Brief</label>
                <textarea 
                  className="input" 
                  rows={4}
                  value={bannerForm.brief}
                  onChange={e => setBannerForm({...bannerForm, brief: e.target.value})}
                  placeholder="Describe the scene..."
                />
              </>
            )}

            <button type="submit" className="btn-primary" disabled={loading} style={{ width: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.5rem' }}>
              {loading ? <Loader2 className="animate-spin" /> : <Send size={18} />}
              Generate with AI
            </button>
          </form>
        </div>

        {/* Output Side */}
        <div className="card" style={{ minHeight: '400px' }}>
          <h2>Live Job Queue</h2>
          <div style={{ marginTop: '1.5rem' }}>
            {Object.values(jobs).reverse().map(job => (
              <div key={job.id} className="card animate-fade-in" style={{ border: '1px solid #eee' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
                  <span style={{ fontWeight: 'bold' }}>{job.type.toUpperCase()} - {job.id.slice(0, 8)}</span>
                  <span className={`badge badge-${job.status}`}>{job.status}</span>
                </div>
                
                {job.status === 'completed' && (
                  <pre style={{ background: '#f8f9fa', padding: '1rem', borderRadius: '8px', overflowX: 'auto', fontSize: '0.8rem' }}>
                    {JSON.stringify(job.result, null, 2)}
                  </pre>
                )}
                
                {job.status === 'failed' && (
                  <div style={{ color: '#721c24', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <AlertCircle size={16} />
                    <span>{job.error}</span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
