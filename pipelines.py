import csv
from bs4 import BeautifulSoup
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

settings = get_project_settings()


class ContentExtractor(object):
    def process_item(self, item, spider):
        fullHTML = item['content']
        soup = BeautifulSoup(fullHTML, 'html.parser')
        content = soup.get_text(separator=' ')
        item['content'] = content
        return item


class CSVWriter(object):
    def __init__(self):
        self.file = open('scraped_data.csv', 'w', newline='')
        self.writer = csv.writer(self.file)

        # Write header row
        self.writer.writerow(['url', 'company', 'content', 'keywords'])

    def process_item(self, item, spider):
        valid = True

        if not item['url']:
            valid = False
            raise DropItem("Missing url!")

        if not item['company']:
            valid = False
            raise DropItem("Missing company!")

        if valid:
            self.writer.writerow([item['url'], item['company'], item['content'], item['keywords']])
        
        return item

    def close_spider(self, spider):
        self.file.close()
