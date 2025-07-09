from soccerdata import MatchHistory

def get_matchhistory_data(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    return MatchHistory(leagues=leagues, seasons=seasons, proxy=proxy, no_cache=no_cache, no_store=no_store)

def load_games(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    mh = get_matchhistory_data(leagues, seasons)
    return mh.read_games()

def get_available_leagues():
    return MatchHistory.available_leagues()
