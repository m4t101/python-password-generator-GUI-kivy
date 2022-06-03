import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from random import shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from pyperclip import copy


class Password:
	def random_generator(self, characters=16, lower=True, upper=True, digit=True, carac=True):
		password = ''
		all_characters = []
		if lower == True:
			all_characters += list(ascii_lowercase)
		if upper == True:
			all_characters += list(ascii_uppercase)
		if digit == True:
			all_characters += list(digits)
		if carac == True:
			all_characters += list(punctuation)
		shuffle(all_characters)
		all_characters = all_characters[:characters]
		return "".join(all_characters)


class MyGrid(Widget):
	amount = ObjectProperty(None)
	lbl = ObjectProperty(None)

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.upper = True
		self.lower = True
		self.digit = True
		self.special = True


	def signal(self):
		amount = self.amount.text
		try:
			amount = int(amount)
		except:
			self.lbl.text = Password.random_generator(self, 16, self.lower, self.upper, self.digit, self.special)
			self.amount.text = ""
			return None
		password = Password.random_generator(
			self, int(amount), self.lower, self.upper, self.digit, self.special)
		self.lbl.text = password
		self.amount.text = ""

	
	def copy(self):
		copy(self.lbl.text)
		self.button = Label(text="Password copied with success")
		self.copied.text = "Password Copied with Success"


class MyApp(App):
	def build(self):
		self.title = "Strong_Random_Password_Generator-----By:MATI-----"
		return MyGrid()


if __name__=="__main__":
    MyApp().run()
