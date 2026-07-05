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



        row_dict = {'Home_Team' : home_team,
                    'Away_Team' : away_team,
                    'Home_Win_Percentage' : home_win_percentage,
                    'Away_Win_Percentage' : away_win_percentage,
                    'Winner' : row['Winner']
                    }
        rows.append(row_dict)



    feature_df = pd.DataFrame(rows)

    return feature_df

