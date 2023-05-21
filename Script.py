from Database import database
from RecommenderFunction import *

def genre_select():
    genre = False
    while genre == False:
        value = input("First, please select a genre. For a list of genres, please enter 'L'.")
        lower_value = value.lower()
        if value == "L" or value == 'l':
            print("""Action
            Adventure
            Animation
            Biography
            Comedy
            Crime
            Documentary
            Drama
            Family
            Fantasy
            History
            Horror
            Music
            Mystery
            News
            Romance
            Sci-Fi
            Sport
            Thriller
            War
            Western
            Any""")
            continue
        if lower_value == "action":
            genre = "Action"
        if lower_value == "adventure":
            genre = "Adventure"        
        if lower_value == "animation":
            genre = "Animation"
        if lower_value == "biography":
            genre = "Biography"
        if lower_value == "comedy":
            genre = "Comedy"
        if lower_value == "crime":
            genre = "Crime"
        if lower_value == "documentary":
            genre = "Documentary"
        if lower_value == "drama":
            genre = "Drama"
        if lower_value == "family":
            genre = "Family"
        if lower_value == "fantasy":
            genre = "Fantasy"
        if lower_value == "history":
            genre = "History"
        if lower_value == "horror":
            genre = "Horror"
        if lower_value == "music":
            genre = "Music" 
        if lower_value == "mystery":
            genre = "Mystery"
        if lower_value == "news":
            genre = "News"
        if lower_value == "romance":
            genre = "Romance"   
        if lower_value == "sci-fi":
            genre = "Sci-Fi"
        if lower_value == "sport":
            genre = "Sport"
        if lower_value == "thriller":
            genre = "Thriller"
        if lower_value == "war":
            genre = "War"
        if lower_value == "western":
            genre = "Western"
        if lower_value == "any":
            genre = "Any"         
        else:
            print("Invalid value. For a list of genres please press 'L'.")
    return genre

def length_select():
    length = False
    while length == False:
        value = input("How long would you like the movie to be? Please select 'short' (under one hour), 'medium' (between one and two hours), 'long' (over two hours) or 'any'.")
        value = value.lower()
        if value == 'short':
            length = 'Short'
        if value == 'medium':
            length = "Medium"
        if value == 'long':
            length = 'Long'
        if value == 'any':
            length = 'Any Length'
        if value == 'Any':
            length = 'Any Length'
        else:
            print("Invalid value. Please select 'short' (under one hour), 'medium' (between one and two hours), 'long' (over two hours) or 'any'.")
    return length

def decade_select():
    decade = False
    while decade == False:
        value = input("What decade would you like to watch a movie from? Please select '60s', '70s', '80s', '90s', '2000s', '2010s','2020s' or 'Any'.")
        if value == '60s':
            decade = '60s'
        if value == '70s':
            decade = '70s'
        if value == '80s':
            decade = '80s'
        if value == '90s':
            decade = '90s'
        if value == '2000s':
            decade = '2000s'
        if value == '2010s':
            decade = '2010s'
        if value == '2020s':
            decade = '2020s'    
        if value == 'any':
            decade = 'Any'
        if value == 'Any':
            decade = 'Any'      
        else:
            print("Invalid value. Please select '60s', '70s', '80s', '90s', '2000s', '2010s','2020s' or 'Any'.")
    return decade

def end_function():
    input_check = False
    while input_check == False:
        end_value = input("Thank you for using this movie recommender. If you would like to run a new search, press 'N', if you would like to quit, press 'Q'.")
        end_value = end_value.lower()
        if end_value == 'n':
            input_check = True
            continue
        if end_value == 'q':
            exit()
        else:
            print("Invalid input. Please press 'N' or 'Q'.")


running = True        
while running == True:
    print("Welcome to the movie recommender service. We will help you find a movie to watch from the imdb database, based on how you answer some simple questions.")
    genre = genre_select()
    print("You have selected " + genre + ".")
    length = length_select()
    print("You have selected " + length + " .")
    decade = decade_select()
    print("You have selected " + decade + " .")
    print("We will now find the top ten rated films matching your critera, with at least 1000 reviews. Please wait.")
    print(recommender_function(genre, length, decade))
    end_function()




         


