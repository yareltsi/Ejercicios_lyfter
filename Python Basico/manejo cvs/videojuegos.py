import csv


def get_game_data():
    name = input("Enter the video game name: ")
    genre = input("Enter the video game genre: ")
    developer = input("Enter the video game developer: ")
    esrb_rating = input("Enter the ESRB rating: ")

    return [name, genre, developer, esrb_rating]


def save_games(games, file_name):
    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Genre", "Developer", "ESRB Rating"])
        writer.writerows(games)


def main():
    quantity = int(input("How many video games do you want to register? "))

    games = []

    for i in range(quantity):
        game = get_game_data()
        games.append(game)

    save_games(games, "video_games.csv")


if __name__ == "__main__":
    main()

