from store import *
from product import *

tiangge = Store("Marites' Tiangge")

shoes = Product("Nike Shoes", 8000, "Footwear")
shirt = Product("Anime T-Shirt", 200, "Men's Wear")
underwear = Product("Bacon Briefs", 150, "Men's Wear")
bag = Product("LV Bag", 100000, "Handbags")

tiangge.add_product(shoes).add_product(shirt).add_product(underwear).add_product(bag)
tiangge.inflation(.05)
tiangge.set_clearance("Men's Wear", .01)