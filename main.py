import kivy
import random
import string
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class password:
	def random_generator(self,cantidad_caracteres=16,minus=True,mayus=True,digit=True,carac=True):
		contrasena = ''
		todos_caracteres = []
		if minus == True:
			todos_caracteres += list(string.ascii_lowercase)
		if mayus == True:
			todos_caracteres += list(string.ascii_uppercase)
		if digit == True:
			todos_caracteres += list(string.digits)
		if carac == True:
			todos_caracteres += list(string.punctuation)
		for caracter in range(cantidad_caracteres):
			contrasena += random.choice(todos_caracteres)
		return contrasena



class MyGrid(Widget):
	cantidad = ObjectProperty(None)
	etiqueta = ObjectProperty(None)

	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.mayus = True
		self.minus = True
		self.digit = True
		self.carac = True


	def signal(self):
		cant = self.cantidad.text
		try:
			cant = int(cant)
		except:
			self.etiqueta.text = password.random_generator(self,16,self.minus,self.mayus,self.digit,self.carac)
			self.cantidad.text = ""
			return None
		contrasena = password.random_generator(self,int(cant),self.minus,self.mayus,self.digit,self.carac)
		self.etiqueta.text = contrasena
		self.cantidad.text = ""



class MyApp(App):
	def build(self):
		self.title = "Strong_Random_Password_Generator By MATI"
		return MyGrid()


if __name__=="__main__":
    MyApp().run()