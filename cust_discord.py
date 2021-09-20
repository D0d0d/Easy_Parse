from dhooks import Webhook, Embed, File


class Discord:
    mHook = type('Webhook', (object,), {})()
    icon = ''
    links =''
    name=''
    cookName =''
    def __init__(self, url):
        self.mHook = Webhook(url)

    def send_embed(self, prod):
        embed = Embed(color=0xFFFFFF)
        if self.name:
            if self.icon:
                embed.set_author(name=self.name,icon_url=self.icon)
            else:
                embed.set_author(name=self.name)

        embed.set_title(prod['name'])
        print(prod['name'])
        if prod['link'] != 'javascript:void(0);':
            embed.url = prod['link']

            print(prod['link'])
        embed.set_thumbnail(prod['image'])
        print(prod['image'])
        if prod['price']:
            embed.add_field(name='Price:', value=prod['price'])
            print(prod['price'])
        if prod['status']:
            embed.add_field(name='Status:', value=prod['status'])
            print(prod['status'])

        szs = prod['sizes']
        if szs:
            if (szs[0]!='-'):
                le = len(szs) // 5
                sizes = ''
                for c_s in range(-1, le): #c_s - current size
                    sizes = '\n'.join(szs[((c_s + 1) * 5):((c_s + 2) * 5)])
                    if sizes:
                        embed.add_field(name='Sizes',value=sizes)
                        print(sizes)

        embed.set_footer(text=self.cookName,
                         icon_url=self.icon)
        print(self.cookName)
        print(self.icon)
        embed.add_field(name=' Links ',
                        value=self.links,
                        inline=False)
        print(self.links)
        print(embed.fields)
        self.mHook.send(embed=embed)



    def send_file(self, name_f, format_f='None'):
        if format_f=='html':
            file = File(name_f, name='page.html')
            self.mHook.send('Your page:', file=file)
        else:
            file = File(name_f, name='file.pkl')
            self.mHook.send('Your Data:', file=file)


    def send_error(self, e):
            self.mHook.send("An error occured! :open_mouth: "+str(e))

    def send_msg(self, msg):
        self.mHook.send(msg)