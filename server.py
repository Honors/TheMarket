from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def main():
  return render_template('index.html')

app.run(host='0.0.0.0')

