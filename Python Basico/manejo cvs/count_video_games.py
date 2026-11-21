
import csv


def read_games():
    games = []

    with open("video_games.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            games.append(row)

    return games


def count_genres(games):
    genre_counts = {}

    for row in games:
        genre = row[1]

        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1

    return genre_counts


def display_counts(genre_counts):
    print("Number of video games by genre:")

    for genre, count in sorted(genre_counts.items()):
        print(genre, ":", count)


def main():
    games = read_games()
    genre_counts = count_genres(games)
    display_counts(genre_counts)


if __name__ == "__main__":
    main()

