from soccerdata import FBref

def get_fbref_data(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    return FBref(leagues=leagues, seasons=seasons, proxy=proxy, no_cache=no_cache, no_store=no_store)

def load_schedule(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_schedule()

def load_team_season_stats(stat_type='standard', opponent_stats=False, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_team_season_stats(stat_type=stat_type, opponent_stats=opponent_stats)

def load_team_match_stats(stat_type='schedule', opponent_stats=False, team=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_team_match_stats(stat_type=stat_type, opponent_stats=opponent_stats, team=team)

def load_player_season_stats(stat_type='standard', leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_player_season_stats(stat_type=stat_type)

def load_player_match_stats(stat_type='summary', match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_player_match_stats(stat_type=stat_type, match_id=match_id)

def load_lineup(match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_lineup(match_id=match_id)

def load_events(match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_events(match_id=match_id)

def load_shot_events(match_id=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fb = get_fbref_data(leagues, seasons)
    return fb.read_shot_events(match_id=match_id)

def get_available_leagues():
    return FBref.available_leagues()
