from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time


class CookieFetcher:
    def __init__(self, edge_driver_path):
        # 设置 Edge 浏览器选项
        self.edge_options = Options()

        # 禁用自动化标识
        self.edge_options.add_argument("--disable-blink-features=AutomationControlled")

        # 设置 WebDriver 路径
        self.edge_driver_path = edge_driver_path

        # 创建 Edge 服务对象
        self.service = Service(self.edge_driver_path)

        # 启动 Edge 浏览器
        self.driver = webdriver.Edge(service=self.service, options=self.edge_options)

        # 打开目标网站
        self.driver.get("https://www.cnvd.org.cn/flaw/list")

        # 等待页面加载
        self.driver.implicitly_wait(100)

        # 等待加载
        time.sleep(3)

    def new_cookie(self, url="https://www.cnvd.org.cn/flaw/list"):
        # 打开目标网站
        self.driver.get(url)

        # 等待页面加载
        self.driver.implicitly_wait(100)

        # 获取 cookies
        cookies = self.driver.get_cookies()

        # 解析 cookies
        c = {}
        for cookie in cookies:
            if cookie['name'] == '__jsl_clearance_s':
                c['__jsl_clearance_s'] = cookie['value']
            elif cookie['name'] == 'JSESSIONID':
                c['JSESSIONID'] = cookie['value']
            elif cookie['name'] == '__jsluid_s':
                c['__jsluid_s'] = cookie['value']
            else:
                return False
        return c

    def close_browser(self):
        # 关闭浏览器
        self.driver.quit()


if __name__ == "__main__":
    edge_driver_path = "C:\\Python\\Python39\\msedgedriver.exe"

    # 创建 CookieFetcher 实例
    cookie_fetcher = CookieFetcher(edge_driver_path)

    # 关闭浏览器
    # cookie_fetcher.close_browser()
    while True:
        if input():
            cookie = cookie_fetcher.new_cookie()
            print(cookie)
