import json

# libs 3th part
import pandas as pd
import requests
from w3lib.html import remove_tags


cidade = 'Kansas'
pagina = 1

# data precisa ser atualizada antes de cada request com a cidade e a pagina
form_data = {
    'group_id': '1545',
    'location': f'{cidade}',
    'user_location[lat]': '-23.5941024',
    'user_location[lng]': '-46.4104869',
    'filters[0][centerline]': '1',
    'query': '',
    'page': f'{pagina}', # trocar o numero da pagina
    'user_id': '68375abc-1c36-4ca7-a84f-f0407e262b97',
    'session_id': '9543c6a0-4e5f-11ed-b19a-a30c3a083de9',
    'parent_id': 'a1b29a42-8b8a-4e68-9b8b-1191ca659f45:APAb7ITG7bcoOa5A/yZ9u9bNbfe5fBTBjg==',
    'token': 'Q2lBQVA3LzRSZkY4M3NLTGFFQlFQbWtoei95c21uNnJBUDhBL3dEL0FQOEFBUklRYUVCUVBta2h6L3lzbW42ckFBQUFBQm9KL0dkcGYvaXFxN1YwIzEw',
}

headers = {
    'authority': 'talent.ongig.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
    'dnt': '1',
    'origin': 'https://www.centerlinedrivers.com',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

# 1 requests para pegar totais de registros
response = requests.post('https://talent.ongig.com/api/external/v1/new/centerline/search', headers=headers, data=form_data)

totalSize = response.json()['response']['totalSize']
resultsjobs = []
nextPage = 1
row = 1
lidos = 1

while lidos < totalSize:
    dados = json.loads(response.text)
    jobs = dados['response']['matchingJobs']

    for job in jobs:
        title = remove_tags(str("".join(job['job']['title'])))
        city = remove_tags(str("".join(job['job']['addresses'])))
        currency = job['job']['compensationInfo']['entries'][0]['range']['minCompensation']['currencyCode']
        units = job['job']['compensationInfo']['entries'][0]['range']['minCompensation']['units']
        qualifications = remove_tags(str("".join(job['job']['qualifications'])))
        description = remove_tags(str("".join(job['job']['description'])))
        if job['job']['jobBenefits'] != None:
            benefits =  remove_tags(str("".join(job['job']['jobBenefits'])))
        else:
            benefits = "N/A"

        itemjobs = {
            'title': title.replace("\n"," "),
            'city': city.replace("\n"," "),
            'salary': units + " " + currency,
            'qualifications': qualifications.replace("\n"," "),
            'description': description.replace("\n"," "),
            'benefits': benefits.replace("\n"," ")
        }
        resultsjobs.append(itemjobs)   
        row += 1
        lidos += 1
        if row > 10:
            nextPage += 1
            form_data.update(page=nextPage)
            row = 1
    
    response = requests.post('https://talent.ongig.com/api/external/v1/new/centerline/search', headers=headers, data=form_data)  

df = pd.DataFrame(resultsjobs)
df.columns = ["TITLE","CITY", "SALARY","QUALIFICATIONS","DESCRIPTION","BENEFITS"]
df.to_csv(f"jobs_center_{cidade}.csv", index=False)
print('# fim #')
