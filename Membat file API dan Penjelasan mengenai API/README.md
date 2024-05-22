
### 1.0 Membuat file untuk API

#### 1.1 Penjelasan mengenai FILE API DIATAS
- **1.2 Payment_APP**
- **1.3 API_AUTH**
- **1.4 API_PAYMENT**
- **1.5 API_PRODUCT**
- **1.6 API_STORE**
- **1.7 API_TRANSACTIONS**
- **1.8 MIDDLEWARE**
- **1.9 REPOSITORIES**
- **1.10 UTILS**
- **1.11 HOOKS.PY**


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

karna di sini saya sudah membuatnya maka bentuknya akan seperti ini di dalam folder `payment_app`


### 1.1 Penjelasan mengenai FILE API DIATAS

#### 1.2 Payment_APP
**Folder Payment_APP ini merupakan struktur yang digunakan untuk mengatur dan mengelompokkan semua file yang terkait dengan proses pembayaran dalam aplikasi. Dengan menggunakan struktur yang terorganisir ini, pengembang dapat dengan mudah menemukan dan mengelola semua file yang berkaitan dengan fungsionalitas pembayaran, mulai dari otentikasi pengguna hingga pengelolaan transaksi dan produk. Ini mempermudah dalam pengembangan, pemeliharaan, dan penyesuaian fitur-fitur pembayaran dalam aplikasi secara efisien dan terstruktur.**


#### 1.3 API_AUTH
di dalam api_auth ini ada 2 file python yaitu `login.py` & `register.py` mereka memiliki fungsi yang berbeda
     
* **login.py**: File ini berisi kode yang mengatur proses autentikasi pengguna saat login ke dalam sistem. Di dalamnya, terdapat 
fungsi-fungsi yang memvalidasi informasi masuk seperti email/telepon dan kata sandi, dan kemudian menghasilkan token otentikasi untuk digunakan dalam sesi pengguna.
     
* **register.py**: File ini mengurus proses pendaftaran pengguna baru ke dalam sistem. Di dalamnya, terdapat fungsi-fungsi yang memvalidasi informasi pendaftaran, seperti email dan kata sandi, dan kemudian menyimpan informasi pengguna baru ke dalam database.

#### 1.4 API_PAYMENT
di dalam api_payment ini terdapat satu file Python yang digunakan untuk payment `pay.py`

* **pay.py**:File ini mengatur proses pembayaran dalam aplikasi. Di dalamnya, terdapat fungsi-fungsi yang menangani transaksi pembayaran, memproses detail pembayaran, dan memastikan bahwa pembayaran dilakukan dengan aman dan benar.



