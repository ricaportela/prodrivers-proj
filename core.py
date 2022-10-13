import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_listas_ul(city='',state='Florida'):
    lista_ul = []    
    resp = requests.get("https://www.prodrivers.com/jobs/?City=&State=Georgia")

    soup = BeautifulSoup(resp.content, "html.parser")
    mydivs = soup.find_all("div", class_="accordionContentInner")
    for todos_uls in mydivs:
        todos_uls = todos_uls.find_all("ul")[:]
        for linha in todos_uls:
            pprint(linha)
            row = linha.find_all("li")
            lista_ul.append(row)

    return lista_ul

if "__main__" == __name__:
    listas=get_listas_ul()
    pprint(listas)

