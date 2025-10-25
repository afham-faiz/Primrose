import { useState } from 'react';
import type { Deck } from '../types';

function Home() {
  const [decks] = useState<Deck[]>([
    {
      id: '1',
      name: 'Stack',
      description: 'last in, first out data structure',
      cards: [],
      createdAt: new Date(),
    },
    {
      id: '2',
      name: 'Queue',
      description: 'first in, first out data structure',
      cards: [],
      createdAt: new Date(),
    },
  ]);

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">My Decks</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {decks.map((deck) => (
          <div
            key={deck.id}
            className="border rounded-lg p-4 hover:shadow-lg transition-shadow cursor-pointer"
          >
            <h2 className="text-xl font-semibold mb-2">{deck.name}</h2>
            <p className="text-gray-600 mb-4">{deck.description}</p>
            <div className="flex justify-between text-sm text-gray-500">
              <span>{deck.cards.length} cards</span>
              <span>Study →</span>
            </div>
          </div>
        ))}
      </div>

      <button className="mt-6 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        + Create New Deck
      </button>
    </div>
  );
}

export default Home;  