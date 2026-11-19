import csv

def read_games():
    games = []

    with open("video_games.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader) 
        
        
        for row in reader:
            games.append(row)
    return games

def display_games(games):
    print("List of registered video games:\n")

    for row in games:
        print(f"Name: {row[0]}")
        print(f"Genre: {row[1]}")
        print(f"Developer: {row[2]}")
        print(f"ESRB Rating: {row[3]}")
        print("")

def main():
    games = read_games()
    display_games(games)

if __name__ == "__main__":
    main()
