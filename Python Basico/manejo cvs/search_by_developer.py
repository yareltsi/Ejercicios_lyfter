
import csv


def read_games():
    games = []

    with open("video_games.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            games.append(row)

    return games


def search_by_developer(games, developer):
    found_games = []

    for row in games:
        if row[2].lower() == developer.lower():
            found_games.append(row)

    return found_games


def display_games(games, developer):
    print(f"\nVideo games developed by {developer}:\n")

    if not games:
        print("No video games found for this developer.")
    else:
        for row in games:
            print("Name:", row[0])
            print("Genre:", row[1])
            print("Developer:", row[2])
            print("ESRB Rating:", row[3])
            print()


def main():
    developer = input("Enter the developer name to search: ")

    games = read_games()
    found_games = search_by_developer(games, developer)
    display_games(found_games, developer)


if __name__ == "__main__":
    main()

