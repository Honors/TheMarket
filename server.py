from flask import Flask
from flask import render_template
from data import data
app = Flask(__name__, static_url_path='')

@app.route('/')
def main():
  return render_template('home.html')

@app.route('/menu/<menu>')
def menu(menu):
  d = data[menu]
  return render_template('menu.html',
    menu_key=menu,
    menu_title=d["menu_title"],
    summary=d["summary"],
    items=d["items"],
    images=d["images"])

app.run(host='0.0.0.0', debug=True)

