# kelasScrap
> Pencarian kelas dengan sedikit advancement.
### Feature
- Only scraping and querying.

# Installation
```sh
$ pip install -r requirements.txt
```

# Usage
Pencarian kelas :
```
search.kelas('hari', 'jam', 'tempat/ruang', 'kelas')
```
Mencari kelas pada hari Senin sekitar jam ke-1 dan bertempat disekitar Kampus D.
Dimana hasil pencarian kelas yang ingin dicari 1IA05 ialah :
```
search.kelas('senin', '1', 'd', '1ia05')
```

Pencarian UTS :
```
search.midTest('matkul', 'hari', 'tanggal', 'waktu', 'ruang', 'kelas')
```
Mencari ujian mata kuliah Matematika Dasar yang dimana melekat pada kelas 1IA ialah :
```
search.midTest('matematika dasar', '', '', 'waktu', '', '1ia')
```

Hasil pencarian akan kosong apabila tidak ada yang match.
Kosongkan argumen menjadi ```''``` agar memproses semua record selabel tanpa dibandingkan.

Runtime depends on your hardware and connection.
```sh
$ python main.py
```

# Todos
- Manusia matcher.
- Mager mencari Dosen?
- Ruang KOSONG pegal kurang dikit.

# Authors
- Muhammad Kharisma Azhari - Initial work
