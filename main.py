import requests
from lxml import etree
import copy
import json
import time
from cookie import CookieFetcher
import os


cookies = {
    "__jsluid_s": "",
    "JSESSIONID": "",
    "__jsl_clearance_s": ""
}


# 获取首页list，可指定页数
def get_page(page_num=1):
    headers = {'Host': 'www.cnvd.org.cn', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'https://www.cnvd.org.cn/flaw/show/CNVD-2025-02160', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

    global cookies
    offset = page_num * 10 - 10
    params = (
        ('flag', 'true'),
    )
    data = {
        'number': '\u8BF7\u8F93\u5165\u7CBE\u786E\u7F16\u53F7',
        'startDate': '',
        'endDate': '',
        'flag': 'true',
        'field': '',
        'order': '',
        'numPerPage': '10',
        'offset': str(offset),
        'max': '10'
    }
    response = requests.post('https://www.cnvd.org.cn/flaw/list', headers=headers, cookies=cookies, params=params, data=data)
    print('首页列表 状态码：', response.status_code)
    if response.status_code == 200:
        html = response.content
        element = etree.HTML(html)
        url_lis = element.xpath("//table[@class='tlist']//tbody//tr//td[1]//a//@href")
        title_lis = element.xpath("//table[@class='tlist']//tbody//tr//td[1]//a//@title")
        degree_lis = [t.strip() for t in element.xpath("//table[@class='tlist']//tbody//tr//td[2]/text()") if t.strip()]
        click_lis = [t.strip() for t in element.xpath("//table[@class='tlist']//tbody//tr//td[3]/text()") if t.strip()]
        date_lis = [t.strip() for t in element.xpath("//table[@class='tlist']//tbody//tr//td[6]/text()") if t.strip()]
        Bug_inform = {
            'url': '',
            'title': '',
            'degree': '',
            'click': '',
            'date': '',
            'inform': {}
        }
        Bug_lis = []
        for i in range(10):
            bug_dic = copy.deepcopy(Bug_inform)  # 字典深拷贝
            bug_dic['url'] = url_lis[i]
            bug_dic['title'] = title_lis[i]
            bug_dic['degree'] = degree_lis[i]
            bug_dic['click'] = click_lis[i]
            bug_dic['date'] = date_lis[i]
            Bug_lis.append(bug_dic)
        return Bug_lis
    elif response.status_code == 521:
        print("\ncookie 失效！正在更新cookie...\n")
        cookies = cookie_fetcher.new_cookie()
        time.sleep(3)
        print('更新完成，重新请求')
        return 'refresh'
    else:
        return False


# 获取详情页信息，传入指定url
def get_inform(url):
    headers = {'Host': 'www.cnvd.org.cn', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'https://www.cnvd.org.cn/flaw/show/CNVD-2025-02160', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
    global cookies
    url = 'https://www.cnvd.org.cn' + url
    response = requests.get(url, headers=headers, cookies=cookies)
    print('详情页 状态码：', response.status_code)
    if response.status_code == 200:
        html = response.content
        tree = etree.HTML(html)

        def clean_text(xpath_result):
            """清理字符串中的换行符、回车符、制表符和空格"""
            return "".join(xpath_result).replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')

        # 字段和对应的 XPath 映射
        field_to_xpath = {
            "CNVD-ID": '//tr[td[text()="CNVD-ID"]]/td[2]//text()',
            "公开日期": '//tr[td[text()="公开日期"]]/td[2]//text()',
            "危害级别": '//tr[td[text()="危害级别"]]/td[2]//text()',
            "影响产品": '//tr[td[text()="影响产品"]]/td[2]//text()',
            "CVE ID": '//tr[td[text()="CVE ID"]]/td[2]//text()',
            "漏洞描述": '//tr[td[text()="漏洞描述"]]/td[2]//text()',
            "漏洞类型": '//tr[td[text()="漏洞类型"]]/td[2]//text()',
            "参考链接": '//tr[td[text()="参考链接"]]/td[2]//text()',
            "漏洞解决方案": '//tr[td[text()="漏洞解决方案"]]/td[2]//text()',
            "厂商补丁": '//tr[td[text()="厂商补丁"]]/td[2]//text()',
            "验证信息": '//tr[td[text()="验证信息"]]/td[2]//text()',
            "报送时间": '//tr[td[text()="报送时间"]]/td[2]//text()',
            "收录时间": '//tr[td[text()="收录时间"]]/td[2]//text()',
            "更新时间": '//tr[td[text()="更新时间"]]/td[2]//text()',
            "漏洞附件": '//tr[td[text()="漏洞附件"]]/td[2]//text()',
        }

        # 使用字典推导式生成最终数据
        data = {field: clean_text(tree.xpath(xpath)) for field, xpath in field_to_xpath.items()}

        return data
    elif response.status_code == 521:
        print("\ncookie 失效！正在更新cookie...\n")
        cookies = cookie_fetcher.new_cookie()
        time.sleep(3)
        print('更新完成，重新请求')
        return 'refresh'
    else:
        return False


# 获取first_page到last_page间的所有页数，sleep_time设置请求时间间隔
def page(first_page=1, last_page=1, sleep_time=4):
    sum_ = (last_page - first_page + 1) * 10
    error = sum_
    json_lis = []
    with open("data.json", "w", encoding="utf-8") as json_file:
        for num in range(first_page, last_page+1):
            bug_lis = get_page(num)
            if bug_lis == 'refresh':
                time.sleep(sleep_time)
                bug_lis = get_page(num)
            if type(bug_lis) == list:
                for bug in bug_lis:
                    inform = get_inform(bug['url'])
                    if inform == 'refresh':
                        inform = get_inform(bug['url'])
                    if type(inform) == dict:
                        bug['inform'] = inform
                        # print(bug)
                        json_lis.append(bug)
                        error -= 1
                    else:
                        print('{0}详情页数据获取失败！'.format(bug['url']))
                    time.sleep(sleep_time)
            else:
                print('第{0}页列表获取失败！'.format(str(num)))
        json.dump(json_lis, json_file, ensure_ascii=False, indent=4)
    print("\n\n目标爬取", sum_)
    print("成功", sum_ - error, "   失败", error)


if __name__ == '__main__':
    '''
        CookieFetcher : cookie模块， 实例化时传入msedgedriver.exe路径。成员new_cookie函数获取更新后的cookie
        get_page : 传入想抓取的页数，返回该页的数据列表
        get_inform : 传入想抓取的详情页url，返回包含该详情页信息的字典
        page ：传入想抓取的起始页和结束页，也可以设置请求时间间隔sleep_time。
                因为未做随机ip，所以需时间设长些，否则容易封ip
    '''
    # 获取当前脚本所在目录的路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建 msedgedriver 的相对路径
    edge_driver_path = os.path.join(current_dir, "msedgedriver.exe")
    # 创建 CookieFetcher 实例
    cookie_fetcher = CookieFetcher(edge_driver_path)
    cookies = cookie_fetcher.new_cookie()

    # page(1, 2)
    # get_page(1)
    # print(get_inform('/flaw/show/CNVD-2025-02380'))
    '''urls = ['/flaw/show/CNVD-2025-02160',
            '/flaw/show/CNVD-2025-01223']
    for i in urls:
        response = get_inform(i)
        print(response)
        time.sleep(4)'''

    while True:
        num_lis = [int(num) for num in input('请输入要抓取的起始页和终止页序号（如：5 10）：').split(' ') if num != '']
        if len(num_lis) == 2:
            page(num_lis[0], num_lis[1], 10)



