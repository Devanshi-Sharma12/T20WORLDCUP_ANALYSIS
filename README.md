# updated_t20_list
This project contains a Python script to find and display player statistics from a CSV file containing data about the top 5 country players in the recent T20 World Cup.The data is collected from ICC official site.

*Description*
The script allows users to search for a player's statistics from a CSV file. The CSV file should have the player's name and their corresponding statistics. The domains include:
1.best bowlers 
2.highest score individual batters
3.Most catches 
4.Most wickets
5.Overall performace of players.

*Dependencies*
Python 3.6
argparse (included in the Python Standard Library)
csv (included in the Python Standard Library)

*Demonstration of how my project works*
Suppose your script file is named playerdata.py.
Step 1:Prepare your environment:
Ensure you have Python installed.
Make sure your CSV file most_wickets_t20_world_cup_2024.csv is in the same directory as your script.

Step 2:Run the script:
Open your terminal or command prompt, navigate to the directory containing the script and the CSV file, and run the script using the following command:
python playerdata.py most_wickets_t20_world_cup_2024.csv "Jasprit Bumrah"

Step 3:
Expected Output:
The script will output the statistics for Jasprit Bumrah:
Stats for Jasprit Bumrah:
Player: Jasprit Bumrah
Country: India
Wickets: 15
Average: 8.26


