from soccerdata import Understat

def get_understat_data(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    return Understat(leagues=leagues, seasons=seasons, proxy=proxy, no_cache=no_cache, no_store=no_store)

def load_schedule(leagues=["ENG-Premier League"], seasons=["2023-24"], include_matches_without_data=True):
    us = get_understat_data(leagues, seasons)
    return us.read_schedule(include_matches_without_data=include_matches_without_data)

def load_team_match_stats(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    us = get_understat_data(leagues, seasons)
    return us.read_team_match_stats()

def load_player_season_stats(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    us = get_understat_data(leagues, seasons)
    return us.read_player_season_stats()

def load_player_match_stats(match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    us = get_understat_data(leagues, seasons)
    return us.read_player_match_stats(match_id=match_id)

def load_shot_events(match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    us = get_understat_data(leagues, seasons)
    return us.read_shot_events(match_id=match_id)

def load_leagues(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    us = get_understat_data(leagues, seasons)
    return us.read_leagues()

def load_seasons(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    us = get_understat_data(leagues, seasons)
    return us.read_seasons()

def get_available_leagues():
    return Understat.available_leagues()
