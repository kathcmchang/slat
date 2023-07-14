BOT_NAME = "sustainNLP"

SPIDER_MODULES = ["sustainNLP.spiders"]
NEWSPIDER_MODULE = "sustainNLP.spiders"

USER_AGENT = 'SustainabilityNLP'
ROBOTSTXT_OBEY = True

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

DOWNLOAD_DELAY = 5
DEPTH_LIMIT = 3

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

REDIRECT_MAX_TIMES = 3

ITEM_PIPELINES = {
    'sustainNLP.pipelines.ContentExtractor': 300,
    'sustainNLP.pipelines.CSVWriter': 800,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
