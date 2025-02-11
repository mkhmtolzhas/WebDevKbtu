import time
import requests


def get_laptops(page: int):
    cookies = {
        'ks.tg': '8',
        'k_stat': '55263dcd-2e73-428b-9419-6f8673c47370',
        'kaspi.storefront.cookie.city': '750000000',
        'locale': 'ru-RU',
        '_hjSessionUser_283363': 'eyJpZCI6IjA1N2JiMzQ2LWU4YjMtNTE0Mi05NzIyLTRjM2FhMTRlMDg5YiIsImNyZWF0ZWQiOjE3Mzk5MDA4MjI2ODQsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSession_283363': 'eyJpZCI6ImIxY2E1YzcxLTRmYTYtNDUyYi1hNjRiLWExMGU5NDhjZGNkZSIsImMiOjE3Mzk5MDc1NDIzNzksInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
        'Accept': 'application/json, text/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'X-KS-City': '750000000',
        'Connection': 'keep-alive',
        'Referer': 'https://kaspi.kz/shop/c/notebooks/?q=%3AavailableInZones%3AMagnum_ZONE1%3Acategory%3ANotebooks&sort=relevance&sc&page=3',
        # 'Cookie': 'ks.tg=8; k_stat=55263dcd-2e73-428b-9419-6f8673c47370; kaspi.storefront.cookie.city=750000000; locale=ru-RU; _hjSessionUser_283363=eyJpZCI6IjA1N2JiMzQ2LWU4YjMtNTE0Mi05NzIyLTRjM2FhMTRlMDg5YiIsImNyZWF0ZWQiOjE3Mzk5MDA4MjI2ODQsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_283363=eyJpZCI6ImIxY2E1YzcxLTRmYTYtNDUyYi1hNjRiLWExMGU5NDhjZGNkZSIsImMiOjE3Mzk5MDc1NDIzNzksInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
    }

    response = requests.get(
        f'https://kaspi.kz/yml/product-view/pl/results?page={page}&q=%3Acategory%3ANotebooks%3AavailableInZones%3AMagnum_ZONE1&text&sort=relevance&qs&requestId=db9c8f578598c6dea568d5e3dfa25443&ui=d&i=-1&c=750000000',
        cookies=cookies,
        headers=headers,
    ).json()["data"]

    formatted_response = []

    for product in response:
        formatted_response.append({
            'title': product['brand'],
            'price': product['unitPrice'],
            'description': product['title'],
            'category': 'Laptops',
            'link': f"https://kaspi.kz/shop{product['shopLink']}",
            'rating': product['rating'],
            'image': product['previewImages'][0]['medium'],
        })
    
    for product in formatted_response:
        response = requests.post('http://localhost:8000/api/v1/products/', json=product)
        print(response.json())



if __name__ == '__main__':
    for page in range(0, 424):
        if page == 0:
            get_laptops(page)
        elif page % 100 == 0:
            time.sleep(10)
        get_laptops(page)


