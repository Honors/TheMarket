from flask import Flask
from flask import render_template
app = Flask(__name__, static_url_path='')

@app.route('/')
def main():
  return render_template('menu.html',
    items=[
      {"name":"Fresh cut deli meats",
       "description":""},
      {"name":"House-made sauces &amp; toppings",
       "description":"Available for retail. Sell at other retail stores."},
      {"name":"Artisanal cheeses",
       "descritption":"Local &amp; International. Available for retail."},
      {"name":"Daily specials",
       "description":"Daily market-fresh fish &amp; meats."},
      {"name":"Artisanal Pizza",
       "description":"""
	  Hand-made Sicilian style pizza with hand-picked toppings.<br>
	  Available all day &amp; Take 'n Bake program.<br>
	  Sell at other retail locations.
	"""},
      {"name":"Salad Station",
       "description":"""
	  Salad bar &amp; Build your own &amp; Take home.<br>
	  Fresh grown produce locally sourced or home-grown when possible.
       """},
      {"name":"Sandwiches",
       "description":"Original deli sandwich selection with daily specials."}],
    images=["pasta.png", "pizza.png", "bread.png"])

app.run(host='0.0.0.0')

