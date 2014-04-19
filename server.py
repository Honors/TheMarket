from flask import Flask, render_template, redirect, request
from data import getData, setData
import json
app = Flask(__name__, static_url_path='')

def isProductType(a):
  return isinstance(a, dict) or isinstance(a, list)
def updateData(patch, data):
  if not isProductType(patch):
    return patch
  elif isinstance(patch, list):
    return patch
  else:
    for k, v in patch.iteritems():
      data[k] = updateData(v, data[k])
    return data
@app.route('/update', methods=['POST'])
def update():
  patch = json.loads(request.data)
  setData(updateData(patch, getData()))
  return json.dumps(getData())

@app.route('/')
def main():
  return render_template('home.html')

@app.route('/service')
def service():
  data = getData()
  return render_template('service.html',
    items=data["service"]["items"])

@app.route('/events')
def events():
  data = getData()
  return render_template('events.html',
    summary=data["events"]["summary"],
    items=data["events"]["items"])

@app.route('/catering')
def catering():
  data = getData()
  return render_template('catering.html',
    summary=data["catering"]["summary"],
    items=data["catering"]["items"])

@app.route('/menus')
def menus():
  return redirect('/menu/bakery')

@app.route('/menu/<menu>')
def menu(menu):
  data = getData()
  d = data["menus"][menu]
  return render_template('menu.html',
    menus=data["menus"],
    menu_key=menu,
    menu_title=d["menu_title"],
    summary=d["summary"],
    items=d["items"],
    images=d["images"])

app.run(host='0.0.0.0', port=3084, debug=True)

