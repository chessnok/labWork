import unittest

from game.player import Player


class DynamicBaseParams(unittest.TestCase):
    pl = Player()

    def test_pl_money(self):
        self.assertEqual(120, self.pl.money)

    def test_pl_credit(self):
        self.assertEqual(0, self.pl.credit)

    def test_pl_promotion(self):
        self.assertEqual(0, self.pl.promotion)

    def test_pl_dataIsReady(self):
        self.assertEqual(False, self.pl.dataIsReady)

    def test_pl_equipments(self):
        self.assertEqual({}, self.pl.equipments)

    def test_pl_services(self):
        self.assertEqual({"logistic": False, "training": False}, self.pl.services)

