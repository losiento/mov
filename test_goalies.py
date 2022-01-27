import unittest
import pandas as pd
from goalies import *

goalies_df = pd.read_csv('t.csv')


class TestGoalies(unittest.TestCase):

    def test_get_total_players(self):
        self.assertEqual(get_total_players(goalies_df), 4)

    def test_get_wins_agg(self):
        self.assertEqual(get_wins_agg(goalies_df), 40.75)

    def test_get_losses_agg(self):
        self.assertEqual(get_losses_agg(goalies_df), 14.0)

    def test_get_gp_agg(self):
        self.assertEqual(get_gp_agg(goalies_df), 58.5)

    def test_get_player_most_stopped(self):
        self.assertEqual(get_player_most_stopped(goalies_df), {
                         'playerID: ': 'destiny', 'goals stopped: ': 60})


if __name__ == '__main__':
    unittest.main()
