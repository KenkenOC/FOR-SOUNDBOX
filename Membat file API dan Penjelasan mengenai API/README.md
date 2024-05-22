
### 4.0 Membuat file untuk API

#### 4.1 Penjelasan mengenai FILE API DIATAS
**4.1 Payment_APP**
- **4.1.1 API_AUTH**
- **4.1.2 API_PAYMENT**
- **4.1.3 API_PRODUCT**
- **4.1.4 API_STORE**
- **4.1.5 API_TRANSACTIONS**
- **4.1.6 MIDDLEWARE**
- **4.1.7 REPOSITORIES**
- **4.1.8 UTILS**
- **4.1.9 HOOKS.PY**


#### 4.0 Membuat File untuk API 

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



#### 4.1 Penjelasan mengenai FILE API DIATAS

### 4.1 Payment_APP
**Folder Payment_APP ini merupakan struktur yang digunakan untuk mengatur dan mengelompokkan semua file yang terkait dengan proses pembayaran dalam aplikasi. Dengan menggunakan struktur yang terorganisir ini, pengembang dapat dengan mudah menemukan dan mengelola semua file yang berkaitan dengan fungsionalitas pembayaran, mulai dari otentikasi pengguna hingga pengelolaan transaksi dan produk. Ini mempermudah dalam pengembangan, pemeliharaan, dan penyesuaian fitur-fitur pembayaran dalam aplikasi secara efisien dan terstruktur.**


#### 4.1.1 API_AUTH
di dalam api_auth ini ada 2 file python yaitu `login.py` & `register.py` mereka memiliki fungsi yang berbeda
