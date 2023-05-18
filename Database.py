import pandas as pd

basics = pd.read_table('title.basics.tsv.gz', compression = 'gzip', nrows = 10000)
#dtype ={'tconst': str, 'titleType': str, 'primaryTitle': str, 'originalTitle': str, 'isAdult': bool, 'startYear': int, 'endYear': int, 'runtimeMinutes': int, 'genres': str}
basics = basics[basics['titleType'] == 'movie']
#print(filtered_basics)
ratings = pd.read_table('title.ratings.tsv.gz', compression = 'gzip', nrows =10000)

database = pd.merge(basics, ratings, on =["tconst"])

print(database)


