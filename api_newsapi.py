import requests
import pprint
def api_category(category,page_size='20',page_number='1',country='ru'):
    url = ('https://newsapi.org/v2/top-headlines?'
           f'country={country}&'
           f'category={category}&'
           f'pageSize={page_size}&'
           f'page={page_number}&'
           'apiKey=6833f76c2dd3469a8a5bbe2d8741fbd5'
           )
    response1 = requests.get(url)
    pprint.pprint(response1.json())

def api_keywords(keywords,page_size='20',page_number='1',country='ru'):
    url = ('https://newsapi.org/v2/top-headlines?'
           f'country={country}&'
           f'q={keywords}&'
           f'pageSize={page_size}&'
           f'page={page_number}&'
           'apiKey=6833f76c2dd3469a8a5bbe2d8741fbd5'
           )
    response1 = requests.get(url)
    pprint.pprint(response1.json())

def api_req(req,page_size='20',page_number='1',language='ru'):
    url = ('https://newsapi.org/v2/everything?'
           f'q={req}&'
           f'pageSize={page_size}&'
           f'page={page_number}&'
           f'language={language}&'
           'apiKey=6833f76c2dd3469a8a5bbe2d8741fbd5'
           )
    response1 = requests.get(url)
    pprint.pprint(response1.json())
api_req('bitcoin')