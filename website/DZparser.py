import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="flex flex-col gap-2 py-6 first:pt-0")

        for item in news:
            title = item.find("h4").text.strip()
            href = item.find("a", class_="flex items-center gap-1 ml-2").get("href")
            author = item.find("a", class_="link").text
            date = item.find("time").text
            print(date)

            self.res.append({
                f"title": title,
                "href": href,
                "author": author,
                "date": date
            })

    def save(self):
        with open(self.path, "w", encoding='utf-8-sig') as f:
            i = 1
            for item in self.res:
                f.write(f"Новость № {i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}\n"
                        f"Автор: {item['author']}\nДата публикации: {item['date']}\n\n{"~" * 100}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


