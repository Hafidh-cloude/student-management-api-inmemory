# Student Management API

REST API sederhana untuk mengelola data mahasiswa menggunakan FastAPI dengan in-memory storage.

## Fitur

- Menambahkan data mahasiswa
- Menampilkan seluruh data mahasiswa
- Menampilkan data mahasiswa berdasarkan ID
- Memperbarui data mahasiswa
- Menghapus data mahasiswa
- Validasi input menggunakan Pydantic
- Interactive API documentation menggunakan Swagger UI

## Teknologi

- Python
- FastAPI
- Pydantic
- Uvicorn

## Storage

Data mahasiswa disimpan menggunakan **in-memory storage (Python list)**.

Data akan kembali kosong ketika aplikasi di-restart atau di-deploy ulang.

## Struktur Project

```text
student-management-api-inmemory/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── students.py
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## Instalasi

Clone repository:
```text
git clone https://github.com/Hafidh-cloude/student-management-api-inmemory.git
cd student-management-api-inmemory
```

## Install dependencies:
```text
uv sync
```
## Jalankan aplikasi:
```text
uv run fastapi dev app/main.py
```
## API akan berjalan di:
```text
http://127.0.0.1:8000
```
## Deployment

Aplikasi telah di-deploy menggunakan FastAPI Cloud.

**API Documentation:**  
https://student-management-api-0822cc2d.fastapicloud.dev/docs

Gunakan Swagger UI untuk mencoba seluruh API secara interaktif.
## API Endpoints
Method	Endpoint	Deskripsi:
```text
GET	/students/	Menampilkan seluruh mahasiswa
POST	/students/	Menambahkan mahasiswa
GET	/students/{id}	Menampilkan mahasiswa berdasarkan ID
PUT	/students/{id}	Memperbarui data mahasiswa
DELETE	/students/{id}	Menghapus data mahasiswa
```
### Contoh
Menambahkan Mahasiswa
```text
POST /students/
```
Request:
```text
{
  "name": "Hafidh",
  "major": "Informatics",
  "semester": 8
}
```
Response:
```text
{
  "id": 1,
  "name": "Hafidh",
  "major": "Informatics",
  "semester": 8
}
```
