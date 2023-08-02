import requests


def get_all_cookies(page):
    headers = {
        "Host": "kaspi.kz",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    url = f"https://kaspi.kz/shop/c/smartphones%20and%20gadgets/?source=kaspikz&page={page}"

    res = requests.get(url, headers=headers)

    ks_ngs_s = res.cookies.get("ks.ngs.s")
    jsessionid = res.cookies.get("JSESSIONID")
    k_stat = res.cookies.get("k_stat")
    ks_tg = res.cookies.get("ks.tg")

    print(ks_ngs_s)
    print(jsessionid)
    print(k_stat)
    print(ks_tg)

    return ks_ngs_s, jsessionid, k_stat, ks_tg
