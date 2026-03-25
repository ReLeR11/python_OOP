from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = "Test Hero"
    level = 10
    health = 20.5
    damage = 15.5

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_attributes_type(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_enemy_hero_same_names(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as e:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_hero_health_not_enough(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

        self.hero.health = -1

        with self.assertRaises(ValueError) as e2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e2.exception))


    def test_enemy_health_not_enough(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)

        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(e.exception))

        enemy.health = -1

        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(e.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-134.5, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_win(self):
        enemy = Hero("Enemy", 1, 1, 1)

        result = self.hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(24.5, self.hero.health)
        self.assertEqual(20.5, self.hero.damage)

    def test_hero_lose(self):
        enemy = Hero("Enemy", 100, 100, 100)
        self.hero.health = 10
        self.hero.damage = 10
        self.hero.level = 1

        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(95, enemy.health)
        self.assertEqual(105, enemy.damage)

    def test_str(self):
        result = f"Hero {self.username}: {self.level} lvl\n" \
                 f"Health: {self.health}\n" \
                 f"Damage: {self.damage}\n"

        actual = str(self.hero)

        self.assertEqual(result, actual)



if __name__ == '__main__':
    main()