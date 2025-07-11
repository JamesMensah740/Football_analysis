import streamlit as st

# Load all loader modules
import utils.espn_loader as espn
import utils.sofascore_loader as sofa
import utils.whoscored_loader as ws
import utils.elo_loader as elo
import utils.fbref_loader as fbref
import utils.fotmob_loader as fotmob
import utils.sofifa_loader as sofifa
import utils.understat_loader as understat
import utils.matchhistory_loader as matchhistory

st.set_page_config(layout="wide", page_title="Football Data Hub")

# Title
st.title("⚽ Football Data Dashboard")

# Sidebar layout
st.sidebar.header("Data Source")
source = st.sidebar.selectbox("Choose data source", [
    "ESPN", "Sofascore", "WhoScored", "FBref", "FotMob",
    "Understat", "SoFIFA", "Club Elo", "MatchHistory"
])

# Placeholder for main display
st.markdown("---")
st.info(f"Select options from the sidebar to explore {source} data.")

# Dynamic content rendering (to be built)
if source == "ESPN":
    st.subheader("📊 ESPN Data Explorer")

    leagues = espn.get_available_espn_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023)", value="2023")

    data_type = st.sidebar.radio("Select Data Type", [
        "Schedule",
        "League Table"
        # "Team Match Stats"  # Uncomment if implemented
    ])

    espn_data = espn.get_espn_data(leagues=[selected_league], seasons=[selected_season])

    if data_type == "Schedule":
        df = espn_data.read_schedule()
        st.dataframe(df)

    elif data_type == "League Table":
        df = espn_data.read_league_table()
        st.dataframe(df)

    # elif data_type == "Team Match Stats":
    #     df = espn_data.read_team_match_stats()
    #     st.dataframe(df)
elif source == "Sofascore":
    st.subheader("📊 Sofascore Data Explorer")

    leagues = sofa.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    data_type = st.sidebar.radio("Select Data Type", [
        "League Table",
        "Schedule",
        "Team Match Stats"
    ])

    ss = sofa.get_sofascore_data(leagues=[selected_league], seasons=[selected_season])

    if data_type == "League Table":
        df = ss.read_league_table()
        st.dataframe(df)

    elif data_type == "Schedule":
        df = ss.read_schedule()
        st.dataframe(df)

    elif data_type == "Team Match Stats":
        stat_type = st.sidebar.selectbox("Stat Type", ["summary", "shots", "xG", "defense", "passing", "duels"])
        team = st.sidebar.text_input("Filter by Team (optional)", value="")
        df = ss.read_team_match_stats(stat_type=stat_type, team=team or None)
        st.dataframe(df)

elif source == "WhoScored":
    st.subheader("📊 WhoScored Data Explorer")

    leagues = ws.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    data_type = st.sidebar.radio("Select Data Type", [
        "Schedule",
        "League Table",
        "Team Match Stats",
        "Player Match Stats"
    ])

    wh = ws.get_whoscored_data(leagues=[selected_league], seasons=[selected_season])

    if data_type == "Schedule":
        df = wh.read_schedule()
        st.dataframe(df)

    elif data_type == "League Table":
        df = wh.read_league_table()
        st.dataframe(df)

    elif data_type == "Team Match Stats":
        stat_type = st.sidebar.selectbox("Stat Type", ["summary", "shots", "passes", "defense", "xG"])
        team = st.sidebar.text_input("Filter by Team (optional)", value="")
        df = wh.read_team_match_stats(stat_type=stat_type, team=team or None)
        st.dataframe(df)

    elif data_type == "Player Match Stats":
        match_id = st.sidebar.text_input("Match ID (optional)", value="")
        df = wh.read_player_match_stats(match_id=int(match_id) if match_id else None)
        st.dataframe(df)


elif source == "FotMob":
    st.subheader("📊 FotMob Data Explorer")

    leagues = fotmob.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    data_type = st.sidebar.radio("Select Data Type", [
        "League Table",
        "Schedule",
        "Team Match Stats"
    ])

    # Create FotMob instance
    ft = fotmob.get_fotmob_data(leagues=[selected_league], seasons=[selected_season])

    if data_type == "League Table":
        force_cache = st.sidebar.checkbox("Use cache", value=False)
        df = ft.read_league_table(force_cache=force_cache)
        st.dataframe(df)

    elif data_type == "Schedule":
        force_cache = st.sidebar.checkbox("Use cache", value=False)
        df = ft.read_schedule(force_cache=force_cache)
        st.dataframe(df)

    elif data_type == "Team Match Stats":
        stat_type = st.sidebar.selectbox("Stat Type", [
            "Top stats", "Shots", "Expected goals (xG)", "Passes", 
            "Defence", "Duels", "Discipline"
        ])
        opp_stats = st.sidebar.checkbox("Include Opponent Stats", value=True)
        team_filter = st.sidebar.text_input("Filter by Team (optional)", value="")

        df = ft.read_team_match_stats(
            stat_type=stat_type,
            opponent_stats=opp_stats,
            team=team_filter or None
        )
        st.dataframe(df)
    st.subheader("Coming soon: FotMob data view")
    
