# Task 1
# Create the years and durations lists
years = list(range(2011, 2021))
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {
    "years": years,
    "durations": durations
}

# Print the dictionary
print(movie_dict)

# Task 2
# Import pandas under its usual alias
import pandas as pd

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame
print(durations_df)
       
 #Task 3      
 # Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt

# Draw a line plot of release_years and durations
plt.plot(durations_df["years"], durations_df["durations"])

# Create a title
plt.title("Netflix Movie Durations 2011-2020")

# Create a line plot of the data with the years column of durations_df on the xaxis, and the durations column on the y-axis
plt.xlabel("Year")
plt.ylabel("Duration")

# Show the plot
plt.show()
   
# Task 4
# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("datasets/netflix_data.csv")

# Print the first five rows of the DataFrame
print(netflix_df.head())

 # Task 5
# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies_col_subset = {100}

# Print the first five rows of the new DataFrame
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]
print(netflix_movies_col_subset.head())

# Task 6
# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])

# Create a title
plt.title("Movie Duration by Year of Release")


# create a scatter plot, placing the release_year on the x-axis and the movie duration on the y-axis. 
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

# Task 7
# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]

# Print the first 20 rows of short_movies
print(short_movies.head(20))

# Task 8
# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for genre in netflix_movies_col_subset["genre"]:
    if genre == "Children":
        colors.append("red")
    elif genre == "Documentaries":
        colors.append("blue")
    elif genre == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Inspect the first 10 values in your list
print(colors[:10])

# Task 9
# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], c=colors)

# Create a title and axis labels
plt.title("Movie Duration by Year of Release")

# Show the plot
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()

# Task 10
# Are we certain that movies are getting shorter?
are_movies_getting_shorter = False



