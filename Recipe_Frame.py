'''
Recipe_Frame.py

Author: Conor Tracey

Created: 		2/10/2016
Latest Update: 	3/11/2016

A module defining the Recipe_Frame object. Recipe_Frames are a child class of the tkinter
Frame class. It is merely a graphical representation of a Recipe object for use in
a tkinter GUI
'''

#Standard library imports
import tkinter as tk
import Scroll_Frame

#local imports
import Recipe, Recipe_Writer, Recipe_Reader


def load_recipe_data(frame):
	for i in range(50):
		tk.Label(frame,text=i).grid(row=i,column=0)
		tk.Label(frame,text="my text"+str(i)).grid(row=i,column=1)
		tk.Label(frame,text="..........").grid(row=i,column=2)

class Recipe_Frame(tk.Frame):

	#width and height of frame
	f_width = 250
	f_height = 200

	#width and height of scroll region
	s_width = 200
	s_height = 200

	def __init__(self, parent, recipe):

		#set parent frame
		tk.Frame.__init__(self, parent, relief=tk.GROOVE, width=self.f_width,\
						  height = self.f_height, bd=1)


		#set the recipe to be shown in the Recipe_Frame
		self.recipe = recipe

		#to make a frame with a scrollbar in tkinter, you have to jump through some
		#hoops. It involves making a canvas with an additional frame inside it. That's
		#what we're doing here. The next [] lines are all to make a scrollbar
		self.canvas = tk.Canvas(self)
		self.inner_frame = tk.Frame(self.canvas)
		self.scrollbar = tk.Scrollbar(self,orient="vertical",command=self.canvas.yview)

		self.canvas.configure(yscrollcommand=self.scrollbar.set)

		self.scrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")

		self.canvas.create_window((0,0),window=self.inner_frame,anchor='nw')


		#funtion for configuring the scrollbar canvas
		def scrollbar_frame_configuration(event):
			self.canvas.configure(scrollregion=self.canvas.bbox("all"),width = self.s_width,\
									height=self.s_height)
			return None


		def load_frame(self):
			self.inner_frame.bind("<Configure>", scrollbar_frame_configuration)
			load_recipe_data(self.inner_frame)



		'''
		self.name_label = tk.Label(self, text = (recipe.name))
		self.type_label = tk.Label(self, text = (recipe.type))

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
		'''



