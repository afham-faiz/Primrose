import { useState } from 'react';
import Home from './pages/home';
import DeckView from './pages/DeckView';
import StudyMode from './pages/StudyMode';

type Page = 'home' | 'deck' | 'study';

function App() {
  const [currentPage, setCurrentPage] = useState<Page>('home');

  const renderPage = () => {
    switch (currentPage) {
      case 'home':
        return <Home />;
      case 'deck':
        return <DeckView />;
      case 'study':
        return <StudyMode />;
      default:
        return <Home />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Simple Navigation */}
      <nav className="bg-white shadow-sm border-b">
        <div className="container mx-auto p-4">
          <div className="flex gap-6">
            <button
              onClick={() => setCurrentPage('home')}
              className={`font-semibold ${currentPage === 'home' ? 'text-blue-600' : 'text-gray-600'}`}
            >
              Home
            </button>
            <button
              onClick={() => setCurrentPage('deck')}
              className={`font-semibold ${currentPage === 'deck' ? 'text-blue-600' : 'text-gray-600'}`}
            >
              Deck View
            </button>
            <button
              onClick={() => setCurrentPage('study')}
              className={`font-semibold ${currentPage === 'study' ? 'text-blue-600' : 'text-gray-600'}`}
            >
              Study Mode
            </button>
          </div>
        </div>
      </nav>

      {/* Page Content */}
      <main>
        {renderPage()}
      </main>
    </div>
  );
}

export default App;