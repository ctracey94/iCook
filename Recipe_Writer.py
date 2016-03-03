'''
Recipe_Writer.py

Author: Conor Tracey

Created: 		2/3/2016
Latest Update: 	2/10/2016

A module defining the Recipe_Writer object for use in the iCook application.
Recipe_Writers write Recipe (defined in Recipe.py) objects into .rec files
'''

#local imports
import Recipe

#MAC OSX path to iCook file library
OSX_PATH = "~/Library/Application Support/iCook"

class Recipe_Writer:
	def __init__(self):
		return

	def write_one(self, recipe, file):

		#write recipe name and type to file
		file.write(recipe.name + '\n')
		file.write(recipe.type + '\n')

		#get number of ingredients and number of instructions
		num_ingr = len(recipe.ingredients)
		num_instr = len(recipe.instructions)

		#write number of ingredients
		file.write(str(num_ingr) + '\n')

		#write ingredients
		for ingredient in recipe.ingredients:
			file.write(ingredient + '\n')

		#write number of instructions
		file.write(str(num_instr) + '\n')

		#write instructions
		for instruction in recipe.instructions:
			file.write(instruction + '\n')

		return

