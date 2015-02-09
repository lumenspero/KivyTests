from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.network.urlrequest import UrlRequest
import json

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '400')

urldetail = "https://api.dell.com/support/v2/assetinfo/detail/tags.json?svctags="

key = "849e027f476027a394edd656eaef4842"
key2 = "d676cf6e1e0ceb8fd14e8cb69acd812d"
key3 = "1adecee8a60444738f280aad1cd87d0e"

keylist = [key, key2, key3]

n = 0

class AccountDetailsForm(AnchorLayout):
	servicetag_box = ObjectProperty()
	systemtype_box = ObjectProperty()
	raidcontroller_box = ObjectProperty()
	idrac_box = ObjectProperty()
	hardrive_box = ObjectProperty()
	memory_box = ObjectProperty()
	systemtype = ObjectProperty()
	idrac = ObjectProperty()
	HDPD = ObjectProperty()
	MEMPD = ObjectProperty()
	hdquantity_box = ObjectProperty()
	memquantity_box = ObjectProperty()
		
	def search(self):

		servicetag = (self.servicetag_box.text)
		global urldetail
		global key
		global response
		global json_obj
		global n

		while True:
			if n%2 == 0:
				apikey = keylist[0]
				n = n + 1
			elif n%2 == 1:
				apikey = keylist[1]
				n = n+1
			break



		urldetail += servicetag
		urldetail += "&apikey="
		urldetail += apikey

		print urldetail

		response = UrlRequest(urldetail)
		json_obj = json.load(response)

		#System Type
		systemtype = json_obj['GetAssetDetailResponse']['GetAssetDetailResult']['Response']['DellAsset']['MachineDescription']

		print systemtype
		self.systemtype_box.text = systemtype

		#Full Asset Part
		AssetPart = json_obj['GetAssetDetailResponse']['GetAssetDetailResult']['Response']['DellAsset']['AssetParts']['AssetPart']

		#RAID controller

		for PartDescription in AssetPart:
			if 'H830' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H730P' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H730' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H810' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H710P' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H710' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H310' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'S110' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H800' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H700' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'H200' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'S300' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'S100' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'PERC6' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'SAS6IR' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'PERC5' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'SAS5IR' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'PERC4' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'PERC3' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'PERC2' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif '320DC' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif '39160' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif '39320' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'A-U320' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'LSI320' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'PCIU320' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'CERC6I' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'CERC SATA 6' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']
			elif 'CERC SATA 2' in PartDescription['PartDescription'] and \
				not 'CBL' in PartDescription['PartDescription']:
				RC = PartDescription['PartDescription']

		print RC
		self.raidcontroller_box.text = RC

		#iDRAC version
		for PartDescription in AssetPart:
			if 'DRAC' in PartDescription['PartDescription'] and \
		    	not 'INFO' in PartDescription['PartDescription']:
				idrac = PartDescription['PartDescription']
			elif 'DRAC' in PartDescription['PartDescription']:
				idrac = PartDescription['PartDescription']
			elif 'BMC' in PartDescription['PartDescription'] and \
			not 'INFO' in PartDescription['PartDescription']:
				idrac = PartDescription['PartDescription']
			elif 'BMC' in PartDescription['PartDescription']:
				idrac = PartDescription['PartDescription']

		print idrac
		self.idrac_box.text = idrac

		#Hard Drive
		for PartDescription in AssetPart:
			if 'HD' in PartDescription['PartDescription'] and \
        		not 'ASSY'in PartDescription['PartDescription'] and \
        		not 'BACKPLANE'in PartDescription['PartDescription'] and \
        		not 'INFO'in PartDescription['PartDescription'] and \
        		not 'SRV' in PartDescription['PartDescription'] and \
        		not 'MOD' in PartDescription['PartDescription'] and \
        		not 'STRG' in PartDescription['PartDescription'] and \
        		not 'Label' in PartDescription['PartDescription'] or \
        		'Hard Drive' in PartDescription['PartDescription'] and \
        		not 'ASSY' in PartDescription['PartDescription'] and \
        		not 'BACKPLANE' in PartDescription['PartDescription'] and \
        		not 'Label' in PartDescription['PartDescription'] and \
        		not 'SRV' in PartDescription['PartDescription'] and \
        		not 'MOD' in PartDescription['PartDescription'] and \
        		not 'STRG' in PartDescription['PartDescription'] and \
        		not 'INFO' in PartDescription['PartDescription'] or \
        		'HD' in PartDescription['PartDescription'] and \
        		'SAS' in PartDescription['PartDescription'] and \
        		not 'ASSY'in PartDescription['PartDescription'] and \
        		not 'BACKPLANE'in PartDescription['PartDescription'] and \
        		not 'SRV' in PartDescription['PartDescription'] and \
        		not 'MOD' in PartDescription['PartDescription'] and \
        		not 'STRG' in PartDescription['PartDescription'] and \
        		not 'Label' in PartDescription['PartDescription'] and \
        		not 'INFO'in PartDescription['PartDescription']:
				HDPD = PartDescription['PartDescription']

				x = filter(lambda person: person['PartDescription'] == HDPD, AssetPart)
				for Quantity in x:
					HDQ = str(Quantity['Quantity'])

		print HDPD
		self.harddrive_box.text = HDPD
		print HDQ
		self.hdquantity_box.text = HDQ

		#Memory
		for PartDescription in AssetPart:
			if 'DIMM' in PartDescription['PartDescription'] and \
				not 'BLNK'in PartDescription['PartDescription'] and \
				not 'INFO'in PartDescription['PartDescription']:
				MEMPD = PartDescription['PartDescription']
            	y = filter(lambda mem: mem['PartDescription'] == MEMPD, AssetPart)
            	for Quantity in y:
                	MEMQ = str(Quantity['Quantity'])

		print MEMPD
		self.memory_box.text = MEMPD
		print MEMQ
		self.memquantity_box.text = MEMQ

			

###This class lets you tab between fields!!! So useful!!!		
class AccountDetailsTextInput(TextInput):
	next = ObjectProperty()
	
	def _keyboard_on_key_down(self, window, keycode, text, modifiers):
		if keycode[0] == 9: 
			self.next.focus = True
		elif keycode[0] == 13:
			self.parent.parent.parent.search()
		else:
			super(AccountDetailsTextInput, self)._keyboard_on_key_down(
				window, keycode, text, modifiers)
				
class Orkiv_snapshot(App):
    pass
 
Orkiv_snapshot().run()