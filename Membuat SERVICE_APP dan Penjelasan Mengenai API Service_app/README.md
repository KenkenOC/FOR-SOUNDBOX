## Service

**Catatan:** *Pastikan Frappe sudah terinstal dan siap digunakan. Jika belum, silakan kunjungi panduan kami di [Set Up Frappe](https://github.com/KenkenOC/FOR-SOUNDBOX/tree/main/Set%20Up%20Frappe).*

### [1.0 Membuat Aplikasi & Situs Baru untuk Service](#10-Membuat-Aplikasi-&-Situs-Baru-Untuk-Service)
- [**1.1 Membuat Aplikasi & Situs Baru untuk Service**](#11-Membuat-Aplikasi-&-Situs-Baru-Untuk-Service)
- [**1.2 Menginstal Aplikasi ke Situs**](#12-Menginstal-Aplikasi-ke-Situs)
- [**1.3 Memastikan Aplikasi Terinstal di Situs**](#13-Memastikan-Aplikasi-Terinstal-di-Situs)

### [2.0 Membuat DocType yang Diperlukan untuk Service](#20-Membuat-DocType-yang-Diperlukan-untuk-Service)
- [**2.1 Membuat DocType**](#21-Membuat-DocType)

### [3.0 Membuka VS Code di Dalam Aplikasi](#30-Membuka-VS-Code-di-Dalam-Aplikasi)
- [**3.1 Membuka VS Code di Dalam Aplikasi**](#31-Membuka-VS-Code-di-Dalam-Aplikasi)

### [4.0 Membuat File API Service](#40-Membuat-File-API-Service)

### [5.0 Penjelasan Mengenai File API Service_app](#50-Penjelasan-Mengenai-File-API-Service_app)

- **5.1 Service**

---

### 1.0 Membuat Aplikasi & Situs Baru untuk Service

#### 1.1 Membuat Aplikasi & Situs Baru untuk Service

1. Membuat Situs Baru

       bench new-site nama_situs

    `bench` akan melakukan hal-hal berikut:

        MySQL root password: 
        Installing frappe...
        Updating DocTypes for frappe        : [====================] 100%
        Set Administrator password: 
        Updating Dashboard for frappe
        tutorial1.test: SystemSettings.enable_scheduler is UNSET
        *** Scheduler is disabled ***

2. Menambahkan situs ke hosts

       bench --site nama_situs.test add-to-hosts

3. Membuat Aplikasi Baru

       bench new-app nama_aplikasi

    `bench` akan meminta informasi berikut:

        App Title [Nama Aplikasi]: Nama Aplikasi
        App Description: Deskripsi aplikasi
        App Publisher: Nama penerbit
        App Email: penerbit@example.com
        App License (agpl-3.0, apache-2.0, bsd-2-clause, bsd-3-clause, bsl-1.0, cc0-1.0, epl-2.0, gpl-2.0, gpl-3.0, lgpl-2.1, mit, mpl-2.0, unlicense) [mit]:
        Create GitHub Workflow action for unittests [y/N]:
        'test_app' created at /workspace/frappe-bench/apps/test_app

#### 1.2 Menginstal Aplikasi ke Situs

1. Menginstal aplikasi ke situs yang sudah dibuat

       bench --site your_site.local install-app nama_aplikasi

    Ganti `your_site.local` dengan nama situs Anda, dan `nama_aplikasi` dengan nama aplikasi yang Anda buat. Outputnya akan seperti ini:

       Installing nama_aplikasi...
       Updating Dashboard for nama_aplikasi

#### 1.3 Memastikan Aplikasi Terinstal di Situs

Masuk ke UI/Dashboard Frappe, klik Help -> About.
> Di sini, saya membuat aplikasi dengan judul *service* di cabang dev.
![Konfirmasi Instalasi Aplikasi](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/063e3efd-3ad9-4573-a86e-56d4fb7d1f43)

Jika tampilannya seperti ini, berarti aplikasi `service` sudah terinstal di situs.

---

### 2.0 Membuat DocType yang Diperlukan untuk Service

#### 2.1 Membuat DocType
Untuk panduan membuat DocType, silakan lihat di [Set Up Frappe](https://github.com/KenkenOC/FOR-SOUNDBOX/tree/main/Set%20Up%20Frappe).

### 3.0 Membuka VS Code di Dalam Aplikasi
#### 3.1 Membuka VS Code di Dalam Aplikasi
Untuk panduan membuka Vscode di dalam Aplikasi, silahkan lihat di [Membuka Vscode ke dalam Apps](https://github.com/KenkenOC/FOR-SOUNDBOX/tree/main/Membuka%20Vscode%20ke%20dalam%20Apps)

### 4.0 Membuat File API Service
       
       /workspace/frappe-bench/apps/service_app/
       ├── license.txt
       ├── pyproject.toml
       ├── README.md
       ├── service
       │ ├── pycache
       │ ├── init.py
       │ └── service.py
       ├── config
       ├── public
       ├── templates
       └── www

### 5.0 Penjelasan Mengenai File API Service_app
#### 5.1 Service 
**Catatan:** *Untuk melihat Code dari service.py, silakan lihat di [service_app](https://github.com/KenkenOC/FOR-SOUNDBOX/tree/main/service_app/service_app/service).*

Di dalam File `Service.py` ada beberapa Def yang memiliki fungsi fungsi yang berbeda 

- def `get_token()`
  
  Fungsi ini bertanggung jawab untuk menghasilkan token yang diperlukan untuk otentikasi saat melakukan permintaan ke API           eksternal. Token dihasilkan dengan menggunakan informasi seperti appId, timestamp, requestId, dan userCode, yang dikombinasikan   dengan app_secret dan dienkripsi menggunakan algoritma MD5. Token yang dihasilkan kemudian dikirimkan kembali untuk digunakan
  dalam permintaan API.

- def `fetch_api()`

  Fungsi ini melakukan permintaan ke API eksternal untuk mendapatkan data berdasarkan parameter yang diberikan. Sebelum melakukan   permintaan, fungsi get_token() dipanggil untuk menghasilkan token yang valid. Setelah token diperoleh, fungsi membua
  permintaan GET ke URL API tertentu dengan menyertakan token dan parameter lain yang diperlukan. Jika permintaan berhasil, data
  yang diterima dari API akan disimpan dan dikembalikan dalam bentuk JSON.

- def `receive_params()`

  Fungsi ini bertanggung jawab untuk menerima parameter dari suatu permintaan dan memprosesnya. Pertama, fungsi fetch_api()
  dipanggil untuk mengambil data dari API eksternal berdasarkan parameter yang diberikan. Kemudian, parameter-parameter tersebut
  digunakan untuk membuat dokumen baru di dalam doctype "Transactions". Dokumen baru tersebut kemudian disimpan ke dalam database.
  Selain itu, fungsi juga mencatat log transaksi baru dan log permintaan baru. Jika terjadi kesalahan selama proses, fungsi akan
  menangani kesalahan tersebut dan mengembalikan pesan kesalahan.

- def `new_transaction_logs()`

  Fungsi ini digunakan untuk membuat log transaksi baru. Ketika sebuah transaksi dilakukan, fungsi ini membuat payload yang
  berisi informasi transaksi, seperti referensi transaksi, nama toko, nama pelanggan, produk yang dibeli, jumlah, harga total,
  dan status transaksi. Informasi ini kemudian digunakan untuk membuat dokumen baru di dalam doctype "Transaction Logs" dan
  disimpan ke dalam database. Jika proses pembuatan log transaksi baru berhasil, fungsi akan mengembalikan pesan sukses.

- def `new_request_logs()`

  Fungsi ini bertanggung jawab untuk mencatat log permintaan baru. Ketika sebuah permintaan diterima, fungsi ini mencatat
  informasi seperti URL permintaan, alamat IP pengirim permintaan, dan payload permintaan. Informasi ini kemudian digunakan untuk
  membuat dokumen baru di dalam doctype "Request Logs" dan disimpan ke dalam database. Jika proses pencatatan log permintaan
  berhasil, fungsi akan mengembalikan pesan sukses.
  
Ini adalah penjelasan dari fungsi-fungsi yang ada dalam file `service.py`. Semoga penjelasan ini membantu memahami fungsionalitas dan proses yang dilakukan oleh setiap fungsi.
