import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("most_wickets_t20_world_cup_2024.csv")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1) 
plt.bar(df['Player'], df['Wickets'], color='skyblue', edgecolor='black')
plt.xlabel('Player')
plt.ylabel('Wickets')
plt.title('Top Wicket Takers in T20 World Cup 2024')
plt.xticks(rotation=45, ha='right')

plt.subplot(1, 2, 2)  
plt.pie(df['Wickets'], labels=df['Player'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(df))))
plt.title('Wickets Distribution among Players')

plt.tight_layout()

plt.show()
