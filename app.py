import csv
import json
import pandas
import numpy 



#region Pandas 
df = pandas.read_csv("movie.csv", names = ["movieColorType", "director", "critic", "duration", "director_facebook_likes","actor_3_facebook_likes", "actor_2_name", "actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords",	"movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"], header=None)

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)
pandas.set_option("display.max_colwidth", 20)
pandas.set_option("display.width", None)

df.fillna(value={"duration" : 0, "director":"Not Available","genres":"Not Available"},inplace=True)


# print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "actor_2_name","plot_keywords","imdb_score"]])

# print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "actor_2_name","plot_keywords","imdb_score"]][(df['duration'] == 100) & (df["movieColorType"] == 'Black and White')])

# print(df[["movieColorType","director","duration"]] [df["duration"] == 100].count()) #.to_string(index=False))

# print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "actor_2_name","plot_keywords","imdb_score","content_rating"]] [((df["content_rating"] =='PG-13') | (df["content_rating"] == 'U/A')) & (df["duration"] == 10_0)])


# print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "actor_2_name","plot_keywords","imdb_score","content_rating"]][df["content_rating"].isin(["PG-13", "U/A"])])

print(df[["movieColorType" , "director", "critic", "duration", "movie_title", "genres", "plot_keywords","imdb_score","content_rating"]])


#endregion





