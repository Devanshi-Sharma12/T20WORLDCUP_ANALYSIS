import csv

csv_file = 't20_world_cup_2024.csv'
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    
    for line in csv_reader:
        print(line)
