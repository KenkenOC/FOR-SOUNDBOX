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
![About](https://private-user-images.githubusercontent.com/76798963/314235901-6f13de67-95c5-428a-9f4c-f790b398da8e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYzNjM3NjksIm5iZiI6MTcxNjM2MzQ2OSwicGF0aCI6Ii83Njc5ODk2My8zMTQyMzU5MDEtNmYxM2RlNjctOTVjNS00MjhhLTlmNGMtZjc5MGIzOThkYThlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTIyVDA3Mzc0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTZiNjgxNjY4MWI2MjBkMjkzY2RiZTBhMTBkZWMxZTEyMzg0OWVhYTRlMDlmOTU3NzMxOTRiNWJlNGZjMWQ0ZjgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.tUARfQnwMUI1XpLKijBF6FpjG6rdVb06TtJR6D0g9qY)

Jika sudah begini berarti App sudah terinstall di Site 


#### 2.0 Membuat Doctype di Frappe

### 2.1 Masuk ke dalam Frappe UI
Biasanya URL nya adalah: `http://site_kamu.local:8000` [http://site_kamu.local:8000](http://site_kamu.local:8000)

### 2.2 Masuk ke dalam Page Build
![PAGE](https://private-user-images.githubusercontent.com/76798963/314231898-ead1fb19-d2b6-4be8-b15a-f43821ea2c37.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYzNjM3NjksIm5iZiI6MTcxNjM2MzQ2OSwicGF0aCI6Ii83Njc5ODk2My8zMTQyMzE4OTgtZWFkMWZiMTktZDJiNi00YmU4LWIxNWEtZjQzODIxZWEyYzM3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTIyVDA3Mzc0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRiZjA2ZGY3ZDdkYjUyNTI2M2I5YzljMTFmOTAwY2E2ZjliODliYzU3MTFlNjk2ZGRmNzZkZWYxMThlMjA4YTQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.QsYySlMtonVVWxtnigteXriUvphXzzA_a7zl53xl_Ps)

### 2.3 Click shortcut DocType
![shortcut](https://private-user-images.githubusercontent.com/76798963/314232069-ae59597d-e7cf-4dd6-ab23-0c9d3c0908d3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYzNjM3NjksIm5iZiI6MTcxNjM2MzQ2OSwicGF0aCI6Ii83Njc5ODk2My8zMTQyMzIwNjktYWU1OTU5N2QtZTdjZi00ZGQ2LWFiMjMtMGM5ZDNjMDkwOGQzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTIyVDA3Mzc0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTllNDg3ODYyYTZmMjkwZjM0NjBhZDE4ZWFhZWU2MDMzMWI2OTM0MzgxNWQ0ZjdiZWI1ODRiNGYzNjE5NjQ1N2UmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.3Jtu3sOWj7B0WbhvcpgpEz_L2144MrK-AZjddlJYJ9E)

### 2.4 Click add DocType
![click](https://private-user-images.githubusercontent.com/76798963/314232200-59c816f0-e803-4112-8817-b628ffe94a65.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYzNjM3NjksIm5iZiI6MTcxNjM2MzQ2OSwicGF0aCI6Ii83Njc5ODk2My8zMTQyMzIyMDAtNTljODE2ZjAtZTgwMy00MTEyLTg4MTctYjYyOGZmZTk0YTY1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTIyVDA3Mzc0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZhMDk5MTM5ZGY2N2RkY2QzYWYwMzQzNzBhOWE2MGJhMjJlOGZhNDA0N2U1ZTQyZTZlYmE2MGIyM2M5YWI1ZjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.gUePjfhaLrrQuyccnGy78dJKvlX36dVuuBZ3S2NqnYY)


### 2.5 Add new DocType
![new](https://private-user-images.githubusercontent.com/76798963/314237266-89cb531c-37ec-423f-8993-3ccfec74c0c6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTYzNjM3NjksIm5iZiI6MTcxNjM2MzQ2OSwicGF0aCI6Ii83Njc5ODk2My8zMTQyMzcyNjYtODljYjUzMWMtMzdlYy00MjNmLTg5OTMtM2NjZmVjNzRjMGM2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MjIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTIyVDA3Mzc0OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ4ZWYyNWRlYmVlODg4ODhjMWU1M2U0MTI4NmRmNzE5YmI1Y2E0YTQ3MjYxZWEzMzEzODNjYzYwNDJmOWY0ZDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.b2k2g_ccoYfVWs3T6apGBI1zhAHfxxJmLTY1ZZVemH8)

| Name           | Keterangan                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------|
| Doctype Name   | Diisi sembarang sesuai dengan nama yang diinginkan dari doctype tersebut.                     |
| Module         | Title dari aplikasi kalian.                                                                   |

Jika sudah click Create & Continue.

### 2.6 Setup Table
![setup](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890016232.png)

Add a new section > Add field > Data

![newsection](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890224623.png)


Save


### 2.7 Menambahkan Role ke Doctype 

![role](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890467421.png)

Permission Rules > Add Row


![role](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890503608.png)


![role](https://github.com/Akiyaaaaaa/frappe/wiki/image/Build-Custom-Rest-HTTP-API/1710890535525.png)

Save