elif source == "Understat":
    st.subheader("📊 Understat Data Explorer")

    leagues = understat.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    us = understat.get_understat_data(leagues=[selected_league], seasons=[selected_season])

    data_type = st.sidebar.radio("Select Data Type", [
        "Schedule",
        "Team Match Stats",
        "Player Season Stats",
        "Player Match Stats",
        "Shot Events"
    ])

    if data_type == "Schedule":
        include_all = st.sidebar.checkbox("Include matches without full data?", value=True)
        df = us.read_schedule(include_matches_without_data=include_all)
        st.dataframe(df)

    elif data_type == "Team Match Stats":
        df = us.read_team_match_stats()
        st.dataframe(df)

    elif data_type == "Player Season Stats":
        df = us.read_player_season_stats()
        st.dataframe(df)

    elif data_type == "Player Match Stats":
        match_id = st.sidebar.text_input("Match ID (optional)", value="")
        df = us.read_player_match_stats(match_id=int(match_id) if match_id else None)
        st.dataframe(df)

    elif data_type == "Shot Events":
        match_id = st.sidebar.text_input("Match ID (optional)", value="")
        df = us.read_shot_events(match_id=int(match_id) if match_id else None)
        st.dataframe(df)
    st.subheader("Coming soon: Understat data view")
    
elif source == "SoFIFA":
    st.subheader("📊 SoFIFA Data Explorer")

    leagues = sofifa.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)

    version_option = st.sidebar.selectbox("Select FIFA Version", ["latest", "all", "Custom ID"])
    if version_option == "Custom ID":
        custom_version = st.sidebar.text_input("Enter Version ID (e.g. 230034)", value="230034")
        versions = custom_version
    else:
        versions = version_option

    sf = sofifa.get_sofifa_data(leagues=[selected_league], versions=versions)

    data_type = st.sidebar.radio("Select Data Type", [
        "Players",
        "Teams",
        "Team Ratings",
        "Player Ratings"
    ])

    if data_type == "Players":
        team_filter = st.sidebar.text_input("Filter by Team (optional)", value="")
        df = sf.read_players(team=team_filter or None)
        st.dataframe(df)

    elif data_type == "Teams":
        df = sf.read_teams()
        st.dataframe(df)

    elif data_type == "Team Ratings":
        df = sf.read_team_ratings()
        st.dataframe(df)

    elif data_type == "Player Ratings":
        team_filter = st.sidebar.text_input("Filter by Team (optional)", value="")
        player_filter = st.sidebar.text_input("Filter by Player ID (optional)", value="")
        df = sf.read_player_ratings(
            team=team_filter or None,
            player=int(player_filter) if player_filter else None
        )
        st.dataframe(df)

    st.subheader("Coming soon: SoFIFA data view")
    
elif source == "Club Elo":
    st.subheader("📈 Club Elo Ratings")

    elo_obj = elo.get_elo_data()

    view = st.sidebar.radio("Choose View", ["Ratings by Date", "Team Elo History"])

    if view == "Ratings by Date":
        selected_date = st.sidebar.date_input("Select Date", value=None)
        if st.button("Load Ratings"):
            df = elo_obj.read_by_date(date=selected_date if selected_date else None)
            st.dataframe(df)

    elif view == "Team Elo History":
        team_name = st.sidebar.text_input("Enter Team Name (e.g., Manchester City)")
        if st.button("Load History") and team_name:
            df = elo_obj.read_team_history(team=team_name)
            st.dataframe(df)
    elif view == "Player Ratings":
    # Placeholder for Player Ratings
    # This section can be expanded later to include player ratings from Club Elo
        st.subheader("Coming soon: Player Ratings")

