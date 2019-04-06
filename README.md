# kelasScrap
> Pencarian kelas dengan sedikit advancement.

### Feature
- Only scraping and querying.

Fungsi utama :
```
kelas.search('hari', 'jam', 'tempat/ruang', 'kelas')
```
Mencari kelas pada hari Senin sekitar jam 1 dan bertempat disekitar Kampus D.

Dimana hasil pencarian kelas yang ingin dicari adalah 1IA05. 
```
kelas.search('senin', '1', 'd', '1ia05')
```
Hasil pencarian akan kosong apabila tidak ada yang match.

Kosongkan argumen menjadi ```''``` untuk memproses semua record selabel tanpa dibandingkan.

### Usage
Speed of run depends on your hardware and connection.
```sh
$ python main.py
```

### Todos
- Manusia matcher.
- Mager mencari Dosen?
- Ruang KOSONG pegal kurang dikit.

