from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "index.html", {"treasures": treasures})


"""
treasures = [
	Treasure("Gold Nugget", 500.00, "gold", "Curly's Creek, NM", "http://staffordcountymuseum.com/wp-content/uploads/2014/02/gold-nugget-2.jpg"),
	Treasure("Fool's Gold", 0, "pyrite", "Fool's Falls, CO", "http://www.gemstonebuzz.com/files/gemstone/pyrite-cube.jpg"),
	Treasure("Coffee Can", 20.00, "tin", "Acme, CA", "http://italianfoodmaterialsandmachinery.com/files/2014/06/CoffeeCan_300dpi.png")
]		"""