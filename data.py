def getData():
  return data
def setData(d):
  data = d
data = {
  "service": {
    "items": [
      {"name": "Daytime = self-serve",
       "description": """
	 Walk up ordering. Food will be brought to tables.<br>
	 Bussers working/cleaning open to close
       """},
      {"name": "Dinner Service",
       "description": """
	 THE CREST GASTROPUB STYLE<br>
	 (5pm-10pm weekdays)<br>
	 Table Service / Host / Bussers
	"""},
      {"name": "Weekend brunch &amp; dinner",
       "description": "Full table service all day"},
      {"name": "Stations",
       "description": """
	 All stations will have specific employees ready to serve our customers<br>
	 Butcher / Deli Station | Pizza / pasta / salad | Cafe / bar / check-out station
       """}]
  },
  "catering": {
    "summary": """
      Catering is not only taking your restaurant market outside of the box,
      but also another way to help promote and expand our brand throughout our
      city.
    """,
    "items": [
      {"name": "Delivery Services",
       "description": ""},
      {"name": "Special events menus",
       "description": "birthdays / graduations / holidays etc."},
      {"name": "Seasonal holiday catered meals",
       "description": """
	 Providing full holiday meals<br>
	 All catering menu items will be made at Cafe Del Mondo
       """}]
  },
  "events": {
    "summary": """
      Continue our commitment to be a part of our community.
    """,
    "items": [
      {"name": "Commitment to collaborate with food business &amp; farmers",
       "description": ""},
      {"name": "Community Engagement",
	"description": ""},
      {"name": "Education",
       "description": ""}]
  },
  "menus": {
    "butcher": {
      "menu_title": "Butcher",
      "summary": """
	Full service butcher that supplies grass fed, gmo free produce for both a
	retail &amp; restaurants environment. Having the use of the butcher shop
	at the market will also enhance the quality in our current restaurants.
      """,
      "items": [
	{"name":"Sustainable/Non GMO farm raised",
	 "description":""},
	{"name":"Dry-Aged Beef",
	 "description":""},
	{"name":"Cured Meats",
	 "description":""},
	{"name":"Fresh Cuts",
	 "description":""},
	{"name":"House-made sausage",
	 "description":""}
      ],
      "images": ["/images/butcher.png"]
    },
    "deli": {
      "menu_title":"Deli",
      "summary":"""
	Offering a large array of artisan deli meats &amp; cheeses, we 
	will have a focus on European style meats and cheeses as well as
	those from the local market.
      """,
      "items":[
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
       "images": ["/images/pasta.png", "/images/pizza.png", "/images/bread.png"]
    },
    "bakery": {
      "menu_title": "Bakery",
      "summary": """
	We have recently been working hard to get our bakery, "Pour Le Paysans"
	located at Cafe Del Mondo up and running. Our goal is to entirely produce
	our own baked goods for our company, retail, &amp; selling our artisan
	baked goods elsewhere in the city.
      """,
      "items": [
	{"name":"Fresh daily, artisanal baked goods",
	 "description":""},
	{"name":"Everything we produce available in retail environment",
	 "description":""},
	{"name":"Pasteries &amp; Sweets",
	 "description":""}
      ],
      "images": ["/images/bakery_bread.png"]
    },
    "cafe": {
      "menu_title": "Cafe",
      "summary": """
	Continuously expanding our knowledge &amp; resources in the Coffee Scene.
	Utilizing our new business principals of local love &amp; sustainability.
      """,
      "items": [
	{"name":"Locally roasted/direct-trade coffees &amp; teas",
	 "description":""},
	{"name":"Traditional cafe drink &amp; menu",
	 "description":""},
	{"name":"Expanding our knowledge into our beverage program",
	 "description":""},
	{"name":"Iced-Coffee To-Go",
	 "description":""}
      ],
      "images": ["/images/coffee.png"]
    },
    "restaurant": {
      "menu_title": "Restaurant",
      "summary": """
	A chef driven, weekly menu, with a European flavor made with locally
	sourced ingredients.
      """,
      "items": [
	{"name":"Locally roasted/direct-trade coffees &amp; teas",
	 "description":"""
	   Focus on locally sourced/grown-by-us ingredients<br>
	   directly corresponds with butcher/deli/retail<br>
	   15 items or less/Small plates with focus on presentation<br>
	   French/Italian dishes &amp; flavors | Daily pasta / steak / fish specials
	 """},
	{"name":"Traditional cafe drink &amp; menu",
	 "description":"""
	   Weekdays 5pm-10pm / business not directly focused on
	   restaurant as a whole
	 """},
	{"name":"Expanding our knowledge into our beverage program",
	 "description":"""
	   9am-3pm brunch menu / closed 3pm-5pm / dinner 5pm-10pm<br>
	   Create new brunch / weekend destination for young, up
	   and coming Italian village
	 """}
      ],
      "images": ["/images/restaurant.png"]
    },
    "bar": {
      "menu_title": "Bar",
      "summary": """
	Being consistent with our business model at The Market, our bar service
	will consist of artisah cocktails, craft beers, &amp; worldly wines
	backed by a knowledgable staff.
      """,
      "items": [
	{"name":"Craft Oriented beer selection",
	 "description":"""
	   20 Tap handles | Using state of the art craft tap system
	 """},
	{"name":"Small variety of Top-Shelf liquers",
	 "description":"""
	   Barel-aging / Creative cocktail creation
	 """},
	{"name":"Hand-Picked Wine Selection",
	 "description":"""
	   Available by the glass or by the bottle
	 """}
      ],
      "images": ["/images/retail_drinks.png"]
    },
    "retail": {
      "menu_title": "Retail",
      "summary": """
	Our goal is to have most of what we make &amp; use in-house available to
	the public in the retail environment.
      """,
      "items": [
	{"name":"Every Product / recipe available for retail",
	 "description":"""
	   Sauces | Salads | Pastas | Breads | House-Picked Pickles |
	   Spices &amp; Seasonings | NUTS! + MORE
	 """},
	{"name":"Ready-to-go Meals",
	 "description":"""
	   Take 'n Bake Pizzas | Salads | Sandwiches + MORE
	 """},
	{"name":"Retail Beverages",
	 "description":"""
	   Large selection of Craft oriented beers<br>
	   Large wine selection with a worldly influence and focus on
	   presigious regions<br>
	   Focus on artisanal sodas &amp; non-alcoholic beverages
	 """}
      ],
      "images": ["/images/retail_shelves.png", "/images/retail_drinks.png"]
    },
    "produce": {
      "menu_title": "Produce",
      "summary": """
	Our ability to grow food is, well, growing.. Growing our own produce and
	our relationship with local farmers is what makes us stand out above
	everything else.
      """,
      "items": [
	{"name":"Produce grown by us &amp; locally sourced",
	 "description":"""
	   Fresh, controlled, selection based on availibility in a 
	   small grocery store setting<br>
	   Utilizing this new location to organize our prodce movement
	   throughout the company
	 """},
	{"name":"CSA Program",
	 "description":"""
	   CSA: Commmunity-supported agriculture is a food production and
	   distribution system that directly connects farmers and consumers.
	   Consumers buy shares in a farm's harvest in advance.
	 """},
      ],
      "images": ["/images/produce.png"]
    }
  }
}

