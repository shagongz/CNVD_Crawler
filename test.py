import requests, time

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6','priority': 'u=0, i',
    'referer': 'https://www.cnvd.org.cn/flaw/list?flag=true',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'cookie': '__jsluid_s=46ac8a65c5b9583c223747c5fb98da80; __jsl_clearance_s=1737707621.885|0|uFlhkHO4Qn0jXAwF%2FNvnYGW5Hlw%3D; JSESSIONID=15533EC5E99A874159177C32F0736B15',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
}
urls = ['https://www.cnvd.org.cn/flaw/show/CNVD-2025-02160',
        'https://www.cnvd.org.cn/flaw/show/CNVD-2025-01223']
for i in urls:
    response = requests.get(i, headers=headers)
    print(response.status_code)
    time.sleep(4)


