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
import traceback

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
mDisc = Discord('https://discord.com/api/webhooks/866779492856889435/LsxwFU-3elBn6oiNCPIlcZ_e5bTKQly3BNzypZpjZPAo8Y9r1DQ6kVVAXstZJL6W27ue')
mDisc.name ='The Brandshop Monitor'
mDisc.icon ='https://i.ibb.co/h9tWQWx/ava.png'
mDisc.links = "[Login](https://brandshop.ru/login/) \n [Checkout](https://brandshop.ru/checkout/)"
mDisc.cookName = ' Soldout Cook '
keys = [
	'Yeezy',
	'Dunk',
	'Air Jordan 1'
]
dif = []
tData.load()
while True:
#for i in range(1):
#	tData.getNewsData()
	try:
#		mDisc.send_file(
		tData.refresh(keys,proxies[random.randint(0,len(proxies)-1)]) #save_page=True), #format_f='html')
		print(tData.data)
		print(tData.oldData)
		dif = tData.getDif()
		print('you are here')
		if dif:
			print('iter')
			for d in dif:
				try:
					print('oph \n\n',d)
					mDisc.send_embed(d)
				except Exception as e:
					mDisc.send_error(e)
					mDisc.send_msg(traceback.format_exc())
					mDisc.send_msg(str(d))
			tData.save()
			print(tData.data)
			print('\n\n\n')
			print(tData.oldData)
	except Exception as e:
		mDisc.send_error(e)
		mDisc.send_msg(traceback.format_exc())
print(dif)


