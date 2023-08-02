import requests
from get_jsession_id import get_all_cookies

# from smartphone_parser import get_proxy


def get_headers(page):
    # setting ks.ngs.s
    # url = "https://kaspi.kz/shop/ab?pt=CATEGORY_1"
    # headers = get_primary_headers()
    # response = requests.get(url, headers=headers)

    # secondary_cookies = response.cookies.get("ks.ngs.s")
    ks_ngs_s, jsessionid, k_stat, ks_tg = get_all_cookies(page)
    headers = {
        "Host": "kaspi.kz",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept": "application/json, text/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.5",
        "Referer": f"https://kaspi.kz/shop/c/smartphones%20and%20gadgets/?source=kaspikz&page={page}",
        "Cookie": f"current-action-name=Index; .AspNetCore.Culture=c%3Dru%7Cuic%3Dru; k_stat={k_stat}; ks.tg={ks_tg}; ssaid=f6b35f40-0f43-11ee-bc0d-a34955185617; kaspi.storefront.cookie.city=750000000; ks.ngs.s={ks_ngs_s}; __tld__=null",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "Connection": "keep-alive",
    }

    return headers
