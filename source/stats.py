import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate games each team has played
def calculate_team_games(df):
    team_games = {}

    for team in df.Home_Team.unique():
        home_games = df.Home_Team.value_counts()[team]
        away_games = df.Away_Team.value_counts()[team]
    
        team_games[team] = int(home_games + away_games)

    return team_games

# Function to calculate wins for each team
def calculate_team_wins(df):
    team_wins = {}

    for team in df.Home_Team.unique():
        home_wins = ((df['Home_Team'] == team) &
                 (df['Winner'] == 'Home')).sum()
        away_wins = ((df['Away_Team'] == team) &
                 (df['Winner'] == 'Away')).sum()

        team_wins[team] = int(home_wins + away_wins)
        
    return team_wins

# Function to calculate teams home win percentage
def calculate_home_win_percentage(df):
    team_home_win_percentage = {}

    for team in df.Home_Team.unique():
        home_wins = ((df['Home_Team'] == team) &
                     (df['Winner'] == 'Home')).sum()
        home_games = df.Home_Team.value_counts()[team]
    
        team_home_win_percentage[team] = round(home_wins / home_games * 100, 2)
        
    return team_home_win_percentage

# Function to calculate teams away win percentage
def calculate_away_win_percentage(df):
    team_away_win_percentage = {}

    for team in df.Home_Team.unique():
        away_wins = ((df['Away_Team'] == team) &
                 (df['Winner'] == 'Away')).sum()
        away_games = df.Away_Team.value_counts()[team]
    
        team_away_win_percentage[team] = round(away_wins / away_games * 100, 2)

    return team_away_win_percentage

# Function to calculate teams overall win percentage
def calculate_team_win_percentage(team_wins, team_games):
    team_win_percentage = {}

    for team in team_games:
        win_percentage = team_wins[team]/team_games[team] * 100
        win_percentage = float(round(win_percentage, 1))
        team_win_percentage[team] = win_percentage

    return team_win_percentage

# Function to calculate home advantage for all teams
def calculate_home_advantage(df):
    home_advantage = df['Winner'].value_counts(normalize=True) * 100
    home_advantage = round(home_advantage, 2)

    return home_advantage

# Function to calculate average points scored by each team
def calculate_team_avg_points(df, team_games):
    team_points = {}

    for team in df.Home_Team.unique():
        home_df = df[df['Home_Team'] == team]
        home_points = home_df.Home_Points.sum()
    
        away_df = df[df['Away_Team'] == team]
        away_points = away_df.Away_Points.sum()

        points = int(home_points + away_points)
        avg_points = points / team_games[team]
        team_points[team] = round(avg_points, 2)

    return team_points

# Function to calculate teams average winning margin
def calculate_team_avg_winning_margin(df):
    team_avg_winning_margin = {}

    for team in df.Home_Team.unique():
        home_win_filter = ((df['Home_Team'] == team) &
                           (df['Winner'] == 'Home'))
        home_win_df = df[home_win_filter]
        home_margins = (home_win_df['Home_Points'] - home_win_df['Away_Points'])

        away_win_filter = ((df['Away_Team'] == team) &
                           (df['Winner'] == 'Away'))
        away_win_df = df[away_win_filter]
        away_margins = (away_win_df['Away_Points'] - away_win_df['Home_Points'])

        team_avg_winning_margin[team] = round(pd.concat([home_margins, away_margins]).mean(), 2)

    return team_avg_winning_margin

# Function to calculate teams average points conceded
def calculate_team_avg_points_conceded(df, team_games):
    team_points_conceded = {}

    for team in df.Home_Team.unique():
        home_df = df[df['Home_Team'] == team]
        home_points_conceded = home_df.Away_Points.sum()
    
        away_df = df[df['Away_Team'] == team]
        away_points_conceded = away_df.Home_Points.sum()

        points_conceded = int(home_points_conceded + away_points_conceded)
        avg_points_conceded = points_conceded / team_games[team]
        team_points_conceded[team] = round(avg_points_conceded, 2)

    return team_points_conceded

def calculate_team_avg_pt_differential(df):
    team_avg_pt_differential = {}

    for team in df.Home_Team.unique():
        home_win_filter = ((df['Home_Team'] == team) &
                           (df['Winner'] == 'Home'))
        home_win_df = df[home_win_filter]
        home_win_margins = (home_win_df['Home_Points'] - home_win_df['Away_Points'])

        away_win_filter = ((df['Away_Team'] == team) &
                           (df['Winner'] == 'Away'))
        away_win_df = df[away_win_filter]
        away_win_margins = (away_win_df['Away_Points'] - away_win_df['Home_Points'])

        win_margins = pd.concat([home_win_margins, away_win_margins])

        
        home_loss_filter = ((df['Home_Team'] == team) &
                           (df['Winner'] == 'Away'))
        home_loss_df = df[home_loss_filter]
        home_loss_margins = (home_loss_df['Home_Points'] - home_loss_df['Away_Points'])

        away_loss_filter = ((df['Away_Team'] == team) &
                           (df['Winner'] == 'Home'))
        away_loss_df = df[away_loss_filter]
        away_loss_margins = (away_loss_df['Away_Points'] - away_loss_df['Home_Points'])

        loss_margins = pd.concat([home_loss_margins, away_loss_margins])

        all_margins = pd.concat([win_margins, loss_margins])
        team_avg_pt_differential[team] = round(all_margins.mean(), 2)

    return team_avg_pt_differential