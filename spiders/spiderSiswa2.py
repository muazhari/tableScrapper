import scrapy
import os
import pandas as pd

class spiderSiswa2(scrapy.Spider):
    df = pd.read_csv("kelas.csv")
    tingkat2 = df['kelas'][df['kelas'].str.startswith('1')]

    name = 'spiderSiswa2'
    allowed_domains = ['baak.gunadarma.ac.id']
    start_urls = ['https://baak.gunadarma.ac.id/cariKelasBaru?tipeKelasBaru=Kelas&teks=' + x for x in tingkat2]

    fileFormat = 'csv'
    fileName = 'siswa2' + '.' + fileFormat
    fileAvailable = os.path.isfile(fileName)

    if fileAvailable:
        open(fileName, 'w+')

    custom_settings = {
        'FEED_FORMAT': fileFormat,
        'FEED_URI': fileName
    }

    def parse(self, response):
        MAIN_XPATH = '/html/body/div/main/section[1]/div/div/div[1]'

        TABLE_XPATH = MAIN_XPATH + '/table[1]'
        TABLE_SELECTOR = response.xpath(TABLE_XPATH)

        RECORD_XPATH = './/tr[position()>1 and position()<=last()]'
        RECORD_SELECTOR = TABLE_SELECTOR.xpath(RECORD_XPATH)

        for rset in RECORD_SELECTOR:
            yield {
                'nomor': rset.xpath('.//td[1]/text()').extract_first(),
                'npm': rset.xpath('.//td[2]/text()').extract_first(),
                'nama': rset.xpath('.//td[3]/text()').extract_first(),
                'kelas_lama': rset.xpath('.//td[4]/text()').extract_first(),
                'kelas_baru': rset.xpath('.//td[5]/text()').extract_first(),
            }

        NEXT_PAGE_SELECTOR = MAIN_XPATH + '/center/nav/ul/ul/li[last()]/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
