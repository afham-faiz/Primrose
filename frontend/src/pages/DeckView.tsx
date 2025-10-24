import { useState } from 'react';
import type { Card } from '../types';

function DeckView() {
  const [cards, /*setCards*/] = useState<Card[]>([
    {
      id: '1',
      front: 'Stack',
      back: 'last in, first out data structure',
      difficulty: 0.5,
    },
    {
      id: '2',
      front: 'queue',
      back: 'first in, first out data structure',
      difficulty: 0.5,
    },
  ]);

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Data Structures</h1>

      <div className="mb-4 flex gap-4">
        <button className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
          Study All
        </button>
        <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          + Add Card
        </button>
      </div>

      <div className="space-y-2">
        {cards.map((card) => (
          <div key={card.id} className="border rounded p-4 flex justify-between items-center">
            <div>
              <span className="font-medium">{card.front}</span>
              <span className="mx-4">→</span>
              <span className="text-gray-600">{card.back}</span>
            </div>
            <button className="text-red-500 hover:text-red-700">Delete</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DeckView;