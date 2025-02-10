import requests, time


headers = {'Host': 'www.cnvd.org.cn', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'https://www.cnvd.org.cn/flaw/show/CNVD-2025-02160', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
cookies = {'__jsluid_s': '43220482fc74d8c54e1af31be3a3c785', '__jsl_clearance_s': '1739173641.262|0|4qUT7uhoTnrO7Oj8RyXx6b5ARlg%3D', 'JSESSIONID': 'A0B899884B28D071D3B77CFCE30C1737'}

urls = ['https://www.cnvd.org.cn/flaw/show/CNVD-2025-02160',
        'https://www.cnvd.org.cn/flaw/show/CNVD-2025-01223']
for i in urls:
    response = requests.get(i, headers=headers, cookies=cookies)
    print(response.status_code)
    time.sleep(4)


