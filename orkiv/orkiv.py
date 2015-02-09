from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput

class AccountDetailsForm(AnchorLayout):
	server_box = ObjectProperty()
	username_box = ObjectProperty()
	password_box = ObjectProperty()
	
	def login(self):
		print(self.server_box.text)
		print(self.username_box.text)
		print(self.password_box.text)
		print("click the goddamn button")
		test_id = self.username_box.text + self.server_box.text
		print test_id

###This class lets you tab between fields!!! So useful!!!		
class AccountDetailsTextInput(TextInput):
	next = ObjectProperty()
	
	def _keyboard_on_key_down(self, window, keycode, text, modifiers):
		if keycode[0] == 9: 
			self.next.focus = True
		elif keycode[0] == 13:
			self.parent.parent.parent.login()
		else:
			super(AccountDetailsTextInput, self)._keyboard_on_key_down(
				window, keycode, text, modifiers)
				
class Orkiv(App):
    pass
 
Orkiv().run()