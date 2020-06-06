import json

# Global controls
power_on = True
movie_library = []
movie_additions = []
movie_removals = []
library_file = "movie_library.json"


def load_data():
    global library_file, movie_library
    with open(library_file) as file_in:
        movie_library = json.load(file_in)
    with open(library_file, 'w') as file_in:
        file_in.truncate(0)
    return None


def add_movie():  # Finished for now.
    """Function for adding a movie to the library."""
    # TODO: Need to make this more sophisticated so that it can later use an arbitrary number of keys.
    global movie_additions
    name = input("What is the name of the movie? ").title()
    director = input("Who is the director of the movie? ").title()
    year = input("What year did the movie come out? ")
    dict_tmp = {"Name": name, "Director": director, "Year": year}
    if find_movie(dict_tmp):  # Check to make sure that the movie isn't already in the library.
        print('This movie has already been added.')
    else:
        movie_additions.append(dict_tmp)
        print('Movie added.')
    return None


def remove_movie(movie=None):  # Finished
    """Function for removing a movie from the library. If no input is given, the function will display a menu."""
    # TODO: add more sophisticated user inputs
    global movie_library, movie_removals
    found = False
    if movie is not None:
        for dic in movie_library:
            if dic == movie:
                movie_removals.append(dic)
                found = True
        if found:
            print("The movie has been removed.")
        else:
            print("No such movie in the list.")
    else:
        print("Right now, the program will only work if you enter the exact name of the movie.")
        movie_name = input("What movie would you like to remove? ")
        for dic in movie_library:
            if dic["Name"] == movie_name.title():
                movie_removals.append(dic)
                found = True
        if found:
            print("The movie has been removed.")
        else:
            print("No such movie in the list.")
    return None


def list_movies():  # Finished
    """Function for displaying the movies in the library."""
    global movie_library
    for movie in movie_library:
        print("")
        for key in movie.keys():
            print('{}: {}'.format(key, movie[key]))
        print("")
    return None


def find_movie(movie=None):  # Finished
    """Function for searching for a movie. If no input is given, the function will display a menu."""
    global movie_library, movie_additions
    found = False
    if movie is not None:
        for dic in movie_library:
            if dic == movie:
                found = True
        for dic in movie_additions:
            if dic == movie:
                found = True
    else:
        print("Currently we can only search by movie title.")
        movie_name = input("What movie would you like to look for? ")
        for movie in movie_library:
            if movie["Name"] == movie_name.title():
                found = True
                print("Here is the information we have about that movie.")
                print("")
                for key in movie.keys():
                    print('{}: {}'.format(key, movie[key]))
                print("")
    return found


def quit_program():  # Finished
    """Function for quitting the program."""
    global power_on
    power_on = False
    return None


def menu():  # Finished
    """Function for displaying the menu options to the user."""
    user_choice = input("Enter A to add a movie, R to remove a movie, L to list the movies in the library, "
                        "F to find a movie in the library, or Q to exit the program. ")
    menu_options = {"a": add_movie, "r": remove_movie, "l": list_movies, "f": find_movie, "q": quit_program}
    if user_choice.lower() in menu_options:
        chosen_function = menu_options[user_choice.lower()]
        chosen_function()
    else:
        print('Unknown selection.')
    return None


def display_changes():  # Finished
    """Function for displaying all the changes made during a session."""
    global movie_additions, movie_removals
    print("The following additions have been made during this session.")
    for movie in movie_additions:
        print("")
        for key in movie.keys():
            print('{}: {}'.format(key, movie[key]))
        print("")
    print("The following removals have been made during this session.")
    for movie in movie_removals:
        print("")
        for key in movie.keys():
            print('{}: {}'.format(key, movie[key]))
        print("")
    return None


def save_changes():
    """Function for saving the changes made during a session."""
    global movie_library, movie_additions, movie_removals
    movie_library += movie_additions
    movie_library = [dic for dic in movie_library if dic not in movie_removals]
    return None


def delete_changes():  # Finished
    """Functions for deleting all the changes made during a session."""
    global movie_additions, movie_removals
    movie_additions.clear()
    movie_removals.clear()
    return None


def save_data():
    with open(library_file, 'w') as file_in:
        json.dump(movie_library, file_in, indent=4)
    return None


if __name__ == "__main__":  # Finished
    load_data()
    while power_on:
        menu()
    display_changes()
    complete = False
    while not complete:
        choice = input('Press S to save the changes or D to delete the changes. ')
        if choice.lower() == "s":
            save_changes()
            complete = True
        elif choice.lower() == "d":
            delete_changes()
            complete = True
        else:
            print('Unknown selection.')
    save_data()
