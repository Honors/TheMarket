from flask import Flask, render_template, redirect
from data import data
app = Flask(__name__, static_url_path='')

@app.route('/')
def main():
  return render_template('home.html')

@app.route('/service')
def service():
  return render_template('service.html',
    items=data["service"]["items"])

@app.route('/events')
def events():
  return render_template('events.html',
    summary=data["events"]["summary"],
    items=data["events"]["items"])

@app.route('/catering')
def catering():
  return render_template('catering.html',
    summary=data["catering"]["summary"],
    items=data["catering"]["items"])

@app.route('/menus')
def menus():
  return redirect('/menu/deli')

@app.route('/menu/<menu>')
def menu(menu):
  d = data["menus"][menu]
  return render_template('menu.html',
    menus=data["menus"],
    menu_key=menu,
    menu_title=d["menu_title"],
    summary=d["summary"],
    items=d["items"],
    images=d["images"])

app.run(host='0.0.0.0', debug=True)

