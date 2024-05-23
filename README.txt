1. akses folder project melalui terminal dengan menggunakan cd #path-folder-project
   contoh jika anda menaruh folder aplikasi ini di desktop maka input statment berikut di terminal: 
   cd .\Desktop\tensorflow-fastapi-starter-pack\
2. aktifkan virtual environtment python yang terdapat pada folder project dengan menginput statement berikut:
   venv\Scripts\activate
3. pastikan virtual envorinment telah aktif dengan melihat adanya tulisan (venv) pada prompt terminal
4. install semua packages python yang diperlukan untuk menjalankan aplikasi dengan menginput statement berikut di terminal:
   pip install -r requirements.txt
5. pastikan semua packages yang dibutuhkan sudah di install dengan benar, dari tidak adanya pesan error yang muncul saat proses instalasi
   jika terjadi error maka coba kembali langkah 4, dan pastikan file requirements.txt ada di folder project
6. aktifkan uvicorn melalui terminal dengan menginputkan statement berikut di terminal
   uvicorn application.server.main:app 
7. pergi ke alamat halaman web yang muncul sebagai output pada terminal, kemudian tambahkan "/dashboard", contohnya:
   http://127.0.0.1:8000/dashboard
8. selamat anda berhasil mengakses aplikasi tersebut.
   