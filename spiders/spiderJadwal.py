import scrapy
import os
import pandas as pd


class spiderJadwal(scrapy.Spider):
    df = pd.read_csv('kelas.csv')
    kelas = df['kelas']

    name = 'spiderJadwal'
    allowed_domains = ['baak.gunadarma.ac.id']
    start_urls = ['https://baak.gunadarma.ac.id/jadwal/cariJadKul?teks=' + x for x in kelas]

    fileFormat = 'csv'
    fileName = 'jadwal' + '.' + fileFormat
    fileAvailable = os.path.isfile(fileName)

    if not fileAvailable:
        custom_settings = {
            'FEED_FORMAT': fileFormat,
            'FEED_URI': fileName
        }

    def parse(self, response):
        item = {}
        MAIN_PATH = '/html/body/div/main/section[3]/div/div/div'

        TABLE_PATH = MAIN_PATH + '/table[2]'
        TABLE_SELECTOR = response.xpath(TABLE_PATH)

        RECORD_XPATH = './/tr[position()>1 and position()<=last()]'
        RECORD_SELECTOR = TABLE_SELECTOR.xpath(RECORD_XPATH)

        for rset in RECORD_SELECTOR:
            yield {
                'kelas': rset.xpath('.//td[1]/text()').extract_first(),
                'hari': rset.xpath('.//td[2]/text()').extract_first(),
                'mata_kuliah': rset.xpath('.//td[3]/text()').extract_first(),
                'waktu': rset.xpath('.//td[4]/text()').extract_first(),
                'ruang': rset.xpath('.//td[5]/text()').extract_first(),
                'dosen': rset.xpath('.//td[6]/text()').extract_first(),
            }

        NEXT_PAGE_SELECTOR = MAIN_PATH + '/center/nav/ul/ul/li[last()]/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
