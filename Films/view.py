def aad_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:
    @aad_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        print("Действие с фильмами:")
        print("1 - добавление фильма :"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @aad_title(" Создание фильма: ")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссера": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }

        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        return dict_film

    @aad_title(" Список фильмов: ")
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    @aad_title("Ввод названия фильма:")
    def get_user_film(self):
        return input("Введите название фильма: ")

    @aad_title("Просмотр фильма")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @aad_title("Сообщение об ошибке:")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм с названием {user_title} не существует")

    @aad_title("Удаление фильма")
    def remove_single_film(self, film):
        print(f"Фильм {film} была удален")

    @aad_title("Сообщение об ошибке:")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")




