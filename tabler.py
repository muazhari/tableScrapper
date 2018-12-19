'''

    Sorry if you saw my unskilled programming skill,
    bad documentation, grammar or English,
    and pardon me if you are confused about
    reading my messy and disorganized code.

    I'm trying my best to learn how to do it rightfully.

'''

from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from itertools import zip_longest
from os.path import isfile
import math


# Grouping a set of element for n
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


# QueryStrings to targeted url.
def params(tingkat, jurusan, kelas, page):
    parameter = {'teks': tingkat + jurusan + kelas,
                 'tipeMhsBaru': 'Kelas',
                 'page': page}
    if tingkat == '2':
        parameter['tipeKelasBaru'] = parameter.pop('tipeMhsBaru')
    return parameter


# Get raw data from html page.
def parsing(url, params):
    web = get(url, params)
    soup = BeautifulSoup(web.text, 'html.parser')
    return soup


# Find and Sort the table to single dataframe.
def extract(label, parsed):
    raw = parsed.find_all(
        'table',
        class_='table table-custom table-primary table-fixed bordered-table stacktable small-only')
    row = [x.get_text().strip() for x in raw[0].find_all('td')]
    return pd.DataFrame(list(grouper(row, len(label))), columns=label)


# Creating a dataframe recursively.
def tabling(url, label, tingkat, jurusan, kelas, page=1, count=None):
    if count != 0:
        parsed = parsing(url, params(tingkat, jurusan, kelas, page))
        df = pd.DataFrame(columns=label).append(extract(label, parsed))
        if count == None:
            count = math.ceil(int(parsed.find_all(
                'p')[1].find('b').get_text().strip()) / 20)
        return df.append(
            tabling(
                url, label, tingkat, jurusan, kelas, page + 1, count - 1),
            ignore_index=True)


'''
Alternative for tabling function with try & except mechanism,
a bit excessive because catching error in the root of parsing function,
and slowing down performance in 2 functions.

The pros are could do simpler and didn't have to specify the pages.

def tabling(url, label, tingkat, jurusan, kelas, page=1, count=None):
    try:
        parsed = parsing(url, params(tingkat, jurusan, kelas, page))
        df = pd.DataFrame(columns=label).append(extract(label, parsed))
        return df.append(
            tabling(
                    url, label, tingkat, jurusan, kelas, page + 1),
                    ignore_index=True)
    except:
        return df
'''

if __name__ == '__main__':
    # Predefined target urls and data.
    url = ['https://baak.gunadarma.ac.id/cariMhsBaru/',
           'https://baak.gunadarma.ac.id/cariKelasBaru/']
    label = [['No', 'No Pend.', 'Nama', 'NPM', 'Kelas', 'Keterangan'],
             ['No', 'NPM', 'Nama', 'Kelas Lama', 'Kelas Baru']]
    tingkat = ['1', '2']
    jurusan = ['IA', 'SA', 'TB', 'EB', 'PA',
               'TA', 'MA', 'KA', 'IC', 'EA', 'ID', 'KB']
    data = dict()

    # Start extracting table from Predefined target.
    for tin in tingkat:
        xurl = url[tingkat.index(tin)]
        xlabel = label[tingkat.index(tin)]
        filename = 'Tingkat_' + tin

        if isfile(filename + '.msgpack'):
            data[tin] = pd.read_msgpack(filename + '.msgpack')
        else:
            df = pd.DataFrame(columns=xlabel)
            for jur in jurusan:
                try:
                    count = 0
                    while True:
                        count += 1
                        kel = ("%.2d" % count)
                        print('Processing [{}{}{}]'.format(tin, jur, kel))
                        df = df.append(tabling(
                            xurl, xlabel, tin, jur, kel), ignore_index=True)
                except:
                    pass

            # Exporting to msgpack.
            df = df.rename_axis('index', axis='columns')
            df.to_msgpack(filename + '.msgpack')

            # Exporting to excel.
            writer = pd.ExcelWriter(filename + '.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name=filename)
            worksheet = writer.sheets[filename]
            writer.save()

    # Find keyword contains in a column.
    searchName = 'a'
    searchCol = 'Nama'
    search = data[0][data[0][[searchCol].str.contains(searchName, case=False)]
