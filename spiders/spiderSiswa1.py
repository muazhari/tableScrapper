import scrapy
import os
import pandas as pd


class spiderSiswa1(scrapy.Spider):
    df = pd.read_csv("kelas.csv")
    tingkat1 = df['kelas'][df['kelas'].str.startswith('1')]

    name = 'spiderSiswa1'
    allowed_domains = ['baak.gunadarma.ac.id']
    start_urls = ['https://baak.gunadarma.ac.id/cariMhsBaru?tipeMhsBaru=Kelas&teks=' + x for x in tingkat1]

    fileFormat = 'csv'
    fileName = 'siswa1' + '.' + fileFormat
    fileAvailable = os.path.isfile(fileName)

    if fileAvailable:
        open(fileName, 'w+')

    custom_settings = {
        'FEED_FORMAT': fileFormat,
        'FEED_URI': fileName
    }

    def parse(self, response):
        MAIN_PATH = '/html/body/div/main/section[1]/div/div/div[1]'

        TABLE_PATH = MAIN_PATH + '/table[1]'
        TABLE_SELECTOR = response.xpath(TABLE_PATH)

        RECORD_XPATH = './/tr[position()>1 and position()<=last()]'
        RECORD_SELECTOR = TABLE_SELECTOR.xpath(RECORD_XPATH)

        for rset in RECORD_SELECTOR:
            yield {
                'nomor': rset.xpath('.//td[1]/text()').extract_first(),
                'no_pend': rset.xpath('.//td[2]/text()').extract_first(),
                'nama': rset.xpath('.//td[3]/text()').extract_first(),
                'npm': rset.xpath('.//td[4]/text()').extract_first(),
                'kelas': rset.xpath('.//td[5]/text()').extract_first(),
                'keterangan': rset.xpath('.//td[6]/text()').extract_first(),
            }

        NEXT_PAGE_SELECTOR = MAIN_PATH + '/center/nav/ul/ul/li[last()]/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
