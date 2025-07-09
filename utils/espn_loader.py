from soccerdata import ESPN

def get_espn_data(leagues=["ENG-Premier League"], seasons=["2023"]):
    return ESPN(leagues=leagues, seasons=seasons)

def load_espn_schedule(leagues=["ENG-Premier League"], seasons=["2023"]):
    espn = get_espn_data(leagues, seasons)
    return espn.read_schedule()

def load_matchsheet(match_id, leagues=["ENG-Premier League"], seasons=["2023"]):
    espn = get_espn_data(leagues, seasons)
    return espn.read_matchsheet(match_id=match_id)

def load_lineup(match_id, leagues=["ENG-Premier League"], seasons=["2023"]):
    espn = get_espn_data(leagues, seasons)
    return espn.read_lineup(match_id=match_id)

def get_available_espn_leagues():
    return ESPN.available_leagues()