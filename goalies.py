from IPython.display import display
from cv2 import getPerspectiveTransform
import pandas as pd
import matplotlib.pyplot as plt

goalies_df = pd.read_csv('t.csv')
#df = goalies_df.groupby(['tmID', 'year'])


total_players = goalies_df['playerID'].nunique()
wins_agg = goalies_df['W'].sum() / total_players
losses_agg = goalies_df['L'].sum() / total_players
gp_agg = goalies_df['GP'].sum() / total_players

# print(wins_agg)
# print(losses_agg)
# print(gp_agg)

# print(goals_stopped[['playerID', 'SHO']])

new_df = goalies_df.groupby(['tmID', 'year', 'playerID'],
                            as_index=False)['SHO'].sum()


most_stopped = new_df[new_df['SHO'].max() ==
                      new_df['SHO']]

most_goals_stopped = {
    'playerID: ': most_stopped['playerID'].values[0],  'goals stopped: ': most_stopped['SHO'].values[0]}

print(most_goals_stopped)


total_mins = goalies_df.groupby(['tmID', 'year', 'playerID'],
                                as_index=False)['Min'].sum()

print(total_mins)

new_df['efficiency'] = new_df['SHO'] / total_mins['Min']

print(new_df)

total_minutes_played = goalies_df['Min'].sum()
total_goals_against = goalies_df['GA'].sum()

# best_efficiency =


# mins_over_GA_agg =
