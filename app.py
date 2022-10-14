import pandas as pd
import csv
from pprint import pprint

from bs4 import BeautifulSoup
from requests_html import HTMLSession


def extract(city='',state='Georgia'):

    session = HTMLSession()    
    resp = session.get(f"https://www.prodrivers.com/jobs/?City={city}&State={state}")
    soup = BeautifulSoup(resp.content, "html.parser")
    return soup

def transform(soup):

    jobs = []  
    accordionItems = soup.find_all(class_ ="accordionItem")
    #print(len(accordionItems))
    title = soup.find('input', {'id': 'title'}).get('value')
    location = soup.find('input', {'id': 'location'}).get('value')

    for div in accordionItems:
        #ultag_com_lis = div.find_next('ul').find_all('li')  #traz somente a description
        #ultag_com_lis = div.find('ul').find_all('li')  
        ultag = div.find_all('ul')
       # print(f'Quantas ULS eu achei? {len(ultag)}')      
        for i,ul in enumerate(ultag):
            job = [] 
            description = [] #0 -> Descrição
            requirements = [] #1 -> Requirements
            benefits = [] #2: -> Beneficios
            print(i)
            if i == 0:
                description.append(ul.text)
            if i == 1:
                requirements.append(ul.text)  
            else:
                if i == 2:
                    print(f"passou >>> {i}")
                    benefits.append(ul.text)
            #job = [description, requirements,benefits]
            job = [i, title, location, description, requirements, benefits]
            jobs.append(job)
            #print(i, ul.text)
        #pprint(ultag)
        ultag_com_lis = div.find_all('li')  
        #pprint(ultag_com_lis)       
        
     
    return jobs


if "__main__" == __name__:
    soup = extract('', 'Georgia')
    jobs = transform(soup)

    with open('jobs.csv', 'w') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(jobs)

    # pprint(listas)


