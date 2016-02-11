'''
Recipe_Frame.py

Author: Conor Tracey

Created: 		2/10/2016
Latest Update: 	2/10/2016

A module defining the Recipe_Frame object. Recipe_Frames are a child class of the tkinter
Frame class. It is merely a graphical representation of a Recipe object for use in
a tkinter GUI
'''

#built-in library imports
import tkinter as tk

#local imports
import Recipe, Recipe_Writer, Recipe_Reader

class Recipe_Frame(tk.Frame):

	def __init__(self, master, recipe):

		#set parent frame
		tk.Frame.__init__(self, master)

		self.recipe = recipe

		self.name_label = tk.Label(self, text = ("NAME: " + recipe.name))
		self.type_label = tk.Label(self, text = ("TYPE: " + recipe.type))

		ingr_text = 'INGREDIENTS:\n'
		for ingr in recipe.ingredients:
			ingr_text += ("- " + ingr)

		self.ingredients_label = tk.Label(self, text = ingr_text)

		instr_text = 'INSTRUCTIONS:\n'
		for instr in recipe.instructions:
			instr_text += instr

		self.instruction_label = tk.Label(self, text = instr_text)

		self.name_label.grid_configure(row=0, column=0)
		self.type_label.grid_configure(row=1, column=0)
		self.ingredients_label.grid_configure(row=2, column=0)
		self.instruction_label.grid_configure(row=3, column=0)

		return


