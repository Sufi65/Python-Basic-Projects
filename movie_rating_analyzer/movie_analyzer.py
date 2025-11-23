import pandas as pd

def movie_rating_analyzer():
    df = pd.read_csv("movie_ratings.csv")

    print("=== Movie Rating Analyzer ===\n")
    print(df)

    avg_rating = df["rating"].mean()
    highest = df.loc[df["rating"].idxmax()]
    lowest = df.loc[df["rating"].idxmin()]

    print("\nAverage Rating:", round(avg_rating, 2))
    print("Highest Rated Movie:", highest["movie"], "-", highest["rating"])
    print("Lowest Rated Movie:", lowest["movie"], "-", lowest["rating"])

if __name__ == "__main__":
    movie_rating_analyzer()
    
    
    #python .\movie_analyzer.py
