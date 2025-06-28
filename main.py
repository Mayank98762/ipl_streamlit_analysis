import streamlit as st 
import pandas as pd 

import matplotlib.pyplot as plt
import seaborn as sns


import wins as w 

deliveries=pd.read_csv("deliveries.csv")
matches=pd.read_csv("matches.csv")  
matches['team1'] = matches['team1'].str.replace('Rising Pune Supergiants', 'Rising Pune Supergiant')
matches['team2'] = matches['team2'].str.replace('Rising Pune Supergiants', 'Rising Pune Supergiant')
deliveries.rename(columns={'match_id': 'id'}, inplace=True)
# --- Futuristic CSS Styling ---
st.markdown(
    """
    <style>
    /* Futuristic background gradient */
    body, .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%) !important;
        color: #e0e0e0 !important;
    }
    /* Remove white gap at top */
    header[data-testid="stHeader"] {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%) !important;
        box-shadow: none !important;
        min-height: 0px !important;
        height: 0px !important;
        border: none !important;
    }
    /* Hide Streamlit top-right header buttons except sidebar nav */
    header[data-testid="stHeader"] div[role="button"]:not([aria-label*="menu"]) {
        position: fixed !important;
        bottom: 10px !important;
        right: 20px !important;
        z-index: 9999 !important;
        display: block !important;
        opacity: 0.8;;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #232526 0%, #414345 100%) !important;
        color: #e0e0e0 !important;
        border-right: 2px solid #00ffe7;
        box-shadow: 2px 0 10px #00ffe7;
    }
    /* Sidebar text and radio/option color fix */
    [data-testid="stSidebar"] * {
        color: #e0e0e0 !important;
    }
    .stRadio label, .stSelectbox label, .stSidebar .st-bb, .stSidebar .st-c3, .stSidebar .st-c4 {
        color: #e0e0e0 !important;
    }
    /* Title styling */
    .stTitle, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #00ffe7 !important;
        text-shadow: 0 0 10px #00ffe7, 0 0 20px #00ffe7;
        letter-spacing: 2px;
    }
    /* Subheader styling */
    .stMarkdown h2, .stMarkdown h3 {
        color: #39ff14 !important;
        text-shadow: 0 0 8px #39ff14;
    }
    /* Dataframe styling */
    .stDataFrame, .stTable {
        background: rgba(20, 30, 48, 0.95) !important;
        border-radius: 10px;
        border: 1px solid #00ffe7;
        color: #e0e0e0 !important;
        box-shadow: 0 0 20px #00ffe733;
    }
    /* Button styling */
    button, .stButton>button {
        background: linear-gradient(90deg, #00ffe7 0%, #39ff14 100%) !important;
        color: #232526 !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold;
        box-shadow: 0 0 10px #00ffe7;
        transition: 0.2s;
    }
    button:hover, .stButton>button:hover {
        background: linear-gradient(90deg, #39ff14 0%, #00ffe7 100%) !important;
        color: #fff !important;
        box-shadow: 0 0 20px #39ff14;
    }
    /* Selectbox styling */
    .stSelectbox>div>div {
        background: #232526 !important;
        color: #00ffe7 !important;
        border: 1px solid #00ffe7 !important;
        border-radius: 8px !important;
    }
    /* Dropdown menu styling for selectbox */
    .stSelectbox [data-baseweb="select"] > div {
        background: #232526 !important;
        color: #00ffe7 !important;
        border: 1px solid #00ffe7 !important;
        border-radius: 8px !important;
        box-shadow: 0 0 10px #00ffe744;
    }
    .stSelectbox [data-baseweb="select"] .css-1n76uvr-option {
        background: #232526 !important;
        color: #00ffe7 !important;
    }
    .stSelectbox [data-baseweb="select"] .css-1n76uvr-option[aria-selected="true"] {
        background: #00ffe7 !important;
        color: #232526 !important;
    }
    .stSelectbox [data-baseweb="select"] .css-1n76uvr-option:hover {
        background: #39ff14 !important;
        color: #232526 !important;
    }
    /* Radio styling */
    .stRadio>div {
        background: #232526 !important;
        color: #00ffe7 !important;
        border-radius: 8px !important;
        border: 1px solid #00ffe7 !important;
    }
    /* Chart backgrounds */
    .stPlotlyChart, .stAltairChart, .stVegaLiteChart, .stPyplotGlobalChart {
        background: #181c20 !important;
        border-radius: 10px;
        box-shadow: 0 0 20px #00ffe733;
    }
    /* General text */
    .stMarkdown p, .stMarkdown span, .stMarkdown div {
        color: #e0e0e0 !important;
    }
    /* Move sidebar collapse button to bottom-left */
    section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
        position: fixed !important;
        bottom: 10px !important;
        left: 10px !important;
        z-index: 9999 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("IPL Analysis")
st.sidebar.image("IPL.png", use_container_width=True)
#.dataframe(deliveries.head())
user_menu=st.sidebar.radio(
    "Select an option",
    ("Total Wins", "Team-Wise Analysis", "Season-Wise Analysis", "Player Performance","Strike Rates","Toss-Win Analysis","Best Partnerships")
)

if user_menu == "Total Wins":
    st.subheader("Total Wins by Each Team")
    win=w.total_wins(matches)
    st.dataframe(win)
    total=w.matches_won(matches)
    
    if st.sidebar.button("Total Matches Won by Each Team"):
        st.subheader("Total Matches Won by Each Team")
        teams= total['Teams']
        wins= total['Total Matches Won']
        plt.figure(figsize=(10, 6))
        plt.bar(teams, wins, color='blue')
        plt.xlabel('Teams')
        plt.ylabel('Total Matches Won') 
        
        plt.xticks(rotation=90)
        st.pyplot(plt)

elif user_menu == "Team-Wise Analysis":
    st.subheader("Team-Wise Analysis")
    team_name = st.sidebar.selectbox("Select a Team", matches['team1'].unique())
    
    if team_name:
        team_matches = matches[(matches['team1'] == team_name) | (matches['team2'] == team_name)]
        
        if not team_matches.empty:
            wins = team_matches[team_matches['winner'] == team_name].shape[0]
            losses = team_matches.shape[0] - wins

            # Pie chart with actual numbers
            labels = ['Wins', 'Losses']
            sizes = [wins, losses]
            colors = ['#4CAF50', '#F44336']
            def make_autopct(values):
                def my_autopct(pct):
                    total = sum(values)
                    val = int(round(pct*total/100.0))
                    return f'{pct:.1f}%\n({val})'
                return my_autopct
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, colors=colors, autopct=make_autopct(sizes), startangle=90)
            ax.axis('equal')
            plt.title(f"{team_name} - Wins vs Losses")
            st.pyplot(fig)


elif user_menu == "Season-Wise Analysis":
    st.subheader("Season-Wise Analysis")
    user_menu=st.sidebar.radio("Select one option",("Number of Wins","Number of Matches played at each venue", "Number of Matches Played in a City","Player which became Player of the Match most"))
    st.sidebar.header("Please select a season to analyze")
    season = st.sidebar.selectbox("Select a Season", matches['season'].unique())
    
    if user_menu=='Number of Wins':
        st.sidebar.header("Please select a team to analyze")
        team= st.sidebar.selectbox("Select a Team for Season Analysis", matches['team1'].unique())
        st.subheader(f"Number of Wins by {team} in {season}")
        sw= w.seasonwise(matches, season, team)
        st.write(f"Matches Played: {sw[0]}, Wins: {sw[1]}")
        wins = matches[(matches['season'] == season) & (matches['winner'] == team)]
        if not wins.empty:
            win_count = wins.shape[0]
            st.write(f"{team} won {win_count} matches in {season}.")
        else:
            st.write(f"{team} did not win any matches in {season}.")

    elif user_menu=='Number of Matches Played in a City':
        st.sidebar.header("Please select a city to analyze")
        city = st.sidebar.selectbox("Select a City", matches['city'].unique())
        st.subheader(f"Number of Matches Played in {season} in {city}")
        matches_in_city = matches[(matches['season'] == season) & (matches['city'] == city)]
        if not matches_in_city.empty:
            match_count = matches_in_city.shape[0]
            st.write(f"{match_count} matches were played in {city} during the {season} season.")
        else:
            st.write(f"No matches were played in {city} during the {season} season.")
    elif user_menu == "Player which became Player of the Match most":
        season_str = str(season)
        st.subheader(f"Players who won Player of the Match most in {season_str}")
        player_of_match = w.player_of_the_match(matches, season_str)
        if not player_of_match.empty:
            # Bar chart
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.bar(player_of_match['Player'], player_of_match['Number of Times'], color='skyblue')
            ax.set_xlabel('Player', fontsize=12)
            ax.set_ylabel('Number of Times', fontsize=12)
            ax.set_title(f'Player of the Match Awards in {season_str}', fontsize=14)
            plt.xticks(rotation=90, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
            top_player = player_of_match.iloc[0]
            st.write(f"{top_player['Player']} won Player of the Match {top_player['Number of Times']} times in {season_str}.")
    elif user_menu == "Number of Matches played at each venue":
        st.subheader(f"Number of Matches Played in {season}")
        w.venue(matches, season)
    

        

elif user_menu == "Player Performance":
    st.subheader("Player Performance Analysis")
    type= st.sidebar.selectbox("Select a Type", ("Batting", "Bowling"))
    if type == "Batting":
        st.subheader("Batting Performance")
        player = st.sidebar.selectbox("Select a Player", deliveries['batter'].unique())
        season_options = ['Overall', 'Season-Wise'] 
        season = st.sidebar.selectbox("Select a Season", season_options)
        metrics= st.sidebar.selectbox("Select a Metric", ("Runs", "Balls Faced"))
        if metrics=='Runs':
            if season == 'Overall':
                full=pd.merge(deliveries, matches, on='id')
                person=full[full['batter'] == player]
                runs = person['batsman_runs'].sum()
                st.write(f"{player} scored {runs} runs in total.")
            elif season == 'Season-Wise':
                full = pd.merge(deliveries, matches, on='id')
                person = full[full['batter'] == player]
                runs_by_season = person.groupby('season')['batsman_runs'].sum().reset_index()
                fig, ax = plt.subplots(figsize=(10, 6))
                bars = ax.bar(runs_by_season['season'].astype(str), runs_by_season['batsman_runs'], color='orange')
                ax.set_xlabel('Season', fontsize=12)
                ax.set_ylabel('Runs', fontsize=12)
                ax.set_title(f'{player} - Runs by Season', fontsize=14)
                plt.xticks(rotation=45)
                ax.bar_label(bars, padding=3)
                plt.tight_layout()
                st.pyplot(fig)
            else:
                full=pd.merge(deliveries, matches, on='id')
                person=full[(full['batter'] == player) & (full['season'] == season)]
                runs = person['batsman_runs'].sum()
                st.write(f"{player} scored {runs} runs in {season}.")
        elif metrics == 'Balls Faced':
            if season == 'Overall':
                person = deliveries[deliveries['batter'] == player]
                balls_faced = person.shape[0]
                st.write(f"{player} faced {balls_faced} balls in total.")
            elif season == 'Season-Wise':
                full = pd.merge(deliveries, matches, on='id')
                person = full[full['batter'] == player]
                balls_by_season = person.groupby('season').size().reset_index(name='balls_faced')
                fig, ax = plt.subplots(figsize=(10, 6))
                bars = ax.bar(balls_by_season['season'].astype(str), balls_by_season['balls_faced'], color='green')
                ax.set_xlabel('Season', fontsize=12)
                ax.set_ylabel('Balls Faced', fontsize=12)
                ax.set_title(f'{player} - Balls Faced by Season', fontsize=14)
                plt.xticks(rotation=45)
                ax.bar_label(bars, padding=3)
                plt.tight_layout()
                st.pyplot(fig)
            else:
                person = deliveries[(deliveries['batter'] == player) & (deliveries['season'] == season)]
                balls_faced = person.shape[0]
                st.write(f"{player} faced {balls_faced} balls in {season}.")
    elif type == "Bowling":
        player = str(st.sidebar.selectbox("Select a Player", deliveries['bowler'].unique()))
        season_options = ['Overall', 'Season-Wise']
        season = str(st.sidebar.selectbox("Select a Season", season_options))
        metrics = st.sidebar.selectbox("Select a Metric", ("Wickets", "Balls Bowled"))
        full = pd.merge(deliveries, matches, on='id')
        if season == 'Overall':
            if metrics == 'Wickets':
                bowlers=deliveries.groupby('bowler')['is_wicket'].sum().sort_values(ascending=False)
                bowlers=bowlers.reset_index()
                bowlers=pd.DataFrame(bowlers)
                bowlers.columns=['Bowler','Number of Wickets']
                player_wickets = bowlers[bowlers['Bowler'] == player]
                st.write(f"{player} took {player_wickets['Number of Wickets'].values[0]} wickets overall.")
            elif metrics == 'Balls Bowled':
                balls=deliveries['bowler'].value_counts()
                balls=balls.reset_index()
                balls=pd.DataFrame(balls)
                balls.columns=['Bowler','Number of Balls Bowled']
                balls= balls[balls['Bowler'] == player]
                st.write(f"{player} bowled {balls['Number of Balls Bowled'].values[0]} balls overall.")
        elif season == 'Season-Wise':
            if metrics=='Wickets':
                df2 = full[full['bowler'] == player]
                wickets_by_season = df2.groupby('season')['is_wicket'].sum().reset_index()
                fig, ax = plt.subplots(figsize=(10, 6))
                bars = ax.bar(wickets_by_season['season'].astype(str), wickets_by_season['is_wicket'], color='purple')
                ax.set_xlabel('Season', fontsize=12)
                ax.set_ylabel('Wickets', fontsize=12)
                ax.set_title(f'{player} - Wickets by Season', fontsize=14)
                plt.xticks(rotation=45)
                ax.bar_label(bars, padding=3)
                plt.tight_layout()
                st.pyplot(fig)
            elif metrics == 'Balls Bowled':
                df2 = full[full['bowler'] == player]
                balls_by_season = df2.groupby('season').size().reset_index(name='balls_bowled')
                fig, ax = plt.subplots(figsize=(10, 6))
                bars = ax.bar(balls_by_season['season'].astype(str), balls_by_season['balls_bowled'], color='orange')
                ax.set_xlabel('Season', fontsize=12)
                ax.set_ylabel('Balls Bowled', fontsize=12)
                ax.set_title(f'{player} - Balls Bowled by Season', fontsize=14)
                plt.xticks(rotation=45)
                ax.bar_label(bars, padding=3)
                plt.tight_layout()
                st.pyplot(fig)
                




                
            
elif user_menu == "Strike Rates":
    st.subheader("Strike Rates")
    st.sidebar.header("Please select the type to analyze")
    type = st.sidebar.selectbox("Select a Type", ("Overall", "Season-Wise"))
    if type == "Overall":
        st.subheader("Overall Strike Rates")
        strike_rate= w.strike_rate_overall(deliveries)
        st.dataframe(strike_rate)
        player = st.sidebar.selectbox("Select a Player", strike_rate['Batter'].unique())
        player_strike_rate= strike_rate[strike_rate['Batter'] == player]
        st.subheader(f"Strike Rate of {player}")
        st.write(f"{player} has a strike rate of {player_strike_rate['Strike Rate'].values[0]} overall.")
    else:
        st.subheader("Season-Wise Strike Rates")
        full = pd.merge(deliveries, matches, on='id')
        player = str(st.sidebar.selectbox("Select a Player", deliveries['batter'].unique()))
        player_data = full[full['batter'] == player]
        if not player_data.empty:
            runs_by_season = player_data.groupby('season')['batsman_runs'].sum()
            balls_by_season = player_data.groupby('season').size()
            strike_rate_by_season = (runs_by_season / balls_by_season * 100).reset_index()
            strike_rate_by_season.columns = ['season', 'Strike Rate']
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(strike_rate_by_season['season'].astype(str), strike_rate_by_season['Strike Rate'], color='teal')
            ax.set_xlabel('Season', fontsize=12)
            ax.set_ylabel('Strike Rate', fontsize=12)
            ax.set_title(f'{player} - Strike Rate by Season', fontsize=14)
            plt.xticks(rotation=45)
            ax.bar_label(bars, padding=3, fmt='%.2f')
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.write("No data available for the selected player.")

elif user_menu == "Toss-Win Analysis":
    season = st.sidebar.selectbox("Select a Season", ("Overall","Season-Wise"))
    team_options = ["Overall"] + list(matches['team1'].unique())
    team = st.sidebar.selectbox("Select a Team", team_options)
    if season == "Overall":
        if team=="Overall":
            st.subheader("Toss-Win Analysis Overall")
            w.toss_win_analysis_overall(matches)
        else:
            st.subheader(f"Toss-Win Analysis for {team} Overall")
            w.toss_win_analysis_season(matches, team)
    elif season == "Season-Wise":
        if team == "Overall":
            st.subheader("Toss-Win Analysis: Season-Wise (All Teams)")
            # Bar graph: x=season, y=number of matches where toss winner == match winner
            season_counts = matches.groupby('season').apply(lambda x: (x['toss_winner'] == x['winner']).sum()).reset_index(name='count')
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(season_counts['season'].astype(str), season_counts['count'], color='skyblue')
            ax.set_xlabel('Season', fontsize=12)
            ax.set_ylabel('Matches (Toss Winner = Match Winner)', fontsize=12)
            ax.set_title('Number of Matches per Season where Toss Winner also Won the Match', fontsize=14)
            plt.xticks(rotation=45)
            ax.bar_label(bars, padding=3)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.subheader(f"Toss-Win Analysis for {team} in Each Season")
            # Bar graph: x=season, y=number of matches where toss winner == team and team also won the match
            team_season = matches[matches['toss_winner'] == team]
            team_season = team_season[team_season['winner'] == team]
            season_counts = team_season.groupby('season').size().reset_index(name='count')
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(season_counts['season'].astype(str), season_counts['count'], color='coral')
            ax.set_xlabel('Season', fontsize=12)
            ax.set_ylabel('Matches', fontsize=12)
            ax.set_title(f'Number of Matches per Season where {team} Won Toss and Match', fontsize=14)
            plt.xticks(rotation=45)
            ax.bar_label(bars, padding=3)
            plt.tight_layout()
            st.pyplot(fig)
            
            
   
elif user_menu == "Best Partnerships":
    how=st.sidebar.selectbox("Select a Type", ("Best of all Time","Season-Wise"))
    if how=="Season-Wise":
        season = st.sidebar.selectbox("Select a Season", matches['season'].unique())
        full = pd.merge(deliveries, matches, on='id')
        st.subheader(f"Best Partnerships in {season}")
        df1=full[full['season']==season]
        df2=df1.groupby(['batter','non_striker'])['total_runs'].sum().sort_values(ascending=False)
        df2=df2.reset_index()
        df2=pd.DataFrame(df2)
        df2.columns=['Batter','Non Striker','Total Runs']
        swbp=df2.head(50)
        st.subheader("Top 50 Best Partnerships of the Season")  
        st.dataframe(swbp)

    if how=="Best of all Time":
        partners=deliveries.groupby(['batter','non_striker'])['total_runs'].sum().sort_values(ascending=False)
        partners=partners.reset_index()
        partners=pd.DataFrame(partners)
        partners.columns=['Batter','Non Striker','Total Runs']
        best_partners=partners.head(50)
        st.subheader("Top 50 Best Partnerships of All Time")
        st.dataframe(best_partners)
     

        


        
