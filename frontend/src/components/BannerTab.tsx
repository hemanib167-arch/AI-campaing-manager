import { useState, type FC, type FormEvent } from 'react';
import { Send, Loader2 } from 'lucide-react';

interface BannerTabProps {
  onSubmit: (data: { brief: string; aspect_ratio: string }) => Promise<void>;
}

export const BannerTab: FC<BannerTabProps> = ({ onSubmit }) => {
  const [brief, setBrief] = useState('');
  const [aspectRatio, setAspectRatio] = useState('16:9');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await onSubmit({ brief, aspect_ratio: aspectRatio });
      setBrief('');
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
          Aspect Ratio
        </label>
        <select
          value={aspectRatio}
          onChange={e => setAspectRatio(e.target.value)}
          className="input"
        >
          <option value="16:9">16:9 (Landscape)</option>
          <option value="1:1">1:1 (Square)</option>
          <option value="9:16">9:16 (Portrait)</option>
          <option value="4:3">4:3 (Standard)</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Visual Brief
        </label>
        <textarea
          value={brief}
          onChange={e => setBrief(e.target.value)}
          className="input"
          rows={6}
          placeholder="e.g. Create a banner featuring an IndiGo aircraft against a sunset sky, with bold text announcing '50% off international routes'"
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
            Generate Banner
          </>
        )}
      </button>
    </form>
  );
};
