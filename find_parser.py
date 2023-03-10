import requests
from fake_headers import Headers
import re
from bs4 import BeautifulSoup
from getting_proxy import gerenate_proxy
# import warnings

# suppress all warnings
# warnings.filterwarnings("ignore")

headers = Headers()
header = headers.generate()
URL = 'https://www.whatsmyua.info/'

print(header)
# r = requests.get(URL, verify=False, headers=header)
# print(r.text)
