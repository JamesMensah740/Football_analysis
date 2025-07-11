from soccerdata import ClubElo
from datetime import datetime
from typing import Optional, Union
import pandas as pd


def get_elo_data(proxy=None, no_cache=False, no_store=False) -> ClubElo:
    """
    Initialize the ClubElo data loader.
    """
    return ClubElo(proxy=proxy, no_cache=no_cache, no_store=no_store)


def load_elo_by_date(
    date: Optional[Union[str, datetime]] = None,
    proxy=None,
    no_cache=False,
    no_store=False,
) -> pd.DataFrame:
    """
    Load Elo ratings for all clubs on a specific date.
    If no date is provided, today's ratings will be used.
    """
    elo = get_elo_data(proxy=proxy, no_cache=no_cache, no_store=no_store)

    if date is None:
        date = datetime.today().strftime("%Y-%m-%d")

    return elo.read_by_date(date=date)


def load_team_elo_history(
    team_name: str,
    max_age: int = 1,
    proxy=None,
    no_cache=False,
    no_store=False,
) -> pd.DataFrame:
    """
    Load full Elo history for a given team.
    """
    elo = get_elo_data(proxy=proxy, no_cache=no_cache, no_store=no_store)
    return elo.read_team_history(team=team_name, max_age=max_age)


def get_available_elo_leagues() -> list[str]:
    """
    Return list of league IDs supported by Club Elo.
    """
    return ClubElo.available_leagues()
