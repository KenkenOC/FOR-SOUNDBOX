# FOR-SOUNDBOX

# API Documentation

## Introduction
This is the documentation for PAYMENT & SERVICE SOUNDBOX.

# List Docs

### List Docs API Payment & Service  

#### 1.0 Set Up Frappe Dahulu 
- [**1.1 Buat Site Baru**](#11-Buat-Site-Baru)
- [**1.2 Install App baru**](#12-Install-App-baru)
- **1.3 Install APP ke Site**
- **1.4 Pastikan app sudah terinstall di site**

#### 2.0 Membuat Doctype di Frappe 
- **2.1 Masuk ke dalam Frappe UI**
- **2.2 Masuk ke dalam Page Build**
- **2.3 Click shortcut DocType**
- **2.4 Click add DocType**
- **2.5 Add new DocType**
- **2.6 Setup Table**
- **2.7 Menambahkan Role ke Doctype**

#### 3.0 Membuka VS-Code ke dalam apps
- **3.1 Masuk ke directory frappe-bench atau init name kamu, setelah itu buka dir apps, dan buka dir app kamu**
- **3.2 Membuka VS-Code**

#### 4.0 Membuat file untuk API

- **4.1 Penjelasan mengenai FILE API DIATAS**
    - **4.2 Payment_APP**
        - **4.3 api_auth**

           API Auth ini didalamanya terdapat dua file Python `login.py`&`register.py`
          
          | No | Nama Definisi | Deskripsi |
          |----|---------------|-----------|
          |    |               |           |

        - **4.4 api_payment**:

          API Payment ini berisi suatu code yang digunakan ketika melakuakn pmebayaran yang akan ngehit dan mengisi ke doctype Transaction Callback, Webhook Logs 
          | Nama Definisi              | Deskripsi                                                                                |
          |-----------------------|------------------------------------------------------------------------------------------|
          | Transaction Callback  | Digunakan untuk menangani callback dari transaksi yang telah dilakukan                    |
          | Webhook Logs          | Merekam log terkait webhook yang dipicu oleh aktivitas pembayaran                          |
          | update_status         | Fungsi untuk memperbarui status transaksi menjadi Success!                               |
          | hit_fetch_api_service | Fungsi untuk memicu Soundbox ketika pembayaran dilakukan                                  |
        - **4.5 api_product**
        - **4.6 api_store**
        - **4.7 api_transactions**
        - **4.8 middleware**
        - **4.9 Repositories**
        - **4.10 utils**
        - **4.11 hooks.py**

## 1.0 Set Up Frappe Dahulu
### 1.1 Buat Site Baru 

    bench new-site nama_site #tidak boleh ada spasi
