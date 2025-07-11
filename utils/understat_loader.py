from soccerdata import Understat

def get_understat_data(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    return Understat(
        leagues=leagues,
        seasons=seasons,
        proxy=proxy,
        no_cache=no_cache,
        no_store=no_store
    )

def load_schedule(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    data = get_understat_data(leagues, seasons, proxy, no_cache, no_store)
    return data.read_schedule()

def load_team_match_stats(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    data = get_understat_data(leagues, seasons, proxy, no_cache, no_store)
    return data.read_team_match_stats()

def load_player_season_stats(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    data = get_understat_data(leagues, seasons, proxy, no_cache, no_store)
    return data.read_player_season_stats()

def load_player_match_stats(match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    data = get_understat_data(leagues, seasons, proxy, no_cache, no_store)
    return data.read_player_match_stats(match_id=match_id)

def load_shot_events(match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    data = get_understat_data(leagues, seasons, proxy, no_cache, no_store)
    return data.read_shot_events(match_id=match_id)

def get_available_leagues():
    return Understat.available_leagues()
