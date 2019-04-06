import pandas as pd
from tabulate import tabulate

class queryJ:
    def __init__(self, files):
        self.tingkat = files['kelas']
        self.jadwal = files['jadwal']
        self.siswa1 = files['siswa1']
        self.siswa2 = files['siswa2']

    def search(self, hari, jam, ruang, kelas):
        harid = self.jadwal[self.jadwal['hari'].str.contains(hari, na=False, case=False)]
        waktu = harid[harid['waktu'].str.contains(jam, na=False, case=False)]
        ruang = waktu[waktu['ruang'].str.contains(ruang, na=False, case=False)]
        kelas = ruang[ruang['kelas'].str.startswith(kelas.upper(), na=False)]
        return tabulate(kelas.reset_index(drop=True), headers='keys', tablefmt='psql')

# search('', '', '', '1ia05')
