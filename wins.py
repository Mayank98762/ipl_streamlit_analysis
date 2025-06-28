
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
deliveries = pd.read_csv("deliveries.csv")
matches = pd.read_csv("matches.csv")
# Replace 'matches.csv' with the actual path to your matches data file
def total_wins(df):
    finals=df[df['match_type']=='Final']
    wins=finals['winner'].value_counts()
    wins=wins.reset_index()

    wins=pd.DataFrame(wins)
    wins.columns=['Teams','Total Number of Wins']
    return wins 

   
def matches_won(df):
    matches_won = df['winner'].value_counts().reset_index()
    matches_won.columns = ['Teams', 'Total Matches Won']
    return matches_won



def seasonwise(df,season,team):
    
    # Filter for the selected season and team
    team_matches = df[(df['season'] == season) & ((df['team1'] == team) | (df['team2'] == team))]
    matches_played = team_matches.shape[0]
    wins = team_matches[team_matches['winner'] == team].shape[0]
    return matches_played, wins

def player_of_the_match(df,season):
    new=df[df['season']==season]
    new1=new['player_of_match'].value_counts().sort_values(ascending = False)
    new1=pd.DataFrame(new1)
    new1=new1.reset_index()
    new1.columns=['Player','Number of Times']
    return new1


def venue(df,season):
    new=df[df['season']==season]
    new1=new['venue'].value_counts().sort_values(ascending = False)
    new1=pd.DataFrame(new1)
    new1=new1.reset_index()
    new1.columns=['Venue','Number of Matches']
    x=new1['Venue']
    y=new1['Number of Matches']
    plt.figure(figsize=(12,8))
    plt.bar(x,y,color='blue')
    plt.xlabel("Venue")
    plt.ylabel("Number of Matches")
    plt.xticks(rotation=90)
    st.pyplot(plt)
    

def strike_rate_overall(df):
    runs_batsman=df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False)
    runs_batsman=runs_batsman.reset_index()
    runs_batsman=pd.DataFrame(runs_batsman)
    runs_batsman.columns=['Batter','Total Runs']
    
    balls_batsman=df.groupby('batter').size().sort_values(ascending=False)
    balls_batsman=balls_batsman.reset_index()
    balls_batsman=pd.DataFrame(balls_batsman)
    balls_batsman.columns=['Batter','Total Balls Faced']
    final=pd.merge(runs_batsman,balls_batsman,on='Batter')
    final['Strike Rate']=final['Total Runs']/final['Total Balls Faced']*100
    return final.sort_values(by='Strike Rate',ascending=False)



import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt
deliveries = pd.read_csv("deliveries.csv")
matches = pd.read_csv("matches.csv")
# Replace 'matches.csv' with the actual path to your matches data file
def total_wins(df):
    finals=df[df['match_type']=='Final']
    wins=finals['winner'].value_counts()
    wins=wins.reset_index()

    wins=pd.DataFrame(wins)
    wins.columns=['Teams','Total Number of Wins']
    return wins 

   
def matches_won(df):
    matches_won = df['winner'].value_counts().reset_index()
    matches_won.columns = ['Teams', 'Total Matches Won']
    return matches_won



def seasonwise(df,season,team):
    
    # Filter for the selected season and team
    team_matches = df[(df['season'] == season) & ((df['team1'] == team) | (df['team2'] == team))]
    matches_played = team_matches.shape[0]
    wins = team_matches[team_matches['winner'] == team].shape[0]
    return matches_played, wins

def player_of_the_match(df,season):
    new=df[df['season']==season]
    new1=new['player_of_match'].value_counts().sort_values(ascending = False)
    new1=pd.DataFrame(new1)
    new1=new1.reset_index()
    new1.columns=['Player','Number of Times']
    return new1


def venue(df,season):
    new=df[df['season']==season]
    new1=new['venue'].value_counts().sort_values(ascending = False)
    new1=pd.DataFrame(new1)
    new1=new1.reset_index()
    new1.columns=['Venue','Number of Matches']
    x=new1['Venue']
    y=new1['Number of Matches']
    plt.figure(figsize=(12,8))
    plt.bar(x,y,color='blue')
    plt.xlabel("Venue")
    plt.ylabel("Number of Matches")
    plt.xticks(rotation=90)
    st.pyplot(plt)
    

def strike_rate_overall(df):
    runs_batsman=df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False)
    runs_batsman=runs_batsman.reset_index()
    runs_batsman=pd.DataFrame(runs_batsman)
    runs_batsman.columns=['Batter','Total Runs']
    
    balls_batsman=df.groupby('batter').size().sort_values(ascending=False)
    balls_batsman=balls_batsman.reset_index()
    balls_batsman=pd.DataFrame(balls_batsman)
    balls_batsman.columns=['Batter','Total Balls Faced']
    final=pd.merge(runs_batsman,balls_batsman,on='Batter')
    final['Strike Rate']=final['Total Runs']/final['Total Balls Faced']*100
    return final.sort_values(by='Strike Rate',ascending=False)



    