import pandas as pd
from source.stats import *

def create_feature_df(df):

    rows = []
    
    
    for index, row in df.iterrows():
        history_df = df.iloc[:index]

        home_team = row['Home_Team']
        away_team = row['Away_Team']

        home_win_percentage = calculate_indv_home_win_percentage(history_df, home_team)
        away_win_percentage = calculate_indv_away_win_percentage(history_df, away_team)

        home_team_avg_points_for = calculate_indv_avg_points(history_df, home_team)
        away_team_avg_points_for = calculate_indv_avg_points(history_df, away_team)

        home_team_avg_points_conceded = calculate_indv_team_avg_points_conceded(history_df, home_team)
        away_team_avg_points_conceded = calculate_indv_team_avg_points_conceded(history_df, away_team)

        home_team_avg_points_differential = calculate_indv_avg_pt_differential(history_df, home_team)
        away_team_avg_points_differential = calculate_indv_avg_pt_differential(history_df, away_team)
        
        home_last5_win_percentage = calculate_indv_last5_win_percentage(history_df, home_team)
        away_last5_win_percentage = calculate_indv_last5_win_percentage(history_df, away_team)

        home_last5_avg_points_for = calculate_indv_last5_avg_points_for(history_df, home_team)
        away_last5_avg_points_for = calculate_indv_last5_avg_points_for(history_df, away_team)
        
        home_last5_avg_points_conceded = calculate_indv_last5_avg_points_conceded(history_df, home_team)
        away_last5_avg_points_conceded = calculate_indv_last5_avg_points_conceded(history_df, away_team)

        home_last5_avg_points_differential = calculate_indv_last5_avg_points_differential(history_df, home_team)
        away_last5_avg_points_differential = calculate_indv_last5_avg_points_differential(history_df, away_team)



        row_dict = {'Season' : row['Season'],
                    'Home_Team' : home_team,
                    'Away_Team' : away_team,
                    'Home_Win_Percentage' : home_win_percentage,
                    'Away_Win_Percentage' : away_win_percentage,
                    'Home_Avg_Points_For' : home_team_avg_points_for,
                    'Away_Avg_Points_For' : away_team_avg_points_for,
                    'Home_Avg_Points_Conceded' : home_team_avg_points_conceded,
                    'Away_Avg_Points_Conceded' : away_team_avg_points_conceded,
                    'Home_Avg_Points_Differential' : home_team_avg_points_differential,
                    'Away_Avg_Points_Differential' : away_team_avg_points_differential,
                    'Home_Last5_Win_Percentage' : home_last5_win_percentage,
                    'Away_Last5_Win_Percentage' : away_last5_win_percentage,
                    'Home_Last5_Avg_Points_For' : home_last5_avg_points_for,
                    'Away_Last5_Avg_Points_For' : away_team_avg_points_for,
                    'Home_Last5_Avg_Points_Conceded' : home_team_avg_points_conceded,
                    'Away_Last5_Avg_Points_Conceded' : away_team_avg_points_conceded,
                    'Home_Last5_Avg_Points_Differential' : home_last5_avg_points_differential,
                    'Away_Last5_Avg_Points_Differential' : away_last5_avg_points_differential,
                    'Winner' : row['Winner']
                    }
        rows.append(row_dict)



    feature_df = pd.DataFrame(rows)

    return feature_df

