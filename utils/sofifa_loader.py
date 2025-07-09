from soccerdata import SoFIFA

def get_sofifa_data(leagues=["ENG-Premier League"], versions="latest", proxy=None, no_cache=False, no_store=False):
    return SoFIFA(leagues=leagues, versions=versions, proxy=proxy, no_cache=no_cache, no_store=no_store)

def load_leagues(leagues=["ENG-Premier League"], versions="latest"):
    sofifa = get_sofifa_data(leagues, versions)
    return sofifa.read_leagues()

def load_versions(max_age=1):
    sofifa = SoFIFA()
    return sofifa.read_versions(max_age=max_age)

def load_teams(leagues=["ENG-Premier League"], versions="latest"):
    sofifa = get_sofifa_data(leagues, versions)
    return sofifa.read_teams()

def load_players(team=None, leagues=["ENG-Premier League"], versions="latest"):
    sofifa = get_sofifa_data(leagues, versions)
    return sofifa.read_players(team=team)

def load_team_ratings(leagues=["ENG-Premier League"], versions="latest"):
    sofifa = get_sofifa_data(leagues, versions)
    return sofifa.read_team_ratings()

def load_player_ratings(team=None, player=None, leagues=["ENG-Premier League"], versions="latest"):
    sofifa = get_sofifa_data(leagues, versions)
    return sofifa.read_player_ratings(team=team, player=player)

def get_available_leagues():
    return SoFIFA.available_leagues()
