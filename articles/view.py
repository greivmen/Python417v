def aad_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*args, **kwargs)

            return output

        return wrap

    return wrapper


class UserInterface:
    @aad_title("Ввод пользовательских данных")
    def wait_user_answer(self):

        print("Действие со статьями:")
        print("1 - создание статьи:"
              "\n2 - просмотр статей"
              "\n3 - просмотр определенной статьи"
              "\n4 - удаление статьи"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @aad_title(" Создание статьи: ")
    def add_user_article(self):
        dict_article = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }

        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")
        return dict_article

    @aad_title(" Список статей: ")
    def show_all_articles(self, articles):
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")

    @aad_title("Ввод названия статьи:")
    def get_user_article(self):
        return input("Введите название статьи: ")

    @aad_title("Просмотр статьи")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} статьи - {article[key]}")

    @aad_title("Сообщение об ошибке:")
    def show_incorrect_title_error(self, user_title):
        print(f"Статья с названием {user_title} не существует")

    @aad_title("Удаление статьи")
    def remove_single_article(self, article):
        print(f"Статья {article} была удалена")


