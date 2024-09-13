import unittest
from hockey_main import Team, Player, Skater


class TestClass(unittest.TestCase):
    def testisstring(self):
        test_team = Team("Flyers", "Philadelphia", 'Gritty')
        self.assertEqual(type(test_team.team_info()), type("s"))

        test_player = Player("Giroux", 28, 36, "Center", test_team.team_name, test_team.city, test_team.mascot)
        self.assertEqual(type(test_player.player_info()), type("s"))

        test_skater = Skater(test_player.player_name, test_player.number, test_player.age, test_player.position, test_team.team_name, test_team.city, test_team.mascot, 30, 43)
        self.assertEqual(type(test_skater.skater_info()), type("s"))
        self.assertEqual(type(test_skater.calc_points()), type(1))


unittest.main()
