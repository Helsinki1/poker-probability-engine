from itertools import combinations
from src.card import Card

class HandEvaluator:
    """Evaluates poker hands."""
    
    # Hand rankings from highest to lowest
    HAND_RANKINGS = [
        "straight_flush",
        "four_of_a_kind",
        "full_house",
        "flush",
        "straight",
        "three_of_a_kind",
        "two_pair",
        "one_pair",
        "high_card"
    ]
    
    @staticmethod
    def evaluate_hand(hole_cards, community_cards):
        """Evaluate the best 5-card hand from hole cards and community cards."""
        all_cards = hole_cards + community_cards
        best_hand = None
        best_hand_value = float('-inf')
        
        for hand in combinations(all_cards, 5):
            hand_value = HandEvaluator._evaluate_five_card_hand(hand)
            if hand_value > best_hand_value:
                best_hand = hand
                best_hand_value = hand_value
        
        return best_hand, best_hand_value
    
    @staticmethod
    def _evaluate_five_card_hand(hand):
        """Evaluate a 5-card poker hand."""
        ranks = [card.rank for card in hand]
        suits = [card.suit for card in hand]
        rank_values = [card.rank_value for card in hand]
        rank_counts = {}
        
        for rank in ranks:
            if rank in rank_counts:
                rank_counts[rank] += 1
            else:
                rank_counts[rank] = 1
        
        # Check for straight flush
        if len(set(suits)) == 1 and HandEvaluator._is_straight(rank_values):
            return 9000 + max(rank_values)
        
        # Check for four of a kind
        if 4 in rank_counts.values():
            four_rank = next(r for r, count in rank_counts.items() if count == 4)
            kicker = next(r for r in ranks if r != four_rank)
            return 8000 + Card.RANKS.index(four_rank) * 20 + Card.RANKS.index(kicker)
        
        # Check for full house
        if 3 in rank_counts.values() and 2 in rank_counts.values():
            three_rank = next(r for r, count in rank_counts.items() if count == 3)
            two_rank = next(r for r, count in rank_counts.items() if count == 2)
            return 7000 + Card.RANKS.index(three_rank) * 20 + Card.RANKS.index(two_rank)
        
        # Check for flush
        if len(set(suits)) == 1:
            return 6000 + sum(Card.RANKS.index(r) for r in ranks)
        
        # Check for straight
        if HandEvaluator._is_straight(rank_values):
            return 5000 + max(rank_values)
        
        # Check for three of a kind
        if 3 in rank_counts.values():
            three_rank = next(r for r, count in rank_counts.items() if count == 3)
            kickers = sorted([Card.RANKS.index(r) for r in ranks if r != three_rank], reverse=True)
            return 4000 + Card.RANKS.index(three_rank) * 400 + kickers[0] * 20 + kickers[1]
        
        # Check for two pair
        if list(rank_counts.values()).count(2) == 2:
            pairs = sorted([Card.RANKS.index(r) for r, count in rank_counts.items() if count == 2], reverse=True)
            kicker = next(Card.RANKS.index(r) for r, count in rank_counts.items() if count == 1)
            return 3000 + pairs[0] * 400 + pairs[1] * 20 + kicker
        
        # Check for one pair
        if 2 in rank_counts.values():
            pair_rank = next(r for r, count in rank_counts.items() if count == 2)
            kickers = sorted([Card.RANKS.index(r) for r in ranks if r != pair_rank], reverse=True)
            return 2000 + Card.RANKS.index(pair_rank) * 1000 + kickers[0] * 100 + kickers[1] * 10 + kickers[2]
        
        # High card
        sorted_values = sorted(rank_values, reverse=True)
        return 1000 + sorted_values[0] * 1000 + sorted_values[1] * 100 + sorted_values[2] * 10 + sorted_values[3] * 1 + sorted_values[4] * 0.1
    
    @staticmethod
    def _is_straight(rank_values):
        """Check if the hand is a straight."""
        sorted_values = sorted(rank_values)
        return (len(set(sorted_values)) == 5 and max(sorted_values) - min(sorted_values) == 4) or \
               (sorted_values == [0, 1, 2, 3, 12])  # A-2-3-4-5 straight