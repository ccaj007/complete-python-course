
MENU_PROMPT = """
    Enter a choice
    Add a movie > a
    View all movies > v
    Find a movie > f
    Quit > q
    >>
"""

#movies = {"title":[],"director":[],"year":[]}
movies = []

def Add_Movie():
    title = input('enter movie title: ')
    director = input('enter director: ')
    year = input ('enter year: ')

    movies.append({

        "title":title,
        "director":director,
        "year":year
    })

    return movies

def View_Movies(movies):
    for movie in movies:
        print(movie)

def Find_Movie():
    inp = input('enter movie to find: ')
    if inp in movies["title"]:
        print(movies["title"], movies["director"], movies["year"])
    else:
        print("Movie not found in inventory")

choice = input(MENU_PROMPT)
while choice != 'q':
    if choice.lower() == 'a':
        Add_Movie()
    elif choice.lower() == 'v':
        View_Movies(movies)
    elif choice.lower() == 'f':
        Find_Movie()
    elif choice.lower() == 'q':
        break
    else:
        print('Invalid choice')

    choice = input(MENU_PROMPT)


