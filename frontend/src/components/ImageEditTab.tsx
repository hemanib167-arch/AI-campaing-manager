import { useState, type FC, type FormEvent, type ChangeEvent } from 'react';
import { Upload, Loader2, Download } from 'lucide-react';

interface ImageEditTabProps {
  onSubmit: (data: { brief: string; referenceImages: string[]; width?: number; height?: number }) => Promise<void>;
}

export const ImageEditTab: FC<ImageEditTabProps> = ({ onSubmit }) => {
  const [brief, setBrief] = useState('');
  const [aspectRatio, setAspectRatio] = useState('16:9');
  const [resolution, setResolution] = useState('1K');
  const [customWidth, setCustomWidth] = useState('1920');
  const [customHeight, setCustomHeight] = useState('1080');
  const [referenceImages, setReferenceImages] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  const handleImageUpload = (e: ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files) {
      const imageUrls = Array.from(files).map(file => URL.createObjectURL(file));
      setReferenceImages(prev => [...prev, ...imageUrls]);
    }
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await onSubmit({
        brief,
        referenceImages,
        width: parseInt(customWidth),
        height: parseInt(customHeight),
      });
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="grid grid-cols-2 gap-6">
      {/* Left Panel - Input */}
      <div className="space-y-6">
        <div className="card">
          <h3 className="text-lg font-bold mb-4">Website Creative</h3>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Creative brief *
              </label>
              <textarea
                value={brief}
                onChange={e => setBrief(e.target.value)}
                className="input"
                rows={4}
                placeholder="hi"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Reference images <span className="text-gray-400">(optional, max 5)</span>
              </label>
              <div className="border-2 border-dashed border-gray-300 rounded-lg p-4 text-center hover:border-indigo-blue transition-colors cursor-pointer">
                <input
                  type="file"
                  multiple
                  accept="image/*"
                  onChange={handleImageUpload}
                  className="hidden"
                  id="image-upload"
                />
                <label htmlFor="image-upload" className="cursor-pointer flex flex-col items-center gap-2">
                  <Upload size={24} className="text-gray-400" />
                  <span className="text-sm text-gray-600">Add images</span>
                </label>
              </div>
              {referenceImages.length > 0 && (
                <div className="grid grid-cols-3 gap-2 mt-3">
                  {referenceImages.map((img, idx) => (
                    <img key={idx} src={img} alt={`ref-${idx}`} className="w-full h-20 object-cover rounded" />
                  ))}
                </div>
              )}
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Aspect ratio
                </label>
                <select
                  value={aspectRatio}
                  onChange={e => setAspectRatio(e.target.value)}
                  className="input"
                >
                  <option value="16:9">16:9</option>
                  <option value="1:1">1:1</option>
                  <option value="9:16">9:16</option>
                  <option value="4:3">4:3</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Resolution level
                </label>
                <select
                  value={resolution}
                  onChange={e => setResolution(e.target.value)}
                  className="input"
                >
                  <option value="1K">1K</option>
                  <option value="2K">2K</option>
                  <option value="4K">4K</option>
                </select>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Custom width <span className="text-gray-400">(px, optional)</span>
                </label>
                <input
                  type="number"
                  value={customWidth}
                  onChange={e => setCustomWidth(e.target.value)}
                  className="input"
                  placeholder="e.g. 1920"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Custom height <span className="text-gray-400">(px, optional)</span>
                </label>
                <input
                  type="number"
                  value={customHeight}
                  onChange={e => setCustomHeight(e.target.value)}
                  className="input"
                  placeholder="e.g. 1080"
                />
              </div>
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
                  Generate website image
                </>
              )}
            </button>
          </form>
        </div>
      </div>

      {/* Right Panel - Result */}
      <div className="card">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-bold">Result</h3>
          {loading && <span className="text-sm text-gray-500">Refining details...</span>}
        </div>

        <div className="bg-gray-100 rounded-lg aspect-video flex items-center justify-center">
          {loading ? (
            <div className="text-center">
              <Loader2 size={48} className="animate-spin text-indigo-blue mx-auto mb-3" />
              <p className="text-sm text-gray-600">Balancing composition...</p>
              <p className="text-xs text-gray-400 mt-1">This may take a few moments</p>
            </div>
          ) : (
            <div className="text-center text-gray-400">
              <p className="text-sm">Your generated image will appear here</p>
            </div>
          )}
        </div>

        {!loading && (
          <button className="btn-primary w-full mt-4 flex items-center justify-center gap-2" disabled>
            <Download size={18} />
            Download Image
          </button>
        )}
      </div>
    </div>
  );
};
