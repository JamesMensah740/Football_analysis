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
#import utils.matchhistory_loader as matchhistory

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
    st.subheader("Coming soon: ESPN data view")
elif source == "Sofascore":
    st.subheader("Coming soon: Sofascore data view")
elif source == "WhoScored":
    st.subheader("Coming soon: WhoScored data view")
elif source == "FBref":
    st.subheader("Coming soon: FBref data view")
elif source == "FotMob":
    st.subheader("Coming soon: FotMob data view")
elif source == "Understat":
    st.subheader("Coming soon: Understat data view")
elif source == "SoFIFA":
    st.subheader("Coming soon: SoFIFA data view")
elif source == "Club Elo":
    st.subheader("Coming soon: Club Elo data view")
elif source == "MatchHistory":
    st.subheader("Coming soon: MatchHistory data view")
else:
    st.error("Please select a valid data source from the sidebar.")
    
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
        
        
