# Netflix Graduation Project - EDA, Statistical Analysis & KPIs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUT = r"/mnt/data/Netflix_Cleaned_Final excel (1).xlsx"

df = pd.read_excel(INPUT, sheet_name="Cleaned_Data")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum().sort_values(ascending=False))

# KPIs
movies = df[df["type"] == "Movie"]
tv = df[df["type"] == "TV Show"]

print("\n--- KPIs ---")
print("Total titles:", len(df))
print("Movies:", len(movies))
print("TV Shows:", len(tv))
print("Movie share:", round(len(movies)/len(df)*100, 2), "%")
print("TV share:", round(len(tv)/len(df)*100, 2), "%")

# Genre analysis
genres = df["listed_in"].dropna().str.split(", ").explode()
print("\nTop 10 genres/categories:\n", genres.value_counts().head(10))

# Country analysis
countries = df["country"].dropna().str.split(", ").explode()
print("\nTop 10 countries:\n", countries.value_counts().head(10))

# Ratings
print("\nTop ratings:\n", df["rating"].value_counts().head(10))

# Statistical analysis
movie_duration = movies["duration_value"].dropna()
print("\n--- Movie duration statistics ---")
print("Mean:", movie_duration.mean())
print("Median:", movie_duration.median())
print("Standard deviation:", movie_duration.std())
print("Minimum:", movie_duration.min())
print("Maximum:", movie_duration.max())

print("\n--- Release year statistics ---")
print(df["release_year"].describe())

# Charts
df["type"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Movies vs TV Shows")
plt.ylabel("")
plt.show()

genres.value_counts().head(10).sort_values().plot(kind="barh", title="Top 10 Genres")
plt.xlabel("Number of titles")
plt.show()

countries.value_counts().head(10).sort_values().plot(kind="barh", title="Top 10 Countries")
plt.xlabel("Number of titles")
plt.show()

df["year_added"].value_counts().sort_index().plot(marker="o", title="Titles Added by Year")
plt.ylabel("Titles added")
plt.show()

movie_duration.plot(kind="hist", bins=25, title="Movie Duration Distribution")
plt.xlabel("Minutes")
plt.show()
