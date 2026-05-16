import { useState, type FC, type FormEvent } from 'react';
import { Send, Loader2 } from 'lucide-react';

interface CopywritingTabProps {
  onSubmit: (data: { channel: string; brief: string; tone: string }) => Promise<void>;
}

export const CopywritingTab: FC<CopywritingTabProps> = ({ onSubmit }) => {
  const [channel, setChannel] = useState('email');
  const [brief, setBrief] = useState('');
  const [tone, setTone] = useState('professional');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await onSubmit({ channel, brief, tone });
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
          Channel
        </label>
        <select
          value={channel}
          onChange={e => setChannel(e.target.value)}
          className="input"
        >
          <option value="email">Email</option>
          <option value="sms">SMS</option>
          <option value="push">Push Notification</option>
          <option value="website">Website</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Tone
        </label>
        <select
          value={tone}
          onChange={e => setTone(e.target.value)}
          className="input"
        >
          <option value="professional">Professional</option>
          <option value="friendly">Friendly</option>
          <option value="urgent">Urgent</option>
          <option value="casual">Casual</option>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Brief
        </label>
        <textarea
          value={brief}
          onChange={e => setBrief(e.target.value)}
          className="input"
          rows={6}
          placeholder="e.g. Write an email promoting our new mobile app with exclusive features for frequent flyers..."
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
            Generate Copy
          </>
        )}
      </button>
    </form>
  );
};
