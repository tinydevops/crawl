# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 定义存储数据结构
class JobItem(scrapy.Item):
    # 创建时间
    createDate = scrapy.Field()
    # 更新时间
    updateDate = scrapy.Field()
    # 结束时间
    endDate = scrapy.Field()
    # 职位URL
    positionURL = scrapy.Field()
    # 福利
    welfare = scrapy.Field()
    # 薪资
    salary = scrapy.Field()
    # 工作年限
    workingExp = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 公司行业
    companyIndustry = scrapy.Field()
    # 公司规模
    companySize = scrapy.Field()
    # 职位名称
    jobName = scrapy.Field()
    # 地区
    businessArea = scrapy.Field()
    # 职位描述
    jobDetail = scrapy.Field()
