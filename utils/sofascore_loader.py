from soccerdata import Sofascore

def get_sofascore_data(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    return Sofascore(leagues=leagues, seasons=seasons)

def load_league_table(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    sofa = get_sofascore_data(leagues, seasons)
    return sofa.read_league_table()

def load_schedule(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    sofa = get_sofascore_data(leagues, seasons)
    return sofa.read_schedule()
