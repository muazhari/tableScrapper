import crawlSpiders
import queryScrap
import os
import pandas as pd


def main():
    spidersFiles = dict(spiderKelas='kelas.csv',
                        spiderJadwal='jadwalKelas.csv',
                        spiderMidTest='jadwalMidTest.csv',
                        spiderSiswa1='siswa1.csv',
                        spiderSiswa2='siswa2.csv')

    isFilesAvailable = all(os.path.isfile(file) for file in spidersFiles.values())

    if not(isFilesAvailable):
        spiders = list(spidersFiles.keys())
        crawlSpiders._crawl(spiders[0])
        crawlSpiders.run(spiders[1:])

    files = dict([(os.path.splitext(file)[0],
                   pd.read_csv(file)) for file in spidersFiles.values()])

    db = queryScrap.database(files)
    print(db.search.kelas('', '', '', '1ia05', ''))
    print(db.search.midTest('', '', '', '', '', '1ia05'))


if __name__ == '__main__':
    main()
