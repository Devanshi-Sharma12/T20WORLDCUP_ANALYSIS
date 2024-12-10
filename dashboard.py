import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("T20 World Cup 2024 Analysis")

    # Load data
    df = pd.read_csv("most_wickets_t20_world_cup_2024.csv")

    # Display data
    st.subheader("Player Stats")
    st.write(df)

    # Select player
    player = st.selectbox("Select a player:", df['Player'])
    player_stats = df[df['Player'] == player]
    st.write(player_stats)

    # Visualization
    st.subheader("Wickets Distribution")
    fig, ax = plt.subplots()
    ax.pie(df['Wickets'], labels=df['Player'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(df))))
    st.pyplot(fig)

if __name__ == "__main__":
    main()
