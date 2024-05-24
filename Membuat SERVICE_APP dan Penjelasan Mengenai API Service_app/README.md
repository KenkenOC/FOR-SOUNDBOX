## Service
***!Pastikan Frappe Sudah Terinstall dan Sudah siap digunakan jika belum bisa kunjungi [Set Up Frappe](https://github.com/KenkenOC/FOR-SOUNDBOX/tree/main/Set%20Up%20Frappe)!***

### [1.0 Membuat App & Site baru untuk Service](#10-Membuat-App-&-Site-Baru-Untuk-Service)
- [**1.1 Membuat App & Site baru untuk Service**](#11-Membuat-App-&-Site-Baru-Untuk-Service)
- [**1.2 Install App ke Site**](#12-Install-App-ke-Site)
- [**1.3 Memastikan App sudah terinstall didalam Site**](#13-Memastikan-App-sudah-terinstall-didalam-Site)


### 2.0 Membuat Doctype Yang Diperlukan Untuk Service 
- **2.1 Masuk ke dalam Frappe UI**
- **2.2 Masuk ke dalam Page Build**
- **2.3 Click shortcut DocType**
- **2.4 Click add DocType**
- **2.5 Add new DocType**
- **2.6 Setup Table**
- **2.7 Menambahkan Role ke Doctype**

### 3.0 Membuka Vscode ke dalam Apps
- **3.1 Membuka Vscode ke dalam Apps**

### 4.0 Membuat File API Service

### 5.0 Penjelasan Mengenai File API Service_app 
- **5.1 Service**


### 1.0 Membuat App & Site baru untuk Service
#### 1.1 Membuat App & Site baru untuk Service**bench new-site nama_site 
    
1. Buat Site Baru

       bench new-site nama_site
   

    ini yang akan dilakukan oleh `bench`

        MySQL root password: 
        
        Installing frappe...
        Updating DocTypes for frappe        : [====================] 100%
        Set Administrator password: 
        Updating Dashboard for frappe
        tutorial1.test: SystemSettings.enable_scheduler is UNSET
        *** Scheduler is disabled ***
   
2. sesudah itu lakukan add to host 

       bench --site nama_site.test add-to-hosts

3. Buat App Baru 

       bench new-app nama_app

   ini yang akan diminta oleh `bench`
    
        App Title [Nama App]: Nama App
        App Description: Deskripsi app
        App Publisher: nyuuk
        App Email: nyuuk@email.com
        App License (agpl-3.0, apache-2.0, bsd-2-clause, bsd-3-clause, bsl-1.0, cc0-1.0, epl-2.0, gpl-2.0, gpl-3.0, lgpl-2.1, mit, mpl-2.0, unlicense) [mit]:
        Create GitHub Workflow action for unittests [y/N]:
        'test_app' created at /workspace/frappe-bench/apps/test_app


#### 1.2 Install App ke Site

1. install app ke site yang sudah dibuat tadi

       bench --site your_site.local install-app nama_app
   
   ganti `your_site.local` dengan site mu, dan `nama_app` dengan nama app yang tadi sudah di create. jawaban nya akan seperti ini

       Installing nama_app...
       Updating Dashboard for nama_app
   
#### 1.3 Memastikan App sudah terinstall didalam Site

Masuk ke UI/Dashboard Frappe, Click Help-> About.
> Di sini saya membuat app dengan *title service* dengan branch dev
![WhatsApp Image 2024-05-24 at 10 54 48 AM](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/063e3efd-3ad9-4573-a86e-56d4fb7d1f43)

Jika sudah begini berarti App `service` sudah terinstall di Site 

