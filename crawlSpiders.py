from scrapy.crawler import CrawlerProcess
from multiprocessing import Pool
import os

def _crawl(spider_name=None):
    if spider_name:
        cmd = 'scrapy runspider ' + '.\spiders\\' + spider_name + '.py'
        os.system(cmd)
    return None


def run(spider_names):
    pool = Pool(processes=len(spider_names))
    pool.map(_crawl, spider_names)
