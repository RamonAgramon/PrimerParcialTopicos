#!/usr/bin/env/python

import requests

import lxml.html

class Game:
  
    def __init__ (self,titles,prices,totalTags,totalPlatforms):
        self.titles = titles
        self.price = prices
        self.totalTags = totalTags
        self.totalPlatforms = totalPlatforms


html = requests.get ('https://store.steampowered.com/explore/new/')

doc = lxml.html.fromstring(html.content)

newReleases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

#print(newReleases)

titles = newReleases.xpath('.//div[@class="tab_item_name"]/text()')

#print(titles)

prices = newReleases.xpath('.//div[@class="discount_final_price"]/text()')

#print(prices)

tags = newReleases.xpath('.//div[@class="tab_item_top_tags"]')

totalTags = []

for tag in tags:
    totalTags.append(tag.text_content())

#print(totalTags)

totalTags = [tag.split(', ') for tag in totalTags]

#print(totalTags)

platformsDiv = newReleases.xpath('.//div[@class="tab_item_details"]')

totalPlatforms = []

for game in platformsDiv:
    namePlatform = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in namePlatform]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    totalPlatforms.append(platforms)

#print(totalPlatforms)

output = []

for info in zip(titles,prices,totalTags,totalPlatforms):
    response = {}
    response['title']= info[0]
    response['price']= info[1]
    response['tags']= info[2]
    response['platforms']= info[3]
    output.append(response)

print(output)
X = 1
for game in zip(titles,prices,totalTags,totalPlatforms):
    game1=Game(info[0],info[1],info[2],info[3])
    print("*********")
    print("Game "+str(X))
    X=X+1
    print("Titulo: "+ game1.titles)
    print("Precio: "+ game1.price)
    print("Etiquetas: "+ str(game1.totalTags))
    print("Plataformas: "+ str(game1.totalPlatforms))
    print("**********")









