from bs4 import BeautifulSoup
import  requests

#   entrée: nom d'article dans la liste des MostWanted
#   sortie: Tableau de phrases (string) à directement implémenter dans content
def recup_links(MostWantedTerm):
    # 1)Transforme le nom en string mettable dans une URL

    terme_URL = MostWantedTerm.replace(" ", '_')
    terme_URL = terme_URL.replace("'", '%27')

    # 2) On s'aide du début d'URL pour accéder aux links
    Pre_URL = 'https://en.wikipedia.org/wiki/Special:WhatLinksHere/'
    r2 = requests.get(Pre_URL + terme_URL)

    # 3) On récupère tous les flags <a> des links du MostWantedTerm
    soup2 = BeautifulSoup(r2.content, "html5lib")
    partie_links = soup2.find('ul', id="mw-whatlinkshere-list")
    partie_links_list = partie_links.find_all('a')

    # 4) On crée le tableau content, avec comme sources le besoin du pré-URL de wiki
    wiki_URL = 'https://en.wikipedia.org/wiki/'

    # on remparque que pour un title, on a 3 elements dont 2 indésirables du type:
    #       Brennan Newberry
    #       Special:WhatLinksHere
    #       Brennan Newberry
    # on garde donc le premier, on vire les deux autres dans les ifs prochains:
    # methode choisie ici: on fait des sauts des sauts de 3 indices par title
    # et on commence a la 3e indice car le premier lien linked est toujours un most:wanted truc

    # Ne peut pas compiler si on envoie un tableau vide

    content_tab = [''] * (int)((len(partie_links_list) / 3))

    for i in range(len(partie_links_list)):
        if ((partie_links_list[i]['title'].find(':')) == (-1)):
            if (i % 3 == 0):  # on prend un indice sur 3
                terme_link_URL = partie_links_list[i]['title'].replace(" ", '_').replace("'", '%27')
                content_tab[((int)(i / 3))] = '*Mention de [[' + MostWantedTerm + ']] dans [[' + partie_links_list[i][
                    'title'] + ']].[' + wiki_URL + terme_link_URL + ']\n'
         #       print(content_tab[((int)(i / 3))])             #fonction à

        # TAILLE DU TABLEAU
    len(content_tab)
    return content_tab

