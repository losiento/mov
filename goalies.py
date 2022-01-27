import pandas as pd


def get_total_players(df):
    return df['playerID'].nunique()


def get_wins_agg(df):
    return df['W'].sum() / get_total_players(df)


def get_losses_agg(df):
    return df['L'].sum() / get_total_players(df)


def get_gp_agg(df):
    return df['GP'].sum() / get_total_players(df)


def get_goals_stopped(df):
    return df.groupby(['tmID', 'year', 'playerID'],
                      as_index=False)['SHO'].sum()


def get_most_stopped(goals_stopped):
    return goals_stopped[goals_stopped['SHO'].max() ==
                         goals_stopped['SHO']]


def get_player_most_stopped(df):
    most_stopped = get_most_stopped(df)
    return {
        'playerID: ': most_stopped['playerID'].values[0],  'goals stopped: ': most_stopped['SHO'].sum()}


def get_total_mins(df):
    return df.groupby(['tmID', 'year', 'playerID'],
                      as_index=False)['Min'].sum()


def get_most_efficiency(df):
    new_df = get_total_mins(df)
    goals_stopped = get_goals_stopped(df)
    total_mins = get_total_mins(df)
    new_df['efficiency'] = goals_stopped['SHO'] / total_mins['Min']
    return new_df[new_df['efficiency'].max() ==
                  new_df['efficiency']]


def get_player_most_efficiency(df):
    most_efficiency = get_most_efficiency(df)
    return {
        'playerID: ': most_efficiency['playerID'].values[0],  'efficiency: ': most_efficiency['efficiency'].values[0]}


def get_total_mins_played(df):
    return goalies_df['Min'].sum()


def get_total_goals_against(df):
    return goalies_df['GA'].sum()


def get_total_shots_against(df):
    return goalies_df['SA'].sum()


def get_mins_over_GA_agg(df):
    return get_total_mins_played(df) / get_total_goals_against(df)


def get_GA_over_SA_agg(df):
    return get_total_goals_against(df) / get_total_shots_against(df)


def get_total_GP(df):
    return df.groupby(['tmID', 'year', 'playerID', 'W'],
                      as_index=False)['GP'].sum()


def get_avg_percentage_wins(df):
    new_df = get_total_GP(df)
    new_df['APW'] = new_df['W'] / new_df['GP']
    return new_df['APW'].mean()


goalies_df = pd.read_csv('t.csv')
print(goalies_df['tmID'])
print(goalies_df['year'])
print(get_wins_agg(goalies_df))
print(get_losses_agg(goalies_df))
print(get_gp_agg(goalies_df))
print(get_mins_over_GA_agg(goalies_df))
print(get_GA_over_SA_agg(goalies_df))
print(get_avg_percentage_wins(goalies_df))
print(get_player_most_stopped(goalies_df))
print(get_player_most_efficiency(goalies_df))
