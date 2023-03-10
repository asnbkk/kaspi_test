

import requests
from utils import group_list
from bs4 import BeautifulSoup
import json

URL = 'https://www.ozon.ru/category/mikrovolnovye-pechi-10546/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=микроволновая печь'
data = '__Secure-access-token=3.0.Kl7Mw9j_TGG-QZYzBxahsw.2.l8cMBQAAAABjz4-MNgM6vaN3ZWKgAICQoA..20230124095804.gv8yeQY2SuLlbIqiH9qgEdNKIgtZfpgi0aKli5kSDzA; __Secure-refresh-token=3.0.Kl7Mw9j_TGG-QZYzBxahsw.2.l8cMBQAAAABjz4-MNgM6vaN3ZWKgAICQoA..20230124095804.p8c2fs7KuGWYx6XTB8pp1AveR4mZtJ8RMf93K-QgWE8; __Secure-ab-group=2; __Secure-user-id=0; AREA_ID=40725; xcid=856f00e422cb9e4e5cfcbad57b0b196c; __Secure-ext_xcid=856f00e422cb9e4e5cfcbad57b0b196c; __cf_bm=eS.xGpDWy5wBdzqOMGiLIn_ut8B.x3MKimui294HanE-1674547089-0-AS4VNnAjhmTx7DZyZVjJdak/7oMAZWXKBuny7sQRS5QPpqTzprqCSSEHnao/F7huwkaxOc5FJwFgAOpQ4051bVS04D14jCLkX5QoqeRyYa7PjfleyK1jPHy/WfH3LS9q4ImPwLr3r/SSWHcc0iZspBqXxiY3cpEqc5ubs1uS4e3C6CTw1cZdv5vlJs7PC2jYvA==; rfuid=LTEzNjEzNDU0MDcsMzUuNzM4MzI5NTkzMDkyMiwtMTMzMzA5NzI5MSxJbnRlbCBNYWMgT1MgWCAxMC4xNSwtMTM1NDYwMTEyNSxXM3NpYm1GdFpTSTZJbEJFUmlCV2FXVjNaWElpTENKa1pYTmpjbWx3ZEdsdmJpSTZJbEJ2Y25SaFlteGxJRVJ2WTNWdFpXNTBJRVp2Y20xaGRDSXNJbTFwYldWVWVYQmxjeUk2VzNzaWRIbHdaU0k2SW1Gd2NHeHBZMkYwYVc5dUwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjBzZXlKMGVYQmxJam9pZEdWNGRDOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5WFgwc2V5SnVZVzFsSWpvaVEyaHliMjFsSUZCRVJpQldhV1YzWlhJaUxDSmtaWE5qY21sd2RHbHZiaUk2SWxCdmNuUmhZbXhsSUVSdlkzVnRaVzUwSUVadmNtMWhkQ0lzSW0xcGJXVlVlWEJsY3lJNlczc2lkSGx3WlNJNkltRndjR3hwWTJGMGFXOXVMM0JrWmlJc0luTjFabVpwZUdWeklqb2ljR1JtSW4wc2V5SjBlWEJsSWpvaWRHVjRkQzl3WkdZaUxDSnpkV1ptYVhobGN5STZJbkJrWmlKOVhYMHNleUp1WVcxbElqb2lRMmh5YjIxcGRXMGdVRVJHSUZacFpYZGxjaUlzSW1SbGMyTnlhWEIwYVc5dUlqb2lVRzl5ZEdGaWJHVWdSRzlqZFcxbGJuUWdSbTl5YldGMElpd2liV2x0WlZSNWNHVnpJanBiZXlKMGVYQmxJam9pWVhCd2JHbGpZWFJwYjI0dmNHUm1JaXdpYzNWbVptbDRaWE1pT2lKd1pHWWlmU3g3SW5SNWNHVWlPaUowWlhoMEwzQmtaaUlzSW5OMVptWnBlR1Z6SWpvaWNHUm1JbjFkZlN4N0ltNWhiV1VpT2lKTmFXTnliM052Wm5RZ1JXUm5aU0JRUkVZZ1ZtbGxkMlZ5SWl3aVpHVnpZM0pwY0hScGIyNGlPaUpRYjNKMFlXSnNaU0JFYjJOMWJXVnVkQ0JHYjNKdFlYUWlMQ0p0YVcxbFZIbHdaWE1pT2x0N0luUjVjR1VpT2lKaGNIQnNhV05oZEdsdmJpOXdaR1lpTENKemRXWm1hWGhsY3lJNkluQmtaaUo5TEhzaWRIbHdaU0k2SW5SbGVIUXZjR1JtSWl3aWMzVm1abWw0WlhNaU9pSndaR1lpZlYxOUxIc2libUZ0WlNJNklsZGxZa3RwZENCaWRXbHNkQzFwYmlCUVJFWWlMQ0prWlhOamNtbHdkR2x2YmlJNklsQnZjblJoWW14bElFUnZZM1Z0Wlc1MElFWnZjbTFoZENJc0ltMXBiV1ZVZVhCbGN5STZXM3NpZEhsd1pTSTZJbUZ3Y0d4cFkyRjBhVzl1TDNCa1ppSXNJbk4xWm1acGVHVnpJam9pY0dSbUluMHNleUowZVhCbElqb2lkR1Y0ZEM5d1pHWWlMQ0p6ZFdabWFYaGxjeUk2SW5Ca1ppSjlYWDFkLFd5SmxiaTFWVXlJc0ltVnVMVlZUSWl3aVpXNGlYUT09LDAsMSwwLDMwLC0xLC0xLDIyNzEyNjUyMCwwLDEsMCwtNDkxMjc1NTIzLElFNWxkSE5qWVhCbElFZGxZMnR2SUUxaFkwbHVkR1ZzSURVdU1DQW9UV0ZqYVc1MGIzTm9LU0F5TURFd01ERXdNU0JOYjNwcGJHeGgsZTMwPSw2NSwtMTc4ODMxOTE5MSwxLDEsLTEsMTY5OTk1NDg4NywxNjk5OTU0ODg3LC0xNDYxNTE4MTIsNg==; _ga_JNVTMNXQ6F=GS1.1.1674547089.1.1.1674547109.40.0.0; _ga=GA1.1.1264252764.1674547089; __exponea_etc__=c4f0675b-8ead-44cb-90e0-6e2778b12355; __exponea_time2__=0.438251256942749; tmr_lvid=e153181fc6c7070a8c0186c0d686c702; tmr_lvidTS=1674547093037; tmr_detect=0%7C1674547111869'
# data={"type":"avails-container","containers":[{"id":"as-n2gqSV","data":{"id":"29dbba30-5a89-11e5-8123-00155d03361b","checkPrice":'true'}},{"id":"as-VxQx6e","data":{"id":"f0fd24cc-1440-11eb-a211-00155d03332b","checkPrice":'true'}},{"id":"as-tPstWn","data":{"id":"2734838e-e1ac-11ea-a224-00155d03333a","checkPrice":'true'}},{"id":"as-oEseoB","data":{"id":"cb3701b4-2ee1-11e7-ac91-00155d03330d","checkPrice":'true'}},{"id":"as-lVci4a","data":{"id":"8e4356f0-09a1-11ea-b324-00155d03330f","checkPrice":'true'}},{"id":"as-6fw62l","data":{"id":"3b9fa525-2314-11e7-84f4-00155d03330d","checkPrice":'true'}},{"id":"as-0qhS-X","data":{"id":"4cfe5d18-2314-11e7-84f4-00155d03330d","checkPrice":'true'}},{"id":"as-H16asg","data":{"id":"8e4356f2-09a1-11ea-b324-00155d03330f","checkPrice":'true'}},{"id":"as-SdriB3","data":{"id":"24e33830-182e-11ea-b324-00155d03330f","checkPrice":'true'}},{"id":"as-tG4Pxn","data":{"id":"0f895342-0fab-11e8-80a7-00155d03330d","checkPrice":'true'}},{"id":"as-Lr7U75","data":{"id":"2ab68eb4-0fab-11e8-80a7-00155d03330d","checkPrice":'true'}},{"id":"as-sFLxUi","data":{"id":"066aea1b-13a5-11e9-8109-00155d03330f","checkPrice":'true'}},{"id":"as-fOYN23","data":{"id":"7e003dbb-753a-11e8-9547-00155d03330d","checkPrice":'true'}},{"id":"as-UOiVM3","data":{"id":"4c1000ca-cd00-11e8-a201-00155df1b806","checkPrice":'true'}},{"id":"as-NgChwr","data":{"id":"80cbdd51-ccff-11e8-a201-00155df1b806","checkPrice":'true'}},{"id":"as-nIv5N2","data":{"id":"51fc6074-586c-11ea-a20f-00155d03332b","checkPrice":'true'}},{"id":"as-ZZd-6c","data":{"id":"eb16846a-9cd1-11eb-a24c-00155dd2ff18","checkPrice":'true'}},{"id":"as-vnJzI1","data":{"id":"af486aa7-2248-11e6-b048-00155d033307","checkPrice":'true'}}]}
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0'}
r = requests.post(URL, verify=False, data=data, headers=header)
soup = BeautifulSoup(r.text, 'html.parser')
# print(json.loads(r.text))

# for index, i in enumerate(soup.find_all('script')):
    # print(i)
    # print(index)
    # print()

script = soup.find_all('script')[6]
json_str = script.text.split("window.__NUXT__.state=")[-1]
print(json_str.split('title')[4])

# spans = soup.find_all('a', class_='e7v
# for span in spans:
    # print(span.text)


