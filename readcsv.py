csv_file_path = 't20_world_cup_2024.csv'
with open(csv_file_path, 'r') as file:
    contents = file.readlines()
data = []
for line in contents:
    row = line.strip().split(',')
    data.append(row)
for row in data:
    print(row)
