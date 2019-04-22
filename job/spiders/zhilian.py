# -*- coding: utf-8 -*-
import scrapy
import json
from job.items import JobItem
from scrapy_redis.spiders import RedisSpider


class ZhilianSpider(RedisSpider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_seq = 0
    base_url = 'https://fe-api.zhaopin.com/c/i/sou?start=%d&pageSize=90&cityId=801&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%s&kt=3&_v=0.87230995&x-zp-page-request-id=80eb5e882e0145c48a43701726450d17-1555897693015-366844'
    #start_urls = [base_url % (start_seq, 'python')]
    has_next = False
    redis_key = "zhilian:start_urls"
    def parse(self, response):
        ret = json.loads(response.body)
        self.has_next = False
        if ret['code'] == 200:
            positions = ret['data']['results']
            if len(positions) > 0:
                self.has_next = True
                for position in positions:
                    detail_url = position['positionURL']
                    createDate = position['createDate']
                    updateDate = position['updateDate']
                    endDate = position['endDate']
                    item = JobItem(createDate=createDate,
                                   updateDate=updateDate,
                                   endDate=endDate,
                                   positionURL=detail_url)

                    yield scrapy.Request(url=detail_url, callback=self.parse_job_detail, meta={'info': item})

        if self.has_next:
            self.start_seq += 90
            yield scrapy.Request(url=self.base_url % (self.start_seq, 'python'), callback=self.parse)

    def parse_job_detail(self, response):
        jobName = response.xpath("//h3/text()").get().strip()
        salary = response.xpath("//span[@class='summary-plane__salary']/text()").get()
        workingExp = response.xpath("//ul[@class='summary-plane__info']//li//text()").getall()
        welfare = response.xpath("//div[@class='highlights__content']//span//text()").getall()
        jobDetail = response.xpath("//div[@class='describtion__detail-content']//p//text()").getall()[1:]
        businessArea = response.xpath("//span[@class='job-address__content-text']//text()").get()
        companyName = response.xpath("//a[@class='company__title']/text()").get()
        companyIndustry = response.xpath("//button[@class='company__industry']/text()").get()
        companySize = response.xpath("//button[@class='company__size']/text()").get()

        info_item = response.meta['info']
        info_item['welfare'] = welfare
        info_item['salary'] = salary
        info_item['workingExp'] = workingExp
        info_item['welfare'] = welfare
        info_item['jobName'] = jobName
        info_item['businessArea'] = businessArea
        info_item['jobDetail'] = jobDetail
        info_item['companyName'] = companyName
        info_item['companyIndustry'] = companyIndustry
        info_item['companySize'] = companySize
        return info_item
