from flask import Flask
from flask import render_template
from data import data
app = Flask(__name__, static_url_path='')

@app.route('/')
def main():
  return "Hello"

@app.route('/menu/<menu>')
def menu(menu):
  data = data[menu]
  return render_template('menu.html',
    menu_title=data["menu_title"],
    summary=data["summary"],
    items=data["items"],
    images=data["images"])

app.run(host='0.0.0.0')

