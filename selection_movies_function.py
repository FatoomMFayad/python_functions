import math
def selection_movies_function(movies):
    budgets = []
    total = sum(float(movie[1]) for movie in movies)
    avg = total/len(movies)
    higher_movies = []
    for movie in movies:
        if movie[1] > avg:
            higher_movies.append((movie[0], movie[1] - avg))
    return avg, higher_movies, len(higher_movies)
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
print(selection_movies_function(movies))