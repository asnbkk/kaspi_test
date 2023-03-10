import requests
import random

host_list = [
    '212.116.246.202', '91.147.126.179', '185.120.78.201',
    '46.8.31.101', '109.248.199.58',
    '185.120.78.220', '212.116.244.223', '91.147.126.195']

USERNAME = 'bekkaliyevassan'
PASS = 'JgMqRpcssL'
PORT = '49155'

def gerenate_proxy():
    HOST = random.choice(host_list)
    
    proxy = {
        'http': f'http://{USERNAME}:{PASS}@{HOST}:{PORT}',
        'https': f'http://{USERNAME}:{PASS}@{HOST}:{PORT}',
    }
    
    return proxy