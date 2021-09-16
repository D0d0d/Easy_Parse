import random
import dhooks
import requests
import  time
import pickle
from time import sleep
import cloudscraper
import lxml.html as html
from dhooks import Webhook
from lxml import etree
import dictdiffer
from data import Data
from cust_discord import Discord

'''
tData = Data()
keys = ['adidas','nike']
tData.getNewsData()
sleep(3)
for key in keys:
    tData.getKeyData(key)
tData.saveData()'''
proxies = [{'http':"http://175.44.109.216:9999"},{'http':"http://180.250.12.10:80"},{'http':"http://36.248.133.187:9999"},{'http':"188.166.83.17:8080"}]
dif =[]
tData = Data()
mDisc = Discord()
mDisc.mHook='https://discord.com/api/webhooks/866779492856889435/LsxwFU-3elBn6oiNCPIlcZ_e5bTKQly3BNzypZpjZPAo8Y9r1DQ6kVVAXstZJL6W27ue'
mDisc.icon = ''
mDisc.links = "[Login](https://brandshop.ru/login/) \n [Checkout](https://brandshop.ru/checkout/)"
mDisc.cookName = ' Soldout Cook '
keys = [
	'Yeezy',
	'Dunk',
	'Air Jordan 1'
]
dif = []
tData.loadData()
#while True:
for i in range(2):
#	tData.getNewsData()
	try:
		tData.getData(keys,proxies[random.randint(0,len(proxies)-1)], save_page=True, l_hook=mDisc.mHook)
		tData.oldData = tData.data
		dif = tData.getDif()
		print('you are here')
		if dif:
			print('iter')
			for d in dif:
				print('oph \n\n',d)
				mDisc.send_embed(d)
			tData.saveData()
			print(tData.data)
			print('\n\n\n')
			print(tData.oldData)

		tData.data.clear()
	except Exception as e:
		try:
			hook = Webhook(mDisc.mHook)
			hook.send("An error occured! :open_mouth: "+str(e))
			print('shit ',e)
		except:
			hook = Webhook(mDisc.mHook)
			hook.send("Double shit happend")
print(dif)


