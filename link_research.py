from bs4 import BeautifulSoup
import  requests

#   Fonction qui prend en entrée un nom d'article sous forme d'un string
#   en sortie va créer un texte, inséré dans content lors de la création de la page
#


entree = "O'Reilly Auto Parts 200 (I-70)"

r = requests.get("https://en.wikipedia.org/wiki/Wikipedia:Most-wanted_articles")
soup = BeautifulSoup(r.content, "html5lib")

terme = soup.find('a', text=entree)

print(terme['href'])

#transforme le nom en string mettable dans une URL - tests


terme_URL = entree.replace(" ",'_')
terme_URL = terme_URL.replace("'",'%27')

print(terme_URL)

#on s'aide du début d'URL pour accéder aux links
Pre_URL = 'https://en.wikipedia.org/wiki/Special:WhatLinksHere/'

r2 = requests.get(Pre_URL+terme_URL)
print(r2.url)

print()

#on récup les flags 'a'

soup2 = BeautifulSoup(r2.content, "html5lib")

partie_links = soup2.find('ul', id="mw-whatlinkshere-list")
partie_links_list = partie_links.find_all('a')

for element in partie_links_list:
    print(element['title'])

#crea source:
wiki_URL = 'https://en.wikipedia.org/wiki/'
#sous un tableau de "external sources" on aura :
# nom [URL]

#enlever duplicatas, enlever Special:WhatLinksHere
#chercher peut etre plus précis.. dans le code wiki

content = []

for i in range(len(partie_links_list)):
    terme_link_URL = partie_links_list[i]['title'].replace(" ",'_').replace("'",'%27')
    print(partie_links_list[i]['title'], "[", wiki_URL+terme_link_URL, "]")
