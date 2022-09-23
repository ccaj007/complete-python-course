
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

def View_Movies():
    for movie in movies:
        print_movie(movie)


def print_movie(m):
    print(f"Title: {m['title']}")
    print(f"Director: {m['director']}")
    print(f"Release year: {m['year']}")


def Find_Movie():
    inp = input('enter movie to find: ')
    for movie in movies:
        if movie["title"] == inp:
            print_movie(movie)
        else:
            print("Movie not found in inventory")


user_options = {
    "a": Add_Movie,
    "v": View_Movies,
    "f": Find_Movie
}


def menu():
    choice = input(MENU_PROMPT)
    while choice != 'q':
        if choice in user_options:
            selected_function = user_options[choice]
            selected_function()

        # if choice.lower() == 'a':
        #     Add_Movie()
        # elif choice.lower() == 'v':
        #     View_Movies(movies)
        # elif choice.lower() == 'f':
        #     Find_Movie()
        # elif choice.lower() == 'q':
        #     break
        else:
            print('Invalid choice')

        choice = input(MENU_PROMPT)


menu()