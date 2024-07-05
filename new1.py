import os
current_directory = os.getcwd() 
documents_path = os.path.join(current_directory, 'Documents')

if not os.path.exists(documents_path):
    os.makedirs(documents_path)
    print(f"Created '{documents_path}' directory.")

os.chdir(documents_path)
print(f"Changed directory to '{documents_path}' successfully.")
print(f"Current working directory: {os.getcwd()}")

data = [
    {"Player": "Aiden Markram", "Country": "South Africa", "Catches": 8},
    {"Player": "Glenn Maxwell", "Country": "Australia", "Catches": 7},
    {"Player": "Harry Brook", "Country": "England", "Catches": 7},
    {"Player": "Tristan Stubbs", "Country": "South Africa", "Catches": 7},
    {"Player": "Tanzim Hasan Sakib", "Country": "Bangladesh", "Catches": 6},
    {"Player": "Mohammad Nabi", "Country": "Afghanistan", "Catches": 6},
    {"Player": "Heinrich Klaasen", "Country": "South Africa", "Catches": 6}
]

csv_file_path = 'most_catches_t20_world_cup_2024.csv'

with open(csv_file_path, 'w') as file:
    file.write('Player,Country,Catches\n')
    for record in data:
        file.write(f"{record['Player']},{record['Country']},{record['Catches']}\n")
print("CSV file has been created successfully.")

if os.path.exists(csv_file_path):
    print(f"CSV file '{csv_file_path}' exists.")
else:
    print(f"CSV file '{csv_file_path}' does not exist.")
