import csv

def read_games():
    games = []

    with open("video_games.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            games.append(row)
    return games

def search_games(games, rating):
    found_games = []

    for row in games:
        if row[3].lower() == rating.lower():
            found_games.append(row)

    return found_games

def display_games(games):
    if not games:
        print("No video games found with this rating.")
    else:
        print("Video games found:\n")
        
        for row in games:
            print(f"Name: {row[0]}")
            print(f"Genre: {row[1]}")
            print(f"Developer: {row[2]}")
            print(f"ESRB Rating: {row[3]}")
            print("")

def main():
    rating = input("Enter the ESRB rating to search for: ")

    games = read_games()
    found_games = search_games(games, rating)
    display_games(found_games)

if __name__ == "__main__":
    main()
