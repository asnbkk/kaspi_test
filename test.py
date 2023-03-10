import requests
import json
from fake_headers import Headers
import re
from bs4 import BeautifulSoup
from getting_proxy import gerenate_proxy
import warnings

# suppress all warnings
warnings.filterwarnings("ignore")

headers = Headers()
header = headers.generate()
header['Referer'] = 'https://kaspi.kz/shop/c/categories/'
 
# send to utils
urls = [
    'https://kaspi.kz/shop/c/smartphones%20and%20gadgets/', 'https://kaspi.kz/shop/c/home%20equipment/', 
    'https://kaspi.kz/shop/c/tv_audio/', 'https://kaspi.kz/shop/c/computers/', 'https://kaspi.kz/shop/c/office/',  
    'https://kaspi.kz/shop/c/beauty%20care%20equipment/', 'https://kaspi.kz/shop/c/medical%20equipment/', 
    'https://kaspi.kz/shop/c/power%20tools/', 'https://kaspi.kz/shop/c/construction%20equipment/', 
    'https://kaspi.kz/shop/c/exercise%20and%20fitness/', 'https://kaspi.kz/shop/c/cycling/', 
    'https://kaspi.kz/shop/c/kick%20scooters/', 'https://kaspi.kz/shop/c/musical%20instruments/', 
    'https://kaspi.kz/shop/c/tires/', 'https://kaspi.kz/shop/c/car%20electronics/',  
    'https://kaspi.kz/shop/c/automotive%20equipments/', 'https://kaspi.kz/shop/c/travel%20gear/',  
    'https://kaspi.kz/shop/c/home/', 'https://kaspi.kz/shop/c/new%20year%20decor/'
]

def get_soup(URL):
    proxies = gerenate_proxy()
    
    r = requests.get(
        URL, 
        headers=header, 
        verify=False,
        proxies=proxies
    )
    print(r)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup 


links = []
for url in urls:
    soup = get_soup(url)
    for script in soup.find_all('script'):
        if 'catalogGrid' in script.text:
            res = script \
                .text \
                .split('.catalogGrid = ')[-1] \
                .split(';\n')[0]
            json_res = json.loads(res)
            try:
                for i in json_res['catalogFirst']['cards']:
                    for row in i['rows']:
                        for link in row['links']:
                            if 'https' in link['link']:
                                links.append(link['link'])
            except:
                links.append(url)

def get_content(link):
    soup = get_soup(link)
    for script in soup.find_all('script'):
        if 'var listing = {' in script.text:
            res = script.text.split('var listing = ')[-1].split(';\n')[0]
            json_str = re.sub(r',\s*]', ']', res)
            json_res = json.loads(json_str)
            return json_res
        
print(len(links))
        
for link in links:
    json_res = get_content(link)
    pages_count = json_res['pagesCount']
    print(pages_count)
    for i in range(1, pages_count):
        items = get_content(link + f'?page={i}')['items']
        # preprocess and save
        print(items)