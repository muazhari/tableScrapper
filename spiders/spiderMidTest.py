import scrapy
import os
import pandas as pd


class spiderJadwalMidTest(scrapy.Spider):
    df = pd.read_csv('kelas.csv')
    kelas = df['kelas']

    name = 'spiderJadwalMidTest'
    allowed_domains = ['baak.gunadarma.ac.id']
    start_urls = ['https://baak.gunadarma.ac.id/jadwal/cariUts?teks=' + x for x in kelas]

    fileFormat = 'csv'
    fileName = 'jadwalMidTest' + '.' + fileFormat
    fileAvailable = os.path.isfile(fileName)

    if fileAvailable:
        open(fileName, 'w+')

    custom_settings = {
        'FEED_FORMAT': fileFormat,
        'FEED_URI': fileName
    }

    def parse(self, response):
        item = {}
        MAIN_XPATH = '/html/body/div/main/section[3]/div/div/div'

        KELAS = response.xpath(MAIN_XPATH + '/p/b/text()').extract_first()

        TABLE_XPATH = MAIN_XPATH + '/table[2]'
        TABLE_SELECTOR = response.xpath(TABLE_XPATH)

        RECORD_XPATH = './/tr[position()>1 and position()<=last()]'
        RECORD_SELECTOR = TABLE_SELECTOR.xpath(RECORD_XPATH)

        for rset in RECORD_SELECTOR:
            yield {
                'kelas': KELAS,
                'hari': rset.xpath('.//td[1]/text()').extract_first(),
                'tanggal': rset.xpath('.//td[2]/text()').extract_first(),
                'mata_kuliah': rset.xpath('.//td[3]/text()').extract_first(),
                'waktu': rset.xpath('.//td[4]/text()').extract_first(),
                'ruang': rset.xpath('.//td[5]/text()').extract_first(),
            }

        NEXT_PAGE_SELECTOR = MAIN_XPATH + '/center/nav/ul/ul/li[last()]/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
