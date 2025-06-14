from DZparser import Parser


def main():
    for i in range(1, 3):
        pars = Parser(f"https://shazoo.ru/news?page={i}", "gaming news.txt")
        pars.run()


if __name__ == "__main__":
    main()
