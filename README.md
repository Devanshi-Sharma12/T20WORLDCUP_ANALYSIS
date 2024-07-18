**PROJECT NAME: T20 WORLD_CUP_ANALYSIS**

This project contains a Python script to find and display player statistics from a CSV file containing data about the top 5 country players in the recent T20 World Cup.The data is collected from ICC official site.

## Description
The script allows users to search for a player's statistics from a CSV file. The CSV file should have the player's name and their corresponding statistics. 
- The statistics are regarding:
    - Best bowlers.
    - Highest scorers.
    - Individual batters.
    - Most catches by players.
    - Most wickets taken by players.
    - Overall performance of players.

## Dependencies
1. Python 3.6
2. argparse (included in the Python Standard Library)
3. csv (included in the Python Standard Library)

## Demonstration of this project works
Suppose your script file is named `playerdata.py`.

1. Prepare your environment:

- Ensure you have Python installed.

- Make sure your CSV file most_wickets_t20_world_cup_2024.csv is in the same directory as your script.


2. Run the script:

  - Open your terminal or command prompt, navigate to the directory containing the script and the CSV file, and run the script using the following command:

      
       ` python name_of_script.py name_of_csv_file.csv "name_of_player" `

       #### Command used in code:
       ```
        python playerdata.py most_wickets_t20_world_cup_2024.csv "Jasprit Bumrah" 
       ```


3. output: 
    ```
    Stats for Jasprit Bumrah:
    Player: Jasprit Bumrah
    Country: India
    Wickets: 15
    Average: 8.26
    ```

4. Visual representation of my bar chart and pie chart
![Bar graph and pie chart](C:/Users/DELL/OneDrive/Desktop/experiment/updated_t20_list/data_visualization_using_barchart_and_pie.png)


## Explanation
1. playerdata.py: 

   This script uses argparse to handle command-line arguments (csv_file and player_name). It reads the CSV file (most_wickets_t20_world_cup_2024.csv), searches for the specified player (Jasprit Bumrah in this example), and prints their statistics if found.

2. Execution:
   Running the script in the terminal with appropriate arguments (python playerdata.py most_wickets_t20_world_cup_2024.csv "Jasprit Bumrah") demonstrates how the script retrieves and displays player statistics based on the provided CSV data.