import { useState } from 'react';
import type { Card } from '../types';

function StudyMode() {
  const [cards] = useState<Card[]>([
    { id: '1', front: 'Stack', back: 'last in, first out data structure', difficulty: 0.5 },
    { id: '2', front: 'Queue', back: 'first in, first out data structure', difficulty: 0.5 },
  ]);
  
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showAnswer, setShowAnswer] = useState(false);

  const currentCard = cards[currentIndex];

  const handleNext = () => {
    if (currentIndex < cards.length - 1) {
      setCurrentIndex(currentIndex + 1);
      setShowAnswer(false);
    }
  };

  const handleDifficulty = (difficulty: 'easy' | 'medium' | 'hard') => {
    // This will later update the spaced repetition algorithm
    console.log(`Marked as ${difficulty}`);
    handleNext();
  };

  if (!currentCard) {
    return <div className="container mx-auto p-6">No cards to study!</div>;
  }

  return (
    <div className="container mx-auto p-6 max-w-2xl">
      <div className="mb-4 text-sm text-gray-600">
        Card {currentIndex + 1} of {cards.length}
      </div>

      <div className="border rounded-lg p-12 text-center min-h-[300px] flex flex-col justify-center">
        <div className="text-2xl mb-4">{currentCard.front}</div>
        
        {showAnswer && (
          <div className="text-xl text-gray-700 mt-4 pt-4 border-t">
            {currentCard.back}
          </div>
        )}
      </div>

      {!showAnswer ? (
        <button
          onClick={() => setShowAnswer(true)}
          className="w-full mt-6 bg-blue-500 text-white py-3 rounded hover:bg-blue-600"
        >
          Show Answer
        </button>
      ) : (
        <div className="mt-6 grid grid-cols-3 gap-4">
          <button
            onClick={() => handleDifficulty('hard')}
            className="bg-red-500 text-white py-3 rounded hover:bg-red-600"
          >
            Hard
          </button>
          <button
            onClick={() => handleDifficulty('medium')}
            className="bg-yellow-500 text-white py-3 rounded hover:bg-yellow-600"
          >
            Medium
          </button>
          <button
            onClick={() => handleDifficulty('easy')}
            className="bg-green-500 text-white py-3 rounded hover:bg-green-600"
          >
            Easy
          </button>
        </div>
      )}
    </div>
  );
}

export default StudyMode;