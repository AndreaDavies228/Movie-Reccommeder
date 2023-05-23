import pandas as pd

df = pd.read_table('database.tsv')

def genre_filter(genre, df):
    if genre != "Any":
        df = df[df["genres"].str.contains(genre)]      
    return df

def length_filter(length, df):
    if length == "Short":
        df = df.loc[(df['runtimeMinutes'] < 60)]
    if length == "Medium":
        df = df.loc[(df['runtimeMinutes'] >= 60) & (df['runtimeMinutes'] <= 120)]
    if length == "Long":
        df = df.loc[(df['runtimeMinutes'] > 120)]
    return df

def decade_filter(decade, df):
    if decade == '60s':
        df = df.loc[(df['startYear'] >= 1960) & (df['startYear'] < 1970)]
    if decade == '70s':
        df = df.loc[(df['startYear'] >= 1970) & (df['startYear'] < 1980)]
    if decade == '80s':
        df = df.loc[(df['startYear'] >= 1980) & (df['startYear'] < 1990)]
    if decade == '90s':
        df = df.loc[(df['startYear'] >= 1990) & (df['startYear'] < 2000)]
    if decade == '2000s':
        df = df.loc[(df['startYear'] >= 2000) & (df['startYear'] < 2010)]
    if decade == '2010s':
        df = df.loc[(df['startYear'] >= 2010) & (df['startYear'] < 2020)]
    if decade == '2020s':
        df = df.loc[(df['startYear'] >= 2020)]   
    return df

def recommender_function(genre, length, decade, df=df):
    genre_filtered = genre_filter(genre, df)
    length_filtered = length_filter(length, genre_filtered)
    df = decade_filter(decade, length_filtered)

    df = df[["primaryTitle", "genres", "runtimeMinutes", "startYear", "averageRating"]]
    df = df.sort_values("averageRating", ascending = False)
    df = df.head(10) 
    return df

#print(recommender_function("Any", "Medium", "Any"))

 
