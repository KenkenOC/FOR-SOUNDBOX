## Service

**Catatan:** *Pastikan Frappe sudah terinstal dan siap digunakan. Jika belum, silakan kunjungi panduan kami di [Set Up Frappe](https://github.com/KenkenOC/FOR-SOUNDBOX/tree/main/Set%20Up%20Frappe).*

### [1.0 Membuat Aplikasi & Situs Baru untuk Service](#10-Membuat-Aplikasi-&-Situs-Baru-Untuk-Service)
- [**1.1 Membuat Aplikasi & Situs Baru untuk Service**](#11-Membuat-Aplikasi-&-Situs-Baru-Untuk-Service)
- [**1.2 Menginstal Aplikasi ke Situs**](#12-Menginstal-Aplikasi-ke-Situs)
- [**1.3 Memastikan Aplikasi Terinstal di Situs**](#13-Memastikan-Aplikasi-Terinstal-di-Situs)

### 2.0 Membuat DocType yang Diperlukan untuk Service
- **2.1 Membuat DocType**

### 3.0 Membuka VS Code di Dalam Aplikasi
- **3.1 Membuka VS Code di Dalam Aplikasi**

### 4.0 Membuat File API Service

### 5.0 Penjelasan Mengenai File API Service_app
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
