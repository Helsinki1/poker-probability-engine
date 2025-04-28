# Poker Probability Engine

A command-line tool and web application that provides GTO (Game Theory Optimal) poker decision recommendations for Texas Hold'em. This engine calculates optimal decisions based on your hole cards, community cards, player positions, stack sizes, and the current game state.

## Features

- GTO-based decision making using Monte Carlo simulations
- Supports all Texas Hold'em game stages (pre-flop, flop, turn, river)
- Accounts for player positions, stack sizes, and bet sizing
- Provides actionable recommendations (call, fold, raise with specific amount)
- Optimized for 5-player games
- Available as both command-line tool and web application

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/prob-engine.git
cd prob-engine

# Install dependencies
pip install -r requirements.txt

# Make the main script executable
chmod +x main.py
```

## Usage

### Web Application

```bash
# Start the web server
python app.py
```

Then open your browser and navigate to `http://localhost:5000`

### Command-Line Tool

```bash
./main.py --hole-cards "Ah Ks" --community-cards "Qh Jh Td" --stacks "1000 1200 800 1500 1300" --positions "utg mp co btn sb" --pot-size 300 --facing-bet 150
```

### Arguments

- `--hole-cards`: Your two hole cards (required)
- `--community-cards`: The community cards (optional)
- `--stacks`: Chip stacks for all 5 players (required)
- `--positions`: Positions for all 5 players (required)
- `--pot-size`: Current pot size (required)
- `--facing-bet`: Size of bet you are facing (optional)
- `--min-raise`: Minimum raise size if applicable (optional)
- `--simulations`: Number of Monte Carlo simulations to run (optional, default=5000)

### Example

```bash
# Pre-flop decision with Ace-King suited in late position
./main.py --hole-cards "Ah Kh" --stacks "1000 1200 800 1500 1300" --positions "utg mp co btn sb" --pot-size 100 --facing-bet 50

# Flop decision with top pair top kicker
./main.py --hole-cards "Ah Kh" --community-cards "Ad 7c 2s" --stacks "950 1150 750 1450 1250" --positions "utg mp co btn sb" --pot-size 200 --facing-bet 100
```

## Position Abbreviations

- `utg`: Under the Gun (first to act pre-flop)
- `utg+1`: Under the Gun+1
- `mp`: Middle Position
- `mp+1`: Middle Position+1
- `hj`: Hijack
- `co`: Cutoff
- `btn`: Button
- `sb`: Small Blind
- `bb`: Big Blind

## Note on Accuracy

The engine uses Monte Carlo simulations to estimate hand equity. Increasing the number of simulations will improve accuracy at the cost of longer calculation time. The default of 5000 simulations provides a good balance between accuracy and performance.