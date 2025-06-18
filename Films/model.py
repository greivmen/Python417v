import pickle
import os


# , duration, atelier, actors
class Film:
    def __init__(self, title, genre, director, year_of_release, duration, atelier, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.duration = duration
        self.atelier = atelier
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"


class FilmModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.films = self.load_data()

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссер": film.director,
            "год выпуска": film.year_of_release,
            "длительность": film.duration,
            "студия": film.atelier,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def save_date(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)

        else:
            return dict()
