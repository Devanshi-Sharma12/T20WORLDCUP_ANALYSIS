
data = [
    "Team,Player,Runs,Strike Rate",
    "Afghanistan,Rahmanullah Gurbaz,281,124.33",
    "India,Rohit Sharma,257,156.7",
    "Australia,Travis Head,255,158.38",
    "South Africa,Quinton de Kock,243,140.46",
    "Afghanistan,Ibrahim Zadran,231,107.44"
]

csv_file_path = 't20_world_cup_2024.csv'

with open(csv_file_path, 'w') as file:
    for line in data:
        file.write(line + '\n')

print(f"CSV file '{csv_file_path}' has been created.")
