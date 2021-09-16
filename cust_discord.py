from dhooks import Webhook, Embed


class Discord:
    mHook = ''
    icon = ''
    links =''
    cookName =''
    def send_embed(self, prod):
        hook = Webhook(self.mHook)
        embed = Embed(color=0xFFFFFF)
        embed.set_author(name='The Brandshop Monitor')

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
        if szs[0]!='-':
            le = len(szs) // 5
            sizes = ''
            for c_s in range(-1, le): #c_s - current size
                sizes = '\n'.join(szs[((c_s + 1) * 5):((c_s + 2) * 5)])
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
        hook.send(embed=embed)
        embed.set_author(name='The Brandshop Monitor')

