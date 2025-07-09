from soccerdata import WhoScored

def get_whoscored_data(
    leagues=["ENG-Premier League"],
    seasons=["2023-24"],
    headless=True,
    proxy=None
):
    return WhoScored(
        leagues=leagues,
        seasons=seasons,
        headless=headless,
        proxy=proxy
    )

def load_schedule(leagues=["ENG-Premier League"], seasons=["2023-24"]):
    ws = get_whoscored_data(leagues, seasons)
    return ws.read_schedule()

def load_missing_players(match_id, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    ws = get_whoscored_data(leagues, seasons)
    return ws.read_missing_players(match_id=match_id)

def load_events(match_id, output_fmt="events", leagues=["ENG-Premier League"], seasons=["2023-24"]):
    ws = get_whoscored_data(leagues, seasons)
    return ws.read_events(match_id=match_id, output_fmt=output_fmt)

def load_player_match_stats(match_id, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    ws = get_whoscored_data(leagues, seasons)
    return ws.read_player_match_stats(match_id=match_id)

def load_shot_events(match_id, leagues=["ENG-Premier League"], seasons=["2023-24"]):
    ws = get_whoscored_data(leagues, seasons)
    return ws.read_shot_events(match_id=match_id)

def get_available_leagues():
    return WhoScored.available_leagues()
