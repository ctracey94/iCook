'''
Recipe_Reader.py

Author: Conor Tracey

Created: 		1/22/2016
Latest Update: 	2/10/2016

A module defining the Recipe_Reader object for use in the iCook application.
Recipe_Readers read .rec filetypes and translate them into Recipe objects
(defined in Recipe.py)
'''

#local imports
import Recipe


#MAC OSX path to iCook file library
OSX_PATH = "~/Library/Application\ Support/iCook"


class Recipe_Reader:

	def __init__(self):
		return

	def read_one(self, file):
		'''
		(file) -> (recipe)

		reads a single recipe from file with name filename, returns a Recipe object
		'''

		#make an empty recipe object
		recipe = Recipe.Recipe('', '', [], [])

		#read the name and type of the recipe from the top two lines of the file
		recipe.name = file.readline()
		recipe.type = file.readline()

		#get the number of ingredients
		num_ingr = file.readline()

		#check for eof in case something went wrong with the file
		if num_ingr == '':
			print("\nERROR: Recipe_Reader reached end of file prematurely, possible file corruption")
			return recipe

		num_ingr = int(num_ingr)

		#get ingredients
		for i in range(num_ingr):

			#read an ingredient
			ingr = file.readline()

			#put the ingredient we just read in the ingredients set
			recipe.ingredients.append(ingr)

		#get the number of instructions
		num_instr = file.readline()

		#check for eof in case something went wrong with the file
		if num_instr == '':
			print("\nERROR: Recipe_Reader reached end of file prematurely, possible file corruption")
			return recipe

		num_instr = int(num_instr)

		#get instructions
		for i in range(num_instr):

			#read an instruction
			instruction = file.readline()

			#put the instruction we just read in the instructions list
			recipe.instructions.append(instruction)

		return recipe


