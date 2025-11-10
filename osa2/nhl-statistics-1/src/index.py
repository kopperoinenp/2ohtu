from statistics_service import StatisticsService
from player_reader import PlayerReader


def main():
    stats = StatisticsService(
        PlayerReader("https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/tehtavat/refs/heads/main/osa2/stats/players-23-24.txt")
        )

    print("Philadelphia Flyers:")
    for player in stats.team("PHI"):
        print(player)

    print("Top point getters:")
    for player in stats.top(10):
        print(player)


if __name__ == "__main__":
    main()
