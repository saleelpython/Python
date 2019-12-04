import csv
import json
import pandas
import os



#region Pandas 
df = pandas.read_csv("movie.csv", names = ["movieColorType", "director", "critic", "duration", "director_facebook_likes","actor_3_facebook_likes", "actor_2_name", "actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords",	"movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"], header=None)

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)
# pandas.set_option("display.max_colwidth", 60)
pandas.set_option("display.width", None)

# x = df["language"].unique()

# for i in x:
#     print(i)

print(df[["movieColorType", "movie_title", "language", "country", "director", "critic", "duration"]])
#endregion





