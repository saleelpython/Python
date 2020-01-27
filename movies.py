import pandas
import numpy
import sys

df = pandas.read_csv("movie.csv", names=["_id", "relese", "color", "director","critic","duration","director_facebook","actor_3_facebook","actor_2_name",	"actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords",	"movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes","production houses"], header=None, nrows=45)

numpy.set_printoptions(threshold=sys.maxsize)

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_colwidth',17)
pandas.set_option('display.width', None)
# pandas.set_option('display.precision',2)

df.fillna(value={"title_year":0,"critic":0,"duration":0, "gross":0, "budget":0}, inplace=True)

# Convert the float to int 
df["title_year"] = df["title_year"].astype(int)
df["critic"] = df["critic"].astype(int)
df["duration"] = df["duration"].astype(int)
df["gross"] = df["gross"].astype(int)
df["budget"] = df["budget"].astype(int)

df.index = ["IndexID : " + str(i) for i in range(df["_id"].count())]

#Q1) Dsiplay "_id", "relese", "color", "movie_title", "director","critic","duration","gross","genres","language","country","content_rating","budget","title_year","production houses"
print(df[["_id", "relese", "color", "movie_title", "director","critic","duration","gross","genres","language","country","content_rating","budget","title_year","production houses"]])

#Q2) Display all movies whose language is "English"
print(df[["_id", "relese", "color", "movie_title", "director","critic","duration","gross","genres","language","country","content_rating","budget","title_year","production houses"]] [df["language"]=='English'])

#Q3) Display all movies whose language is "English" AND country is "New Zealand"
print(df[["_id", "relese", "color", "movie_title", "director","critic","duration","gross","genres","language","country","content_rating","budget","title_year","production houses"]] [(df["language"]=='English') & (df["country"] == 'New Zealand')])

#Q4) Display all movies whose language is "English" AND country is either "New Zealand" OR "Canada"
print(df[["_id", "relese", "color", "movie_title", "director","critic","duration","gross","genres","language","country","content_rating","budget","title_year","production houses"]] [(df["language"]=='English') & ((df["country"]=='New Zealand') | (df["country"]=='Canada'))])

#Q5) Change DataFrame Index to "director" name
df.index = df["director"]

#Q6) Dsiplay the data whose DateFrame Indes is "James Cameron" and display movie title and the production house name
print(df.loc["James Cameron"] [["movie_title","production houses","critic","duration","language","country"]])

#Q7) Dsiplay the data whose DateFrame Indes is "James Cameron" and display movie title and the production house name
#TODO sys.argv we muse import sys module
print(df.loc[sys.argv[1]] [["movie_title","production houses","critic","duration","language","country"]])

#Q8)


#Q9)


#Q10)


#Q11)


#Q12)


#Q13)


#Q14)


#Q15)


#Q16)


#Q17)


#Q18)


#Q19)


#Q20)

