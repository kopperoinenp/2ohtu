import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_palauttaa_oikean_pelaajan(self):
        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.team, "EDM")

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        self.assertIsNone(self.stats.search("Pukki"))

    def test_team_palauttaa_joukkueen_pelaajat(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        names = [p.name for p in edm_players]
        self.assertIn("Gretzky", names)
        self.assertIn("Kurri", names)

    def test_top_palauttaa_yhden_parhaan(self):
        paras = self.stats.top(1)
        self.assertEqual(len(paras), 1)
        self.assertEqual(paras[0].name, "Gretzky")

    def test_top_palauttaa_useamman_parhaan_oikeassa_jarjestyksessa(self):
        top3 = self.stats.top(3)
        self.assertEqual([p.name for p in top3],
                         ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_palauttaa_tyhjan_listan_jos_zero(self):
        self.assertEqual(self.stats.top(0), [])


if __name__ == "__main__":
    unittest.main()
