// Define the shape of our data
export interface Card {
  id: string;
  front: string;
  back: string;
  lastReviewed?: Date;
  nextReview?: Date;
  difficulty: number; // 0-1, affects spacing algorithm
}

export interface Deck {
  id: string;
  name: string;
  description: string;
  cards: Card[];
  createdAt: Date;
  lastStudied?: Date;
}

export interface User {
  id: string;
  username: string;
  email: string;
  decks: Deck[];
}