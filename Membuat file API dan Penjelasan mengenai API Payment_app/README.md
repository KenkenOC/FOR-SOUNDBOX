> [!CAUTION]
> Pastikan Frappe sudah terinstall jika belum bisa mengikuti tutorial berikut [Set Up Frappe](https://github.com/KenkenOC/FOR-SOUNDBOX/tree/main/Set%20Up%20Frappe).*


### [1.0 Membuat file untuk API](#10-membuat-file-untuk-api-1)

#### [1.1 Penjelasan mengenai FILE API DIATAS](#11-penjelasan-mengenai-file-api-diatas-1)
- [**1.2 Payment_APP**](#12-payment_app)
- [**1.3 API_AUTH**](#13-api_auth)
- [**1.4 API_PAYMENT**](#14-api_payment)
- [**1.5 API_PRODUCT**](#15-api_product)
- [**1.6 API_STORE**](#16-api_store)
- [**1.7 API_TRANSACTIONS**](#17-api_transactions)
- [**1.8 MIDDLEWARE**](#18-middleware)
- [**1.9 REPOSITORIES**](#19-repositories)
- [**1.10 UTILS**](#110-utils)
- [**1.11 HOOKS.PY**]()


#### 1.0 Membuat File untuk API 

     /workspace/frappe-bench/apps/payment_app/
    ├── license.txt
    ├── pyproject.toml
    ├── README.md
    └── payment_app
        ├── api_auth
        │   ├── login.py
        │   └── register.py
        ├── api_payment
        │   └── pay.py
        ├── api_product
        │   └── product.py
        ├── api_store
        │   └── store.py
        ├── api_transactions
        │   └── transactions.py
        ├── middleware
        │   ├── auth.py
        │   └── request_log.py
        ├── repositories
        │   ├── after_transactions.py
        │   ├── customer.py
        │   ├── pay.py
        │   ├── product.py
        │   └── store.py
        └── utils
            ├── generate_code.py
            └── response.py

karna di sini saya sudah membuatnya maka bentuknya akan seperti ini di dalam folder payment_app


### 1.1 Penjelasan mengenai FILE API DIATAS

#### 1.2 Payment_APP
Folder Payment_APP ini merupakan struktur yang digunakan untuk mengatur dan mengelompokkan semua file yang terkait dengan proses pembayaran dalam aplikasi. Dengan menggunakan struktur yang terorganisir ini, pengembang dapat dengan mudah menemukan dan mengelola semua file yang berkaitan dengan fungsionalitas pembayaran, mulai dari otentikasi pengguna hingga pengelolaan transaksi dan produk. Ini mempermudah dalam pengembangan, pemeliharaan, dan penyesuaian fitur-fitur pembayaran dalam aplikasi secara efisien dan terstruktur.


#### 1.3 API_AUTH
di dalam api_auth ini ada 2 file python yaitu login.py & register.py mereka memiliki fungsi yang berbeda
     
* `login.py`: File ini berisi kode yang mengatur proses autentikasi pengguna saat login ke dalam sistem. Di dalamnya, terdapat 
fungsi-fungsi yang memvalidasi informasi masuk seperti email/telepon dan kata sandi, dan kemudian menghasilkan token otentikasi untuk digunakan dalam sesi pengguna.
     
* `register.py`: File ini mengurus proses pendaftaran pengguna baru ke dalam sistem. Di dalamnya, terdapat fungsi-fungsi yang memvalidasi informasi pendaftaran, seperti email dan kata sandi, dan kemudian menyimpan informasi pengguna baru ke dalam database.

#### 1.4 API_PAYMENT
di dalam api_payment ini terdapat satu file Python yang digunakan untuk payment pay.py

* `pay.py`: File ini mengatur proses pembayaran dalam aplikasi. Di dalamnya, terdapat fungsi-fungsi yang menangani transaksi pembayaran, memproses detail pembayaran, dan memastikan bahwa pembayaran dilakukan dengan aman dan benar.

#### 1.5 API_PRODUCT
* `product.py`: File ini mengelola informasi produk dalam aplikasi. Fungsi-fungsi di dalamnya menangani pembuatan, pembaruan, penghapusan, dan pengambilan data produk dari database.


#### 1.6 API_STORE 
* `store.py`: File ini mengatur informasi toko dalam aplikasi. Terdapat fungsi-fungsi yang mengelola data toko seperti menambahkan toko baru, memperbarui informasi toko, dan menghapus toko dari sistem.


#### 1.7 API_TRANSACTIONS
* `transactions.py`: File ini menangani pengelolaan transaksi dalam aplikasi. Di dalamnya terdapat fungsi-fungsi untuk mencatat transaksi, mengambil riwayat transaksi, dan melakukan pembatalan atau pengembalian transaksi jika diperlukan.


#### 1.8 MIDDLEWARE
* `auth.py`: File ini berisi middleware untuk mengatur otorisasi dan autentikasi pengguna dalam setiap permintaan yang masuk ke sistem.

* `request_log.py`: File ini berisi middleware yang mencatat setiap permintaan yang masuk ke sistem untuk tujuan monitoring dan debugging.


#### 1.9 REPOSITORIES
* `after_transactions.py`: File ini mengelola operasi yang harus dilakukan setelah transaksi selesai, seperti pembaruan status atau pengiriman notifikasi.

* `customer.py`: File ini menangani data pelanggan, termasuk pembuatan, pembaruan, dan penghapusan data pelanggan.

* `pay.py`: File ini berhubungan dengan data pembayaran dan mencatat detail setiap transaksi pembayaran.

* `product.py`: File ini berhubungan dengan data produk, mengelola informasi produk dalam database.

* `store.py`: File ini berhubungan dengan data toko, mengelola informasi terkait toko dalam aplikasi.

#### 1.10 UTILS
* `generate_code.py`: File ini berisi fungsi-fungsi utilitas untuk menghasilkan kode unik yang digunakan dalam berbagai proses dalam aplikasi.

* `response.py`: File ini berisi fungsi-fungsi utilitas untuk membentuk respons yang konsisten dalam API, seperti format standar untuk pesan sukses atau pesan error.
