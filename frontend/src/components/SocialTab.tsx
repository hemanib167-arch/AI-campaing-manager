import { useState, type FC, type FormEvent } from 'react';
import { Send, Loader2 } from 'lucide-react';

interface SocialTabProps {
  onSubmit: (data: { campaign_type: string; description: string }) => Promise<void>;
}

export const SocialTab: FC<SocialTabProps> = ({ onSubmit }) => {
  const [campaignType, setCampaignType] = useState('sale');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await onSubmit({ campaign_type: campaignType, description });
      setDescription('');
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Campaign Type
        </label>
        <select
          value={campaignType}
          onChange={e => setCampaignType(e.target.value)}
          className="input"
        >
          <option value="sale">Flash Sale</option>
          <option value="new_route">New Route Launch</option>
          <option value="brand">Brand Awareness</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Campaign Description
        </label>
        <textarea
          value={description}
          onChange={e => setDescription(e.target.value)}
          className="input"
          rows={6}
          placeholder="e.g. 15% off on all domestic flights for 48 hours. Valid for bookings made between June 1-3."
          required
        />
      </div>

      <button
        type="submit"
        disabled={loading}
        className="btn-primary w-full flex items-center justify-center gap-2"
      >
        {loading ? (
          <>
            <Loader2 size={18} className="animate-spin" />
            Generating...
          </>
        ) : (
          <>
            <Send size={18} />
            Generate Social Post
          </>
        )}
      </button>
    </form>
  );
};
