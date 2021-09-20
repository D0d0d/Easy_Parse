import requests
import time
import pickle
from time import sleep
import lxml.html as html
import cloudscraper
import random
import re
from lxml import etree
from dhooks import Webhook, File

class Data:
    scraper = cloudscraper.create_scraper()
    newsData = []
    delay = {'bot': 3,
             'top': 6, }
    newsOldData = []
    data = []
    oldData = [{'name': '', 'sizes': ''}]
    headers = {
        'authority': 'brandshop.ru',
        'sec-ch-ua': '^\\^Google',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://brandshop.ru/new/',
        'accept-language': 'ru,de-DE;q=0.9,de;q=0.8,en-US;q=0.7,en;q=0.6', }

    def save(self):
        self.oldData = self.data
        with open("OldData.pkl", "wb") as a_file:
            pickle.dump(self.data, a_file)

    #        a_file = open("newsOldData.pkl", "wb")
    #        pickle.dump(self.newsData, a_file)

    def load(self):
        with open("OldData.pkl", "rb") as a_file:
            self.oldData = pickle.load(a_file)

    #        a_file = open("newsOldData.pkl", "rb")
    #        self.newsOldData = pickle.load(a_file)

    def refresh(self, keys, proxies, save_page=False):
        self.randDelay()
        resp = self.scraper.get(
            'https://brandshop.ru/new/?limit=240&mfp=31-kategoriya%5BКроссовки%5D,manufacturers%5B11,308,47,811%5D',
            proxies=proxies)
        page_n = html.fromstring(resp.text)

        for product in page_n.xpath('//div[contains(@class,"product-container")]'):
            item = {}
            print(etree.tostring(product))
            item['name'] = product.xpath('./div/a/img/attribute::alt')[0]
            if any(key.lower() in item['name'].lower() for key in keys) and (
                    item['name'] not in [d['name'] for d in self.data]):
                #    print('\n'.join(product.xpath('./descendant::text()')).replace('\n                    ','').replace('  ',''))
                if product.xpath('./div/div[@class="salestart"]'):
                    item['status'] = ' '.join(
                        product.xpath('./div/div[@class="salestart"]/descendant::text()')).replace(
                        '\n                    ', '').replace('  ', '')
                elif product.xpath('./div/div[@class="special"]'):
                    item['status'] = ' '.join(product.xpath('./div/div[@class="special"]/descendant::text()')).replace(
                        '\n                    ', '').replace('  ', '')
                else:
                    item['status'] = 'В наличии'
                item['image'] = product.xpath('./div/a/img/attribute::src')[0]
                item['link'] = product.xpath('./div/a/attribute::href')[0]
                item['price'] = ''.join(product.xpath('./div/div[@class="price"]/text()')).replace(
                    '\n                            ', '')

                if item['link'] != 'javascript:void(0);':
                    self.randDelay(bot=0)
                    item['sizes'] = self.getSizes(item, proxies)
                    print(item['sizes'])
                else:
                    item['sizes'] = ['-']
                self.data.append(item)
            print(item, '\n\n\n')
        if save_page:
            with open("page.html", "w", encoding='utf-8') as html_f:
                html_f.write(resp.text)
                return html_f.name

    def getSizes(self, item, proxies):
        link = 'https://brandshop.ru/getproductsize/' + re.search('/goods/(.+?)/', item['link']).group(1) + '/'
        resp = self.scraper.get(
            link,
            headers=self.headers,
            proxies=proxies)
        lines = resp.json()
        return [line['name'] for line in lines]

    def getDif(self):
        dif = []
        for nD in self.data:
            if (not(any(nD['name'] == o_D['name'] for o_D in self.oldData)))or(not(self.oldData)):
                dif.append(nD)
                print("you've entered 1 state")
            else:
                print("you've entered 2 state")
                gen = [x for x in self.oldData if x['name'] == nD['name']]
                #               print('gen \n',gen,'\n',self.oldData)
                for o_D in gen:
                    if (((nD['sizes']) != (o_D['sizes']))):
                        dif.append(nD)
                        print("you've entered 3 state")
                    print(nD['name'])
                    print(nD['sizes'])
                    print(o_D['sizes'])
                    print('\n\n')

        return dif

    def randDelay(self, bot=delay['bot'], top=delay['top']):
        time.sleep(random.randint(bot, top))
