from jinja2 import Environment, FileSystemLoader


information = [
    {"type": "text", "name": "firstname", "placeholder": "Имя"},
    {"type": "text", "name": "lastname", "placeholder": "Фамилия"},
    {"type": "text", "name": "address", "placeholder": "Адрес"},
    {"type": "tel", "name": "phone", "placeholder": "Телефон"},
    {"type": "email", "name": "email", "placeholder": "Почта"},
]

file_loader = FileSystemLoader('macro_dz')
env = Environment(loader=file_loader)

tm = env.get_template('home.html')
msg = tm.render(information=information, title="Регистрация:")

print(msg)