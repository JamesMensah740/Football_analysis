from soccerdata import MatchHistory

def get_matchhistory_data(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    """
    Initialize MatchHistory object with selected leagues and seasons.
    """
    return MatchHistory(
        leagues=leagues,
        seasons=seasons,
        proxy=proxy,
        no_cache=no_cache,
        no_store=no_store
    )

def load_match_data(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    """
    Load match-level game data from MatchHistory source.
    """
    mh = get_matchhistory_data(leagues, seasons, proxy, no_cache, no_store)
    return mh.read_games()

def get_available_leagues():
    """
    Return a list of available leagues for MatchHistory.
    """
    return MatchHistory.available_leagues()