elif source == "MatchHistory":
    st.subheader("📂 MatchHistory Data")

    leagues = matchhistory.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    if st.button("Load MatchHistory Data"):
        match_data_df = matchhistory.load_match_data(leagues=[selected_league], seasons=[selected_season])
        st.dataframe(match_data_df)

    
# League and season selection (per source)
if source == "ESPN":
    leagues = espn.get_available_espn_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023)", value="2023")

    if st.button("Load ESPN Schedule"):
        schedule_df = espn.load_espn_schedule(leagues=[selected_league], seasons=[selected_season])
        st.dataframe(schedule_df)

elif source == "Sofascore":
    leagues = sofa.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    if st.button("Load Sofascore Table"):
        table_df = sofa.load_league_table(leagues=[selected_league], seasons=[selected_season])
        st.dataframe(table_df)
        
elif source == "WhoScored":
    leagues = ws.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    if st.button("Load WhoScored Schedule"):
        schedule_df = ws.load_schedule(leagues=[selected_league], seasons=[selected_season])
        st.dataframe(schedule_df)

elif source == "FBref":
    st.subheader("📊 FBref Data Explorer")

    # 1. Select League and Season
    leagues = fbref.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season", value="2023-24")

    # 2. Select Data Type
    data_type = st.sidebar.radio("Select Data Type", [
        "Team Season Stats", 
        "Team Match Stats", 
        "Player Season Stats", 
        "Player Match Stats", 
        "Schedule", 
        "Events", 
        "Lineups", 
        "Shot Events"
    ])

    # 3. Shared setup
    fb = fbref.get_fbref_data(leagues=[selected_league], seasons=[selected_season])

    if data_type == "Team Season Stats":
        stat_type = st.sidebar.selectbox("Stat Type", [
            "standard", "keeper", "keeper_adv", "shooting", "passing", "passing_types",
            "goal_shot_creation", "defense", "possession", "playing_time", "misc"
        ])
        opp = st.sidebar.checkbox("Include Opponent Stats", value=False)

        df = fb.read_team_season_stats(stat_type=stat_type, opponent_stats=opp)
        st.dataframe(df)

    elif data_type == "Team Match Stats":
        stat_type = st.sidebar.selectbox("Stat Type", [
            "schedule", "keeper", "shooting", "passing", "passing_types", 
            "goal_shot_creation", "defense", "possession", "misc"
        ])
        team = st.sidebar.text_input("Filter by Team (optional)")
        opp = st.sidebar.checkbox("Include Opponent Stats", value=False)

        df = fb.read_team_match_stats(stat_type=stat_type, opponent_stats=opp, team=team or None)
        st.dataframe(df)

    elif data_type == "Player Season Stats":
        stat_type = st.sidebar.selectbox("Stat Type", [
            "standard", "shooting", "passing", "passing_types", "goal_shot_creation",
            "defense", "possession", "playing_time", "misc", "keeper", "keeper_adv"
        ])
        df = fb.read_player_season_stats(stat_type=stat_type)
        st.dataframe(df)

    elif data_type == "Player Match Stats":
        stat_type = st.sidebar.selectbox("Stat Type", [
            "summary", "keepers", "passing", "passing_types", "defense", 
            "possession", "misc"
        ])
        match_id = st.sidebar.text_input("Match ID (optional)", value="")
        df = fb.read_player_match_stats(stat_type=stat_type, match_id=int(match_id) if match_id else None)
        st.dataframe(df)

    elif data_type == "Schedule":
        df = fb.read_schedule()
        st.dataframe(df)

    elif data_type == "Lineups":
        match_id = st.sidebar.text_input("Match ID (optional)", value="")
        df = fb.read_lineup(match_id=int(match_id) if match_id else None)
        st.dataframe(df)

    elif data_type == "Events":
        match_id = st.sidebar.text_input("Match ID (optional)", value="")
        df = fb.read_events(match_id=int(match_id) if match_id else None)
        st.dataframe(df)

    elif data_type == "Shot Events":
        match_id = st.sidebar.text_input("Match ID (optional)", value="")
        df = fb.read_shot_events(match_id=int(match_id) if match_id else None)
        st.dataframe(df)

elif source == "FotMob":
    leagues = fotmob.get_available_leagues()
    selected_league = st.sidebar.selectbox("Select League", leagues)
    selected_season = st.sidebar.text_input("Enter Season (e.g. 2023-24)", value="2023-24")

    if st.button("Load FotMob Schedule"):
        schedule_df = fotmob.load_schedule(leagues=[selected_league], seasons=[selected_season])
        st.dataframe(schedule_df)
        
        
