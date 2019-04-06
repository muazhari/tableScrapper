import crawlSpiders
import queryJ
import os
import pandas as pd

def main():
    spiders = ['spiderKelas', 'spiderJadwal', 'spiderSiswa1', 'spiderSiswa2']
    reqFiles = ['kelas.csv', 'jadwal.csv', 'siswa1.csv', 'siswa2.csv']

    if not(all(os.path.isfile(file) for file in reqFiles)):
        crawlSpiders._crawl(spiders[0])
        crawlSpiders.run(spiders[1:])

    files = dict(
                    kelas = pd.read_csv("kelas.csv"),
                    jadwal = pd.read_csv("jadwal.csv"),
                    siswa1 = pd.read_csv("siswa1.csv"),
                    siswa2 = pd.read_csv("siswa2.csv"),
                )

    kelas = queryJ.queryJ(files)
    '''
    kelas.search('hari', 'jam', 'tempat/ruang', 'kelas')

    Contoh penggunaan fungsi yaitu kelas.search('senin', '1', 'd', '1ia05').

    Yang artinya mencari kelas pada hari Senin sekitar jam 1 dan bertempat disekitar Kampus D. Dimana hasil pencarian kelas ingin dicari adalah 1ia05.

    Hasil pencarian akan kosong apabila tidak ada yang match.

    Atau kosongkan argumen menjadi '' untuk mengeluarkan kondisi.
    (memproses semua record selabel tanpa dibandingkan)
    '''
    print(kelas.search('', '', '', '1ia05'))

if __name__ == '__main__':
    main()
