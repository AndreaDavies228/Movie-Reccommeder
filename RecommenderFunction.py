from Database import database

def genre_filter(genre, database):
    return database

def length_filter(length, database):
    if length == "Short":
        database = database.loc[(database['runtimeMinutes'] < 60)]
    if length == "Medium":
        database = database.loc[(database['runtimeMinutes'] >= 60) & (database['runtimeMinutes'] <= 120)]
    if length == "Long":
        database = database.loc[(database['runtimeMinutes'] > 120)]
    return database

def decade_filter(decade, database):
    return database

def recommender_function(genre, length, decade, database=database):
    genre_filtered = genre_filter(genre, database)
    length_filtered = length_filter(length, genre_filtered)
    database = decade_filter(decade, length_filtered)

    database = database[["primaryTitle", "runtimeMinutes", "averageRating"]]
    database = database.sort_values("averageRating", ascending = False)
    database = database.head(10) 
    return database

#print(recommender_function("Any", "Medium", "Any"))

 
