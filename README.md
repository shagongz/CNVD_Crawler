### 爬取网址：https://www.cnvd.org.cn

### 依赖库
>    selenium  
>    requests  
>    lxml  
>    copy  
>    json  
>    time  
>    cookie（自写模块，已包含）

### 浏览器驱动：
>    msedgedriver.exe(已包含)

### 使用
- 输入起始页和终止页，中间空一格。  
- 会抓取首页列表和详情页信息  
- 最终保存为json  
### 封IP问题
该网站限制了请求频率，请求过快会封ip  
所以要想提高爬虫速度  
需要使用ip代理池，以及多线程
```
因为未做ip代理，所以尽量降低请求频率，否则容易封ip
设置了每次请求等待5秒
```


