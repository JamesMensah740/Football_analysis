from soccerdata import ClubElo
import pandas as pd
from datetime import datetime

def get_clubelo_data(proxy=None, no_cache=False, no_store=False):
    return ClubElo(proxy=proxy, no_cache=no_cache, no_store=no_store)

def load_elo_by_date(date=None, proxy=None, no_cache=False, no_store=False):
    """
    Load ELO ratings for all teams on a specific date.
    If no date is passed, today's ELO ratings will be returned.
    """
    elo = get_clubelo_data(proxy=proxy, no_cache=no_cache, no_store=no_store)
    if date is None:
        date = datetime.today().strftime("%Y-%m-%d")
    return elo.read_by_date(date=date)

def load_team_elo_history(team_name, max_age=1, proxy=None, no_cache=False, no_store=False):
    """
    Load historical ELO ratings for a given club.
    """
    elo = get_clubelo_data(proxy=proxy, no_cache=no_cache, no_store=no_store)
    return elo.read_team_history(team=team_name, max_age=max_age)

def get_available_elo_leagues():
    return ClubElo.available_leagues()
