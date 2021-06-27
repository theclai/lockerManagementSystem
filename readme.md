# Locker Management System

Locker Management System adalah program untuk manajemen loker berbasic command line

## Instalasi
install python 3.8.0
Buat python environment baru dan load env

```bash
python3 -m venv <nama_environment>
source <name_environtment>/bin/activate
```

Gunakan manajement paket [pip](https://pip.pypa.io/en/stable/) untuk menginstall library unittest

```bash
pip install -r requirements.txt
```

## Menjalankan Unit Test
1. Basic Test

```bash
python -m unittest test.py -v
```
2. Coverage
```bash
coverage run test.py
coverage report
coverage html #generate menjadi file html
```

## Menjalankan Locker Management System
```bash
python main.py
```
## Perintah yang Tersedia
1. init
2. status
3. exit
4. find
5. search
6. leave
7. input