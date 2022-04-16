import scrapy
from scrapy import Request



class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['https://seattle.craigslist.org/search/est/cta','https://seattle.craigslist.org']
    start_urls = ['https://seattle.craigslist.org/search/est/cta/']

    def parse(self, response):
        #Getting all ads on a single page
        results = response.xpath('//div[@class="result-info"]')
        for result in results:
            title = result.xpath('h3[@class="result-heading"]/a[@class="result-title hdrlnk"]/text()').extract_first()
            price = result.xpath('span[@class="result-meta"]/span[@class="result-price"]/text()').extract_first()
            neighbourhood = result.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first().strip('+)').replace("(","")
            url = result.xpath('h3[@class="result-heading"]/a/@href').extract_first()
            
            #Browsing to the ad page and calling the parse_page function to scrape the description
            yield Request(url, callback = self.parse_page, dont_filter=True,
                          meta={'title':title, 'price':price, 'neighbourhood': neighbourhood, 'url': url})
        
        #Getting the link for the next button
        next_button = response.xpath('//a[@class="button next"]/@href').extract_first()
        next_url = "https://seattle.craigslist.org" + next_button
        
        yield Request(next_url, callback=self.parse, dont_filter=True)
            
            #yield {'title':title, 'price':price, 'neighbourhood': neighbourhood, 'url': ad_url}
                      
    def parse_page(self, response):
        title = response.meta['title']
        price = response.meta['price']
        neighbourhood = response.meta['neighbourhood']
        url = response.meta['url']
        ad_content = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract()).strip()
        
        yield {'title':title, 'price':price, 'neighbourhood': neighbourhood, 'url': url, 'ad_description': ad_content}
            
