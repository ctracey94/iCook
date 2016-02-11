'''
Recipe.py

Author: Conor Tracey

Created:        1/20/2016
Latest Update:  2/10/2016

A module defining Recipe objects for use in the iCook application.
'''
__author__ = 'tracey'


class Recipe:

    def __init__(self, name='', type='', ingredients=[], instructions=[]):
        self.name = name
        self.type = type
        self.ingredients = ingredients
        self.instructions = instructions

        return
