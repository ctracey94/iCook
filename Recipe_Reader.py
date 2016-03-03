'''
Recipe_Reader.py

Author: Conor Tracey

Created: 		1/22/2016
Latest Update: 	2/25/2016

A module defining the Recipe_Reader object for use in the iCook application.
Recipe_Readers read .rec filetypes and translate them into Recipe objects
(defined in Recipe.py)
'''

#local imports
import Recipe


#MAC OSX path to iCook file library
OSX_PATH = "~/Library/Application Support/iCook"


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
			#(remove newline '\n' character from input)
		recipe.name = file.readline().replace('\n', '')
		recipe.type = file.readline().replace('\n', '')

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

			#the next 4 lines exists to preserve the newline structure of the input recipe:
				#when Recipe_Writer writes recipes, it puts newlines at the end of each write
				#these need to be removed by the reader, but we still want the user to be
				#able to put newlines where they want. 
			if len(ingr) == 1:
				ingr.replace('\n', ' ')
			else:
				ingr.replace('\n', '')

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


