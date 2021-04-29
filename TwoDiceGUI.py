"""
Program: TwoDiceGUI.py
Author:Joseph 4/28/2021

***Note: The file breezypythongui.py MUST be in the same directory as this file for the application to work.***
"""

from breezypythongui import EasyFrame
import random

class TwoDice(EasyFrame):
	"""Display a greeting in a window"""

	def __init__(self):
	   """Sets up the window and the label."""
	   EasyFrame.__init__(self, title = "Two Dice Game", resizable = False, background = "Red")

	   self.addLabel(text = "Two Dice Game", row = 0, column = 0, columnspan = 3, sticky = "NSEW", background = "Red").config(font = ("Courier", 24))
	   self.addLabel(text = "Player roll is", row = 1, column = 0, background = "yellow").config(font =("Verdana", 10))
	   self.addLabel(text = "Computer roll is", row = 2, column = 0, background = "yellow").config(font = ("Verdana", 10))

	   self.field1 = self.addIntegerField(value = 0, row = 1, column = 1)
	   self.field2 = self.addIntegerField(value = 0, row = 2, column = 1)
	   self.button = self.addButton(text = "Roll", row = 3, column = 0, columnspan = 3, command = self.spin).config(font = ("Georgia", 8))
	   self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 3, sticky = "NSEW", background = "Cyan")

	  
	   

	def spin(self):
		# variables and constants
		num1 = random.randint(1, 6)
		num2 = random.randint(1, 6)
		result = ""
		if num1 == num2:
			result = "You Tied!"
		elif num1 > num2:
			result = "You win!"	
		else:
			result = "The Computer wins!"			
					
		

		# output phase
		self.field1.setNumber(num1)
		self.field2.setNumber(num2)
		self.resultArea["text"] = result

			
		

#definition of the main() function for program entry
def main():
	"""Instantiates and pops up the window."""
	TwoDice().mainloop()

# global call to the main() function
main()
