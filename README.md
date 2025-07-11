# ⚽ Football Data Hub

A Streamlit-powered dashboard for exploring rich football datasets from multiple trusted sources.

## 📊 Data Sources Integrated

- **FBref**: Comprehensive team & player statistics (match/season), events, lineups, xG.
- **Understat** (planned): Detailed xG & player-level shot data.
- **Club Elo** (planned): Global club ratings and performance trends.
- **WhoScored**, **Sofascore**, **FotMob** (planned): Match stats, player ratings, fixtures.
- **SoFIFA** (planned): Player ratings, potential, and team stats from FIFA games.
- **MatchHistory** (TBD): Historical match analytics.

## 🛠 Features
- Interactive dashboard with source-based views.
- League and season selectors.
- Detailed stat filters (team/player, match/season, events, xG).
- Clean layout powered by Streamlit.

##  Getting Started

 ##  How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/JamesMensah740/Football_analysis.git
cd Football_analysis

python -m venv .venv
source .venv/bin/activate     # On Windows: .venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

file structure 
Football_analysis/
│
├── app.py                      # Main Streamlit app
├── requirements.txt            # Python dependencies
├── .gitignore
├── utils/                      # Modular data loaders
│   ├── fbref_loader.py
│   ├── whoscored_loader.py
│   ├── ...
└── README.md                   # You are here
