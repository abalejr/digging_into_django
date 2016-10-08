from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request):
	treasures = Treasure.objects.all()
	return render(request, "index.html", {"treasures": treasures})

def details(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request, "details.html", {"treasure": treasure})


"""
treasures = [
	Treasure(name="Gold Nugget", value=500.00, material="gold", location="Curly's Creek, NM", img_url="http://staffordcountymuseum.com/wp-content/uploads/2014/02/gold-nugget-2.jpg"),
	Treasure(name="Fool's Gold", value=0, material="pyrite", location="Fool's Falls, CO", img_url="http://www.gemstonebuzz.com/files/gemstone/pyrite-cube.jpg"),
	Treasure(name="Coffee Can", value=20.00, material="tin", location="Acme, CA", img_url="http://italianfoodmaterialsandmachinery.com/files/2014/06/CoffeeCan_300dpi.png")
]		"""