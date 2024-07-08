import argparse
import csv

def find_player_stats(csv_file, player_name):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['Player'].lower() == player_name.lower():
                return row
    return None

def main():
    parser = argparse.ArgumentParser(description="Find player stats from a CSV file.")
    parser.add_argument('csv_file', type=str, help='Name of the CSV file')
    parser.add_argument('player_name', type=str, help='Name of the player')

    args = parser.parse_args()

    player_stats = find_player_stats(args.csv_file, args.player_name)
    
    if player_stats:
        print(f"Stats for {args.player_name}:")
        for key, value in player_stats.items():
            print(f"{key}: {value}")
    else:
        print(f"No stats found for player: {args.player_name}")

if __name__ == '__main__':
    main()
