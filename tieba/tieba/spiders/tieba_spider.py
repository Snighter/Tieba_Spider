import time
import scrapy
import random
from tieba.items import TiebaItem

class TiebaSpider(scrapy.Spider):
    name = 'tieba_spider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ["https://tieba.baidu.com/f?kw=bilibili"]

    def __init__(self, *args, **kwargs):
        super(TiebaSpider, self).__init__(*args, **kwargs)
        self.count = 0

    def parse(self, response):
        for tieba in response.css('li.j_thread_list'):
            item = TiebaItem()
            item['title'] = tieba.css('a.j_th_tit ::attr(title)').extract_first()
            item['author'] = tieba.css('span.tb_icon_author ::attr(title)').extract_first().split(":")[-1]
            item['reply'] = tieba.css('span.threadlist_rep_num::text').extract_first()
            item['link'] = response.urljoin(tieba.css('a.j_th_tit::attr(href)').extract_first())

            # 发起请求获取帖子信息
            # time.sleep(8 + 4 * random.random())
            yield scrapy.Request(item['link'], callback=self.fetch_post_info, meta={'item': item})

        # 增加计数器，检查是否达到 10
        self.count += 1
        if self.count >= 10:
            return  # 停止爬取

        # 处理下一页

        # time.sleep(12 + 6 * random.random())
        next_page = response.css('a.next::attr(href)').extract_first()
        if next_page is not None:
            next_full_page = response.urljoin(next_page)
            yield scrapy.Request(next_full_page, callback=self.parse, meta={'count': self.count})


    def fetch_post_info(self, response):
        item = response.meta['item']
        item['author_level'] = response.xpath('//*[@id="j_p_postlist"]/div[1]/div[1]/ul/li[4]/div/a/div[2]/text()').extract_first()
        if not item['author_level']:
            item['author_level'] = response.xpath('//*[@id="j_p_postlist"]/div[1]/div[1]/ul/li[5]/div/a/div[2]/text()').extract_first()
        item['ip'] = response.xpath('//*[@id="j_p_postlist"]/div[1]/div[2]/div[4]/div[1]/div/span[1]/text()').extract_first()
        item['os'] = response.xpath('//*[@id="j_p_postlist"]/div[1]/div[2]/div[4]/div[1]/div/span[4]/a/text()').extract_first()
        if not item['os']:
            item['os'] = "PC客户端"
        yield item
