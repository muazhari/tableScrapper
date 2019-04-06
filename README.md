# kelasScrap
> Pencarian kelas dengan sedikit advancement.
### Feature
- Only scraping and querying.

# Installation
```sh
$ pip install -r requirements.txt
```

# Usage
Menggunakan Fungsi utama :
```
kelas.search('hari', 'jam', 'tempat/ruang', 'kelas')
```
Mencari kelas pada hari Senin sekitar jam 1 dan bertempat disekitar Kampus D. 
Dimana hasil pencarian kelas yang ingin dicari 1IA05 ialah :
```
kelas.search('senin', '1', 'd', '1ia05')
```
Hasil pencarian akan kosong apabila tidak ada yang match.
Kosongkan argumen menjadi ```''``` agar memproses semua record selabel tanpa dibandingkan.

Speed of run depends on your hardware and connection.
```sh
$ python main.py
```

# Todos
- Manusia matcher.
- Mager mencari Dosen?
- Ruang KOSONG pegal kurang dikit.

# Authors
- Muhammad Kharisma Azhari - Initial work

