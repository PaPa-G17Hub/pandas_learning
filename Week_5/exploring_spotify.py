import pandas as pd

df = pd.read_csv("spotify_songs.csv")
df.info()

print("df.shape")
print(df.shape)

print()
print(df.columns)

print("snapshot")
print()

print("\nhead")
print(df.head)

print("\ntop")
print()

print("\nNumber of each genre")
print(df["playlist_genre"].value_counts())

print("\nThe .mode function will return a dataframe's series")
print("\nThis is because there can be more than one value")
print(df["playlist_genre"].mode())

print("\nThis will display just the element value, but will not display possible other mode values")
print(df["playlist_genre"].mode()[0])

print("\nDisplays the median value")
print(df["duration_ms"].median())

print("\nDisplays the mean value")
print(df["duration_ms"].mean())

print("\nFind the max value")
print(df["duration_ms"].max())

print("\nFind the min value")
print(df["duration_ms"].min())

print("The range of 'duration_ms' is")
max_duration = df["duration_ms"].max()
min_duration = df["duration_ms"].min()
print(max_duration - min_duration)

print("\nFind the sum of these value")
print(df["duration_ms"].sum())

print("\nSorting the songs by duration length")
print(df.sort_values(by=["duration_ms"]))

# pd.set_option('display_max_rows',None)
print("\nSorting the songs by descending track name")
print(df.sort_values(by=["track_name"],ascending=False))

print("\nGrouping the songs by genre and displaying the minimun length")
print(df.groupby("playlist_genre")["duration_ms"].min())

print("\nUsing queries")
print(df.query("track_artist == 'Ricky Martin'"))

#displaying a query using a variable value needs to be prefixed by an "@" sign
mean_value = df["duration_ms"].mean()
sorted_songs_by_duration_df = df.sort_values(by=["duration_ms"])
print(sorted_songs_by_duration_df)
print(sorted_songs_by_duration_df.query("duration_ms > @mean_value"))