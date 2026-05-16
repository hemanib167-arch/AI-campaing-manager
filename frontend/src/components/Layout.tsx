import type { FC, ReactNode } from 'react';
import { Plane } from 'lucide-react';

interface LayoutProps {
  children: ReactNode;
}

export const Layout: FC<LayoutProps> = ({ children }) => {
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="container mx-auto px-6 py-4">
          <div className="flex items-center gap-3">
            <Plane size={32} color="#1A1AAF" />
            <h1 className="text-2xl font-bold text-indigo-blue">6E Creative Studio</h1>
          </div>
        </div>
      </header>
      <main className="container mx-auto px-6 py-8">
        {children}
      </main>
    </div>
  );
};
