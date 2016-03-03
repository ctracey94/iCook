'''
App_Initializer.py

Author: Conor Tracey

Created: 		2/26/2016
Latest Update: 	3/02/2016

A module defining the App_Initializer object for the iCook application. This object
runs boot operations for iCook. These include checking that the proper filesystem is
in place, and nothing else so far.
'''

# Standard Library Imports
import os, stat

# Local Imports
import Recipe, Recipe_Reader

# MAC OSX path to iCook file library
OSX_PATH = os.path.expanduser("~/Library/Application Support/iCook/")


class App_Initializer:

	def __init__(self):
		types = []
		return None

	def make_file_sys(self):
		'''
		(None) -> None

		Creates a default filesystem, with default recipes and types. For use in
		first-time setup
		'''

		#make main directory
		os.makedirs(OSX_PATH)

		#make a file for recipe types
		type_file = open(OSX_PATH + "types", "w+")

		#load default types into memory
		self.types = ['Entree', 'Dessert', 'Appetizer', 'Drink', 'Breakfast', 'Lunch', 'Side']

		#write default types
		for type in self.types:
			type_file.write(type + '\n')

		type_file.close()

		#make a file for recipes
		recipe_file = open(OSX_PATH + "recipes", "w+")

		###### LOAD DEFAULT RECIPES ######

		banana_cream_pie = Recipe.Recipe(name = "Banana Cream Pie", type = "Dessert")
		banana_cream_pie.ingredients = ["1 cup sugar","1/4 cup corn starch","1/2 teaspoon salt",\
								"3 cups 2% milk", "2 large eggs, lightly beaten","3 tablesoons butter",\
								"1-1/2 teaspoons vanilla extract","1 pastry shell (9 inches), baked",\
								"2 large firm bananas","1 cup heavy whipping cream, whipped"]

		banana_cream_pie.instructions = ["1. In a large saucepan, combine sugar, cornstarch, salt and milk",\
								 "until smooth. Cook and stir over medium-high heat until thickened and",\
								 "bubbly. Reduce heat; cook and stir 2 minutes longer. Remove from heat.",\
								 "Stir a small amount of hot filling into eggs; return all to pan.",\
								 "Bring to a gentle boil; cook and stir 2 minutes longer.",\
								 " ",\
								 "2. Remove from heat. Gently stir in butter and vanilla. Press plastic",\
								 "wrap onto surface of custard; refrigerate, covered, 30 minutes.",\
								 " ",\
								 "3. Spread half of the custard into pastry shell. Slice bananas; arrange",\
								 "over filling. Pour remaining custard over bananas. Spread with",\
								 "whipped cream. Refrigerate 6 hours or overnight. Yield: 8 servings"]

		baked_potatoes = Recipe.Recipe(name = "Baked Potatoes", type = "Sides")
		baked_potatoes.ingredients = ["4 russet potatoes (about 1/2 lb), scrubbed", \
									 "olive oil", "sea salt", "freshly ground pepper", "unsalted butter"]

		baked_potatoes.instructions = ["1. Preheat oven to 350°. Prick potatoes all over with a fork and rub with oil; \
										season generously with salt and pepper.", " ", "2. Place potatoes directly on an \
										oven rack and roast until very soft when squeezed and skin is crisp, 60–75 minutes.",\
									   " ", "3. Cut open each potato; season with salt and pepper and top with butter, Parmesan, \
									    and/or chives."]

		fried_chicken = Recipe.Recipe(name = "Fried Chicken", type = "Entree")
		fried_chicken.ingredients = ["4 cups all-Purpose flour, divided", "2 tablespoons garlic salt",\
									 "1 tablespoon paprika", "3 teaspoons pepper, divided", "2-1/2 teaspoons poultry seasoning",\
									 "2 large Eggs", "1-1/2 cups water", "1 teaspoon salt", "2 broiler/fryer chickens (3-1/2 to 4 \
									 pounds each), cut up", "Oil for deep-fat frying"]
		fried_chicken.instructions = ["1. In a large resealable plastic bag, combine 2-2/3 cups flour, garlic salt, paprika, 2-1/2 \
									  teaspoons pepper and poultry seasoning. In a shallow bowl, beat eggs and water; add salt and \
									  the remaining flour and pepper. Dip chicken in egg mixture, then place in the bag, a few pieces \
									  at a time. Seal bag and shake to coat.", " ", "2. In a deep-fat fryer, heat oil to 375°. Fry chic\
									  ken, several pieces at a time, for 5-6 minutes on each side or until golden brown and juices run \
									  clear. Drain on paper towels."]



		return None


	def check_file_sys(self):

		#check if main directory exists, otherwise make it
		if not os.path.isdir(OSX_PATH):
			self.make_file_sys()

		#TODO - finish writing method...


	def load_recipes(self):
		'''
		(None) -> Dictionary

		loads recipes from the main directory (sorted by type) into a dictionary which is
		returned
		'''

		# initialize
		recipes = {}
