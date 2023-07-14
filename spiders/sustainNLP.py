from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
import re
from sustainNLP.items import sustainItem


class WebSpider(Spider):
    name = "sustainNLP"
    
    def __init__(self, *args, **kwargs):
        super(WebSpider, self).__init__(*args, **kwargs)
        
        self.file_path = "sme.txt"
        self.whitelist = ['sustainab', 'green', 'eco', 'renewable', 'recycl', 'carbon-neutral', 'net-zero', 'climate', 'energy-efficiency', 'waste-management', 'conservat', 'biodivers', 'emission', 'clean', 'organic', 'natural-resource', 'pollut', 'environmental', 'sustainable-development', 'greenhouse']
        self.blacklist = ['document', 'blog', 'product', 'news', 'press', 'archive', 'search', 'login']
        self.extractor = LinkExtractor()

    def start_requests(self):
        with open(self.file_path) as f:
            for line in f:
                [url, company] = line.split(',')
                try:
                    url = url.strip()
                    request = Request(url)
                    request.meta.update(company = company.strip())
                    yield request
                except:
                    continue

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            return

        domain_origin = urlparse(response.url).netloc
        url = response.url

        if response.meta.get('keywords', ()):
            yield self.process_item(response)

        for link in self.extractor.extract_links(response):
            domain_this = urlparse(link.url).netloc
            if domain_this != domain_origin:
                continue

            link_str = ' '.join([link.text.lower(), link.url.lower()])
            keywords = list(set(re.findall("|".join(self.whitelist), link_str, flags = re.I)))
            flashcards = list(set(re.findall("|".join(self.blacklist), link_str, flags = re.I)))

            if not keywords and flashcards:
                continue

            request = Request(url = link.url)
            request.meta.update({'link_text': link.text, 'keywords': keywords, 'company': response.meta['company']})
            yield request

    def process_item(self, response):
        if response.meta.get('keywords', ()):
            item = sustainItem()
            item['url'] = response.url
            item['link_text'] = response.meta['link_text']
            item['company'] = response.meta['company']
            item['content'] = response.body
            item['keywords'] = response.meta['keywords']
            yield item
