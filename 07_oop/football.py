import logging
import random
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class Ball:
    def __init__(self, size=5, color="blue", pressure=5.0):
        self.size = size
        self.color = color
        self.pressure = pressure

    def change_pressure(self, new_pressure):
        self.pressure = new_pressure

    def __repr__(self):
        return f"Ball object. {self.size=}, {self.color=}, {self.pressure=}"


class Player:
    def __init__(self, stamina=8, speed=7, agility=9):
        self.stamina = stamina
        self.speed = speed
        self.agility = agility
        self.ball = None
        self.position = (0, 0)

    def pass_the_ball(self, player):
        if self.ball:
            player.ball = self.ball
            self.ball = None

    def __repr__(self):
        return f"Player object. {self.stamina=}, {self.speed=}, {self.agility=}"


class Team:
    def __init__(self):
        self.players = [
            Player(
                stamina=random.randint(5, 10),
                speed=random.randint(5, 10),
                agility=random.randint(5, 10),
            )
            for _ in range(11)
        ]
        self.points = 0

    def __repr__(self):
        return "Team object.\n\t" + "\n\t".join(map(repr, self.players))

class Match:
    def __init__(self):
        self.team_a = Team()
        self.team_b = Team()
        self.ball = Ball()


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_match(self):
        match = Match()

        log.debug(match.team_a)
        log.debug(match.team_b)
        player_x = match.team_a.players[0]
        player_y = match.team_a.players[1]

        self.assertIsNone(player_x.ball)

        player_x.ball = match.ball
        self.assertIsNotNone(player_x.ball)

        player_x.pass_the_ball(player_y)
        self.assertIsNone(player_x.ball)
        self.assertIsNotNone(player_y.ball)


if __name__ == "__main__":
    unittest.main(verbosity=2)
