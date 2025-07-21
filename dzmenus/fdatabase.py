import math
import time
import _sqlite3


class FDataMenu:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения БД")
        return []

    def add_post(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, text, tm))
            self.__db.commit()
            return True
        except _sqlite3.Error as e:
            print("Ошибка добавления игры в базу данных" + str(e))
            return False

    def get_post(self, post_id):
        try:
            self.__cur.execute(f"SELECT title, text FROM posts WHERE id = {post_id}")
            res = self.__cur.fetchone()
            if res:
                return res
        except _sqlite3.Error as e:
            print("Ошибка добавления игры в базу данных" + str(e))

        return False, False

    def get_posts_annonce(self):
        try:
            self.__cur.execute("SELECT id, title, text FROM posts ORDER BY time DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except _sqlite3.Error as e:
            print("Ошибка получения игры из базы данных" + str(e))

        return []
