# CEST CETTE PARTIE QUI CREE DES PAGES
from pywikiapi import Site
from bs4 import BeautifulSoup
import requests
from link_research import recup_links


user = "YGrebici@MostWantedBot"
passw = "rebp70qighbgk55lpoi47b8fnesf3au3"
baseurl = 'http://wikipast.epfl.ch/wikipast/'
summary = 'MostWantedBot page creation'
MostWantedTerm = 'Akari Inoue'

baseurl = 'http://wikipast.epfl.ch/wikipast/'
baseurl + 'api.php'

site = Site('http://wikipast.epfl.ch/wikipast/api.php')  # Définition de l'adresse de l'API
site.no_ssl = True  # Désactivation du https, car non activé sur wikipast
site.login(user, passw)  # Login du bot

results = []
# Cherche dans toutes les pages celles commençant par Mahatma
for res in site.query(list='allpages', apprefix=MostWantedTerm):
    results.append(res)

# check if page already exists
if len(results[0]['allpages']) == 1:
    print('Page déjà existante')

else:
    # Login request
    payload = {'action': 'query', 'format': 'json', 'utf8': '', 'meta': 'tokens', 'type': 'login'}
    r1 = requests.post(baseurl + 'api.php', data=payload)

    # login confirm
    login_token = r1.json()['query']['tokens']['logintoken']
    payload = {'action': 'login', 'format': 'json', 'utf8': '', 'lgname': user, 'lgpassword': passw,
               'lgtoken': login_token}
    r2 = requests.post(baseurl + 'api.php', data=payload, cookies=r1.cookies)

    # get edit token2  comme si on appuyait sur le bouton modifier?
    # le csrf token est un jeton de confirmation de sécurité
    params3 = '?format=json&action=query&meta=tokens&continue='
    r3 = requests.get(baseurl + 'api.php' + params3, cookies=r2.cookies)
    edit_token = r3.json()['query']['tokens']['csrftoken']

    edit_cookie = r2.cookies.copy()
    edit_cookie.update(r3.cookies)

    content_tab = recup_links(MostWantedTerm)

    content = ''

    # contenu de la page (vide)
    for element in content_tab:
        content += element

    # save action (modif de la page avec l'action edit)
    payload = {'action': 'edit', 'assert': 'user', 'format': 'json', 'utf8': '', 'text': content, 'summary': summary,
               'title': MostWantedTerm, 'token': edit_token}
    r4 = requests.post(baseurl + 'api.php', data=payload, cookies=edit_cookie)

    # payload semble etre une fonction qui va créer un url avec des commandes: ici fonction principale est edit, puis on y ajoute les arguments

    r4.json()

    # dans le r4 (requete 4 je pense), mis sous format json, on a le result:succes donc page MostWantedTerm bien créée