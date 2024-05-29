# List Docs

### List Docs API Payment & Service  

### [1.0 Set Up Frappe Dahulu](#10-set-up-frappe-dahulu-1)
- [**1.1 Buat Site Baru**](#11-Buat-Site-Baru)
- [**1.2 Install App baru**](#12-Install-App-baru)
- [**1.3 Install APP ke Site**](#13-install-app-ke-site)
- [**1.4 Pastikan app sudah terinstall di site**](#14-pastikan-app-sudah-terinstall-di-site)

### [2.0 Membuat Doctype di Frappe](#20-membuat-doctype-di-frappe-1)
- [**2.1 Masuk ke dalam Frappe UI**](#21-masuk-ke-dalam-frappe-ui)
- [**2.2 Masuk ke dalam Page Build**](#22-masuk-ke-dalam-page-build)
- [**2.3 Click shortcut DocType**](#23-click-shortcut-doctype)
- [**2.4 Click add DocType**](#24-click-add-doctype)
- [**2.5 Add new DocType**](#25-add-new-doctype)
- [**2.6 Setup Table**](#26-setup-table)
- [**2.7 Menambahkan Role ke Doctype**](#27-menambahkan-role-ke-doctype)


## 1.0 Set Up Frappe Dahulu
### 1.1 Buat Site Baru 

1. install dan set-up `frappe-bench` dengan mengikuti [Tutorial](https://frappeframework.com/docs/user/en/installation)
   
2. Start the server by running `bench start`

3. buat site baru
   
        bench new-site nama_site 
   
    ini yang akan dilakukan oleh `bench`

        MySQL root password: 
        
        Installing frappe...
        Updating DocTypes for frappe        : [====================] 100%
        Set Administrator password: 
        Updating Dashboard for frappe
        tutorial1.test: SystemSettings.enable_scheduler is UNSET
        *** Scheduler is disabled ***
    
4. sesudah itu lakukan add to host 

        bench --site tutorial1.test add-to-hosts
    
### 1.2 Install App baru
1. Install app
   
       bench new-app nama_app
       
    ini yang akan diminta oleh `bench`
    
        App Title [Nama App]: Nama App
        App Description: Deskripsi app
        App Publisher: nyuuk
        App Email: nyuuk@email.com
        App License (agpl-3.0, apache-2.0, bsd-2-clause, bsd-3-clause, bsl-1.0, cc0-1.0, epl-2.0, gpl-2.0, gpl-3.0, lgpl-2.1, mit, mpl-2.0, unlicense) [mit]:
        Create GitHub Workflow action for unittests [y/N]:
        'test_app' created at /workspace/frappe-bench/apps/test_app
        
### 1.3 Install App ke Site
1. install app ke site yang sudah dibuat tadi

       bench --site your_site.local install-app nama_app
   
   ganti `your_site.local` dengan site mu, dan `nama_app` dengan nama app yang tadi sudah di create. jawaban nya akan seperti ini

       Installing nama_app...
       Updating Dashboard for nama_app

### 1.4 Pastikan app sudah terinstall di site

Masuk ke UI/Dashboard Frappe, Click Help-> About.
> Di sini saya membuat app dengan *title Tutorial App* dengan branch dev
![image](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/f6984551-061d-4fd8-bfaa-c5cda1161a02)

Jika sudah begini berarti App sudah terinstall di Site 



#### 2.0 Membuat Doctype di Frappe

### 2.1 Masuk ke dalam Frappe UI
Biasanya URL nya adalah: `http://site_kamu.local:8000` [http://site_kamu.local:8000](http://site_kamu.local:8000)

### 2.2 Masuk ke dalam Page Build
![image](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/081cb1e0-ed45-46e2-b931-260f6acf3124)


### 2.3 Click shortcut DocType
![image](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/985cc9a1-2649-4d9f-bc9b-d622adffdd17)


### 2.4 Click add DocType
![image](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/f33ad04b-fbf1-4be2-841c-71694664c37a)


### 2.5 Add new DocType
![image](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/665e8a95-912e-4d23-be75-9eaa9f07718b)



| Name           | Keterangan                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------|
| Doctype Name   | Diisi sembarang sesuai dengan nama yang diinginkan dari doctype tersebut.                     |
| Module         | Title dari aplikasi kalian.                                                                   |

Jika sudah click Create & Continue.

### 2.6 Setup Table
![image](https://github.com/KenkenOC/FOR-SOUNDBOX/assets/161264420/c3266f73-d205-46fc-bb68-29b32e49be5e)


Add a new section > Add field > Data

![newsection](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890224623.png)


Save


### 2.7 Menambahkan Role ke Doctype 

![role](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890467421.png)

Permission Rules > Add Row

![role](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890535525.png)

Save


