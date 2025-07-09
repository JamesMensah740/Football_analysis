from soccerdata import FotMob

def get_fotmob_data(leagues=["ENG-Premier League"], seasons=["2023-24"], proxy=None, no_cache=False, no_store=False):
    return FotMob(leagues=leagues, seasons=seasons, proxy=proxy, no_cache=no_cache, no_store=no_store)

def load_schedule(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fm = get_fotmob_data(leagues, seasons)
    return fm.read_schedule()

def load_league_table(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fm = get_fotmob_data(leagues, seasons)
    return fm.read_league_table()

def load_team_match_stats(stat_type="Top stats", opponent_stats=True, team=None, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fm = get_fotmob_data(leagues, seasons)
    return fm.read_team_match_stats(stat_type=stat_type, opponent_stats=opponent_stats, team=team)

def load_leagues(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fm = get_fotmob_data(leagues, seasons)
    return fm.read_leagues()

def load_seasons(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    fm = get_fotmob_data(leagues, seasons)
    return fm.read_seasons()

def get_available_leagues():
    return FotMob.available_leagues()
