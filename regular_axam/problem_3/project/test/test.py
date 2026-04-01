from unittest import TestCase, main

from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(TestCase):

    def setUp(self):
        self.player = SoccerPlayer("Cristiano", 38, 10, "Juventus")
        self.other_player = SoccerPlayer("Messias", 35, 15, "PSG")

    def test_init_successful(self):
        self.assertEqual("Cristiano", self.player.name)
        self.assertEqual(38, self.player.age)
        self.assertEqual(10, self.player.goals)
        self.assertEqual("Juventus", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_name_setter_raises_when_name_too_short(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Pesho", 20, 5, "PSG")
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_age_setter_raises_when_age_below_16(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Cristiano", 15, 5, "PSG")
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_goals_setter_sets_zero_when_negative(self):
        player = SoccerPlayer("Cristiano", 38, -5, "Juventus")
        self.assertEqual(0, player.goals)

    def test_team_setter_raises_for_invalid_team(self):
        expected_message = (
            "Team must be one of the following: "
            "Barcelona, Real Madrid, Manchester United, Juventus, PSG!"
        )
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Cristiano", 38, 10, "Liverpool")
        self.assertEqual(expected_message, str(ex.exception))

    def test_change_team_returns_invalid_message_for_invalid_team(self):
        result = self.player.change_team("Liverpool")
        self.assertEqual("Invalid team name!", result)
        self.assertEqual("Juventus", self.player.team)

    def test_change_team_successfully_changes_team(self):
        result = self.player.change_team("Barcelona")
        self.assertEqual("Team successfully changed!", result)
        self.assertEqual("Barcelona", self.player.team)

    def test_add_new_achievement_adds_achievement_when_missing(self):
        result = self.player.add_new_achievement("Golden Boot")

        self.assertEqual(
            "Golden Boot has been successfully added to the achievements collection!",
            result
        )
        self.assertIn("Golden Boot", self.player.achievements)
        self.assertEqual(1, self.player.achievements["Golden Boot"])

    def test_add_new_achievement_increments_existing_achievement(self):
        self.player.add_new_achievement("Golden Boot")
        self.player.add_new_achievement("Golden Boot")

        self.assertEqual(2, self.player.achievements["Golden Boot"])

    def test_lt_returns_other_player_is_top_scorer_when_other_has_more_goals(self):
        result = self.player < self.other_player
        expected = "Messias is a top goal scorer! S/he scored more than Cristiano."
        self.assertEqual(expected, result)

    def test_lt_returns_self_is_better_when_self_has_more_goals(self):
        better_player = SoccerPlayer("Cristiano", 38, 20, "Juventus")
        weaker_player = SoccerPlayer("Messias", 35, 15, "PSG")

        result = better_player < weaker_player
        expected = "Cristiano is a better goal scorer than Messias."
        self.assertEqual(expected, result)

    def test_lt_returns_self_is_better_when_goals_are_equal(self):
        first_player = SoccerPlayer("Cristiano", 38, 15, "Juventus")
        second_player = SoccerPlayer("Messias", 35, 15, "PSG")

        result = first_player < second_player
        expected = "Cristiano is a better goal scorer than Messias."
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()