import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_listas_ul(city='',state='Georgia'):
    jobs = []  

    
    resp = requests.get(f"https://www.prodrivers.com/jobs/?City={city}&State={state}")
    soup = BeautifulSoup(resp.content, "html.parser")
    accordionItems = soup.find_all(class_ ="accordionItem")
    #print(len(accordionItems))
    for div in accordionItems:
        
        #ultag_com_lis = div.find_next('ul').find_all('li')  #traz somente a description
        #ultag_com_lis = div.find('ul').find_all('li')  
        ultag = div.find_all('ul')
       # print(f'Quantas ULS eu achei? {len(ultag)}')      
        for i,ul in enumerate(ultag):
            job = [] 
            description = [] #0 -> Descrição
            requirements = [] #1 -> Requirements
            benefitis = [] #2: -> Beneficios
            print(i)
            if i == 0:
                description.append(ul.text)
            if i == 1:
                requirements.append(ul.text)  
            else:
                benefitis.append(ul.text)
            job = [description, requirements,benefitis]
            jobs.append(job)
            #print(i, ul.text)
        #pprint(ultag)
        ultag_com_lis = div.find_all('li')  
        pprint(ultag_com_lis)       
        
     
    return jobs


if "__main__" == __name__:
    listas=get_listas_ul()
    pprint(listas)


