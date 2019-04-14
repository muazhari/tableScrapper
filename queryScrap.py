import pandas as pd
from tabulate import tabulate


class database:
    def __init__(self, files):
        self.file = files
        self.search = search(database=self)


class search(database):
    def __init__(self, database):
        self.database = database
        self.file = self.database.file

    def kelas(self, hari, jam, ruang, kelas, nama=None):
        hari = self.file['jadwalKelas'][self.file['jadwalKelas']['hari'].str.contains(
            hari, na=False, case=False)]
        jam = hari[hari['waktu'].str.contains(jam, na=False, case=False)]
        ruang = jam[jam['ruang'].str.contains(ruang, na=False, case=False)]
        kelas = ruang[ruang['kelas'].str.startswith(kelas.upper(), na=False)]
        result = kelas

        if nama:
            nama = self.file['siswa1'][self.file['siswa1']['nama'].str.contains(
                nama, na=False, case=False)]

            result = nama[nama['kelas'].isin(kelas['kelas'])]

        return tabulate(result.reset_index(drop=True), headers='keys', tablefmt='psql')

    def midTest(self, matkul, hari, tanggal, waktu, ruang, kelas):
        matkul = self.file['jadwalMidTest'][self.file['jadwalMidTest']['mata_kuliah'].str.contains(
            matkul, na=False, case=False)]
        hari = matkul[matkul['hari'].str.contains(hari, na=False, case=False)]
        tanggal = hari[hari['tanggal'].str.contains(
            tanggal, na=False, case=False)]
        waktu = tanggal[tanggal['waktu'].str.contains(
            waktu, na=False, case=False)]
        ruang = waktu[waktu['ruang'].str.contains(ruang, na=False, case=False)]
        kelas = ruang[ruang['kelas'].str.contains(kelas, na=False, case=False)]
        result = kelas

        return tabulate(result.reset_index(drop=True), headers='keys', tablefmt='psql')


# search('','','','1ia05')
