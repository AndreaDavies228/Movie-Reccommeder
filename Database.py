import pandas as pd

basics = pd.read_table('title.basics.tsv.gz', compression = 'gzip', usecols = ['tconst','titleType','primaryTitle', 'startYear', 'runtimeMinutes', 'genres'], dtype ={'tconst': str, 'titleType': str, 'primaryTitle': str, 'startYear': str, 'runtimeMinutes': str, 'genres': str})
#dtype ={'tconst': str, 'titleType': str, 'primaryTitle': str, 'originalTitle': str, 'isAdult': bool, 'startYear': int, 'endYear': int, 'runtimeMinutes': int, 'genres': str}
basics = basics[basics['titleType'] == 'movie']
#print(filtered_basics)
ratings = pd.read_table('title.ratings.tsv.gz', compression = 'gzip', dtype ={'tconst': str, 'averageRating': str, 'numVotes': str})

database = pd.merge(basics, ratings, on =["tconst"])

database.drop(database[database['runtimeMinutes'] == r"\N"].index, inplace = True)
database[['runtimeMinutes']] = database[['runtimeMinutes']].apply(pd.to_numeric)

database.drop(database[database['numVotes'] == r"\N"].index, inplace = True)
database[['numVotes']] = database[['numVotes']].apply(pd.to_numeric)
database = database.loc[(database['numVotes'] >= 1000)]

database.drop(database[database['startYear'] == r"\N"].index, inplace = True)
database[['startYear']] = database[['startYear']].apply(pd.to_numeric)


database.to_csv('database.tsv', sep="\t")


