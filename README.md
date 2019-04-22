# crawl
智联职位爬虫

# scrapy + elasticsearch +mongdb

# 分析
* [搜索页面](https://sou.zhaopin.com/?jl=801&sf=0&st=0&kw=python&kt=3)
* 查看`网页源码`，没有找到页面中出现的职位信息，这些数据应该是通过异步方式加载进来的。
* 打开浏览器`开发者工具`(F12)，选择`Network`，查看`XHR`，数据实际请求的是`https://fe-api.zhaopin.com/c/i/sou?startSize=0&pageSize=90&cityId=801&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&_v=0.21529939&x-zp-page-request-id=3fa001d5b6e64747853ff6448b6416ff-1555914974605-972967`。其中`startSize`表示请求偏移(90的倍数)，`pangeSize`固定为90，`kw`职位关键字，支持中文。接口返回数据为json格式，提取其中的`positionURL`字段再次传入引擎。
* 分析好的职位信息支持写入elasticsearch 和mongdb
