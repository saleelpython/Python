import pandas

# df = pandas.read_csv("movie.csv", names=["color", "director","critic","duration","director_facebook","actor_3_facebook","actor_2_name",	"actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords",	"movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes","new_movie_facebook_likes"], header=None )

# pandas.set_option("display.max_rows", None)
# pandas.set_option("display.max_columns", None)
# pandas.set_option("display.max_colwidth", 15)
# pandas.set_option("display.width", None)


# # print(df[["color","movie_title","critic","director","duration","language","country","content_rating","budget","aspect_ratio","movie_facebook_likes","new_movie_facebook_likes"]])

# df["new_movie_facebook_likes"] = df["movie_facebook_likes"] + 1



# print(df[["movie_facebook_likes", "new_movie_facebook_likes"]])

# df = pandas.DataFrame([
#     {"_id":1, "indexID": "1001", "firstName": "Saleel", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
#     {"_id":2,"indexID": "1002", "firstName": "Vrushali", "lastName": "Bagde", "canVote": "True", "canDrive": "False"}, 
#     {"_id":3,"indexID": "1003", "firstName": "Sharmin", "lastName": "Bagde", "canVote": "True", "canDrive": "True"}, 
#     {"_id":4,"indexID": "1004", "firstName": "Nitish", "lastName": "Patil", "canVote": "True", "canDrive": "True"}, 
#     {"_id":5,"indexID": "1005", "firstName": "Neel", "lastName": "Save", "canVote": "False", "canDrive": "True"}, 
#     {"_id":6,"indexID": "1006", "firstName": "Deep", "lastName": "Save", "canVote": "False", "canDrive": "False"}, 
#     {"_id":7,"indexID": "1007", "firstName": "Ruhan", "lastName": "Bagde", "canVote": "False", "canDrive": "False"}
# ], columns=["_id", "indexID", "firstName", "lastName", "canVote", "canDrive", "haveCard"])

# print(df["haveCard"])

code_dict = {'..-': 'U', '--..--': ', ', '....-': '4', '.....': '5',
'-...': 'B', '-..-': 'X', '.-.': 'R', '--.-': 'Q',
'--..': 'Z', '.--': 'W', '-..-.': '/', '..---': '2',
'.-': 'A', '..': 'I', '-.-.': 'C', '..-.': 'F',
'---': 'O', '-.--': 'Y', '-': 'T', '.': 'E',
'.-..': 'L', '...': 'S', '-.--.-': ')',
'..--..': '?', '.----': '1', '-----': '0',
'-.-': 'K', '-..': 'D', '----.': '9',
'-....': '6', '.---': 'J', '.--.': 'P',
'.-.-.-': '.', '-.--.': '(', '--': 'M',
'-.': 'N', '....': 'H', '---..': '8',
'...-': 'V', '--...': '7',
'--.': 'G', '...--': '3', '-....-': '-'}

string = "SALEEL"

# for key, value in code_dict.items():
#     print (f'{key}   {value}')

x = ""

for i in string:
    for key, value in code_dict.items():
        if i == value :
            x = x  + key + " "

print(x)


