#!/usr/bin/env python3

from src.card import Card
from src.poker_engine import PokerEngine

def test_preflop_decision():
    """Test a basic pre-flop decision."""
    # AKs in the button position
    hole_cards = [Card("Ah"), Card("Kh")]
    community_cards = []
    player_stacks = [1000, 1200, 800, 1500, 1300]  # 5th (last) stack is our player
    player_positions = ["utg", "mp", "co", "btn", "sb"]
    pot_size = 100
    facing_bet = 50
    
    engine = PokerEngine(num_simulations=1000)  # Reduced for quicker test
    decision = engine.process_game_state(
        hole_cards, 
        community_cards, 
        player_stacks, 
        player_positions, 
        pot_size, 
        facing_bet
    )
    
    print(f"AKs from SB facing 50 into pot of 100: {decision}")
    
def test_flop_decision():
    """Test a flop decision."""
    # AKs with top pair top kicker on flop
    hole_cards = [Card("Ah"), Card("Kh")]
    community_cards = [Card("Ad"), Card("7c"), Card("2s")]
    player_stacks = [950, 1150, 750, 1450, 1250]
    player_positions = ["utg", "mp", "co", "btn", "sb"]
    pot_size = 200
    facing_bet = 100
    
    engine = PokerEngine(num_simulations=1000)  # Reduced for quicker test
    decision = engine.process_game_state(
        hole_cards, 
        community_cards, 
        player_stacks, 
        player_positions, 
        pot_size, 
        facing_bet
    )
    
    print(f"AKs with TPTK on A72 rainbow flop facing 100 into pot of 200: {decision}")

if __name__ == "__main__":
    print("Running engine tests...")
    test_preflop_decision()
    test_flop_decision()
    print("Tests completed.")