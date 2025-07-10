from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('DZmacro')
env = Environment(loader=file_loader)

tm = env.get_template('home.html')
msg = tm.render()

print(msg)
