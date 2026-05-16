import type { FC } from 'react';
import { MessageSquare, PenTool, Image, ImagePlus } from 'lucide-react';

export type TabType = 'social' | 'copywriting' | 'banner' | 'imageEdit';

interface TabsProps {
  activeTab: TabType;
  onTabChange: (tab: TabType) => void;
}

export const Tabs: FC<TabsProps> = ({ activeTab, onTabChange }) => {
  const tabs = [
    { id: 'social' as const, label: 'Social', icon: MessageSquare },
    { id: 'copywriting' as const, label: 'Copywriting', icon: PenTool },
    { id: 'banner' as const, label: 'Banner', icon: Image },
    { id: 'imageEdit' as const, label: 'Image Edit', icon: ImagePlus },
  ];

  return (
    <div className="flex gap-2 mb-6 border-b border-gray-200">
      {tabs.map(tab => {
        const Icon = tab.icon;
        return (
          <button
            key={tab.id}
            onClick={() => onTabChange(tab.id)}
            className={`flex items-center gap-2 px-6 py-3 font-medium transition-colors border-b-2 ${
              activeTab === tab.id
                ? 'border-indigo-blue text-indigo-blue bg-indigo-50'
                : 'border-transparent text-gray-600 hover:text-gray-900 hover:bg-gray-50'
            }`}
          >
            <Icon size={18} />
            {tab.label}
          </button>
        );
      })}
    </div>
  );
};
