import kivy

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.properties import ObjectProperty
from urllib2 import urlopen
import json



class ButtonSearch(AnchorLayout):
	servicetag_box = ObjectProperty()
	systeminfo_box = ObjectProperty()



	def search(self):

		urlfull = 'https://api.dell.com/support/v2/assetinfo/detail/tags.json?svctags=3T11NM1&apikey=849e027f476027a394edd656eaef4842'

		response = urlopen(urlfull)
		json_obj = json.load(response)

		systemtype = json_obj['GetAssetDetailResponse']['GetAssetDetailResult']['Response']['DellAsset']['MachineDescription']

		return

		self.systeminfo_box.text = systemtype
		print "searched"

	def clear(self):
		self.servicetag_box.text = "cleared"
		self.systeminfo_box.text = "cleared"



class urlrequest(App):
	pass


if __name__ == "__main__":
	urlrequest().run()