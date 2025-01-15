# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech - mdavap

## Business Understanding

Jaya Jaya Maju adalah sebuah perusahaan multinasional yang telah beroperasi selama lebih dari dua dekade sejak pendiriannya pada tahun 2000. Dalam perjalanannya, perusahaan ini telah berkembang menjadi organisasi yang cukup besar dengan lebih dari 1000 karyawan yang tersebar di berbagai wilayah di seluruh negeri. Meskipun pertumbuhan bisnisnya terbilang positif, perusahaan ini masih menghadapi tantangan signifikan dalam pengelolaan sumber daya manusia.


Salah satu indikator yang menunjukkan adanya masalah dalam manajemen SDM adalah tingginya tingkat attrition rate yang mencapai lebih dari 10%. Angka ini mengindikasikan bahwa perusahaan kehilangan sejumlah besar karyawan secara reguler, yang dapat berdampak negatif pada berbagai aspek operasional. Tingginya tingkat pergantian karyawan ini berpotensi meningkatkan biaya rekrutmen dan pelatihan, menurunkan produktivitas, serta berisiko kehilangan pengetahuan dan pengalaman berharga dari karyawan yang meninggalkan perusahaan.

Dengan begitu, pada proyek ini akan membuat sebuah dashboard untuk membantu departemen HR serta model Machine Learning agar bisa mempredikisi suatu karyawan akan attrition atau tidak.

### Permasalahan Bisnis

Permasalahan pada Jaya Jaya Maju adalah memiliki tingkat attrition rate yang mencapai lebih dari 10% oleh karena itu dengan membuat suatu dashboard untuk memonitor karyawan-karyawan serta sebuah model machine learning akan mengurangi attrition rate.

### Cakupan Proyek

Cakupan proyek yang akan dikerjakan disini adalah pengembangan suatu dashboard serta pembuatan model machine learning untuk memprediksi karyawan yang mungkin akan meninggalkan perusahaan.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:

```
conda create -n sbm_meta python=3.10
conda activate sbm_meta
pip install -r requirements.txt
```

Running notebook
```
jupyter .
```

## Machine Learning

### Data Preparation
- Dataset yang digunakan memiliki 35 kolom dan total data 1470.
- Dataset ini memiliki data kosong pada kolom `Attrition` maka kita akan mengisi data kosong dengan angka 0.
- Selanjutnya, melakukan encoding pada kolom yang bukan berisi angka seperti `BusinessTravel Department, EducationField, Gender, JobRole, MaritalStatus, Over18, OverTime`.
- Dan yang terakhir membagi dataset sebesar 20% untuk data uji dan 80% untuk data latih.

### Modeling
- DecisionTreeClassifier dan menggunakan default parameternya.
- RandomForestClassifier dengan menambahkan parameter `n_estimators` yaitu 50.
- LinearSVC dengan menggunakan default parameter juga.

### Evaluation
Evaluasi disini akan menggunakan metrik Accuracy, Recall, Precision dan Confusion Matrix.

- Decision Tree
    - Kelebihan:
        - Memiliki recall tertinggi (0.394) dibanding model lain, artinya paling baik dalam mengidentifikasi true positive
        - Seimbang antara precision dan recall dibanding model lain
        - Menghasilkan true positive dan true negative yang cukup berimbang (238 dan 13)
    - Kekurangan:
        - Accuracy terendah (0.854) dibanding model lain
        - Precision rendah (0.361)
        - False positive tertinggi (23) yang menunjukkan banyak kesalahan prediksi positif
- Random Forest
    - Kelebihan:
        - Accuracy lebih baik (0.888) dibanding Decision Tree
        - Precision (0.5) lebih baik dari Decision Tree
        - False positive rendah (3) menunjukkan lebih sedikit kesalahan prediksi positif
    - Kekurangan:
        - Recall rendah (0.091) menunjukkan kesulitan mendeteksi kasus positif
        - True negative sangat rendah (3)
        - False negative tinggi (30) menunjukkan banyak kasus positif yang tidak terdeteksi
- Linear SVC
    - Kelebihan:
        - Accuracy tertinggi (0.895)
        - Precision sempurna (1.0) artinya semua prediksi positif benar
        - Tidak ada false positive (0)
    - Kekurangan:
        - Recall sangat rendah (0.061) menunjukkan sangat sulit mendeteksi kasus positif
        - False negative tertinggi (31)
        - True negative sangat rendah (2)

Kesimpulan:
- Linear SVC dipilih karena keakuratan dalam memprediksi karyawan akan keluar atau tidak sangat diperlukan.

### Deployment
Deployment menggunakan streamlit dan pickle untuk menyimpan serta memuat model yang telah dibuat sebelumnya, berikut command untuk menjalankan deployment.
```
streamlit run prediction.py
```

## Business Dashboard
Business Dashboard terdiri 3 bagian yaitu:
1. Top Section - Key Metrics Cards
    - Overall Attrition Rate (Number), Keseluruhan presentasi dari Attrition.
    - Total Employee Count (Number), Jumlah karyawan.
    - Total Churned Employees (Number), Jumlah karyawan yang keluar.
    - Avarage Monthly Income (Number), Rata-rata gaji karyawan dalam sebulan.
2. Middle Section - Primary Charts
    - Department-wise Attrition (Bar Chart), Grafik yang menunjukan Attrition berdasarkan departemen.
    - Salary Range Impact (Bar Chart), Grafik yang menunjukan Attrition berdasarkan gaji.
3. Bottom Section - Detailed Analysis
    - Job Satisfaction vs Attrition (Pie Chart), Grafik yang menunjukan kepuasan dalam perkerjaan dengan perbandingan Attrition rate.
    - Work-Life Balance Impact (Bar Chart), Grafik yang menunjukan karyawan yang memiliki keseimbangan hidup dan kerja.

[Link Dashboard](https://ds-meta.getani.me/public/dashboard/0a18543d-f076-48b0-8579-f02067ea9058)
dan Berikut username dan password untuk metabase
```
root@mail.com
root123
```

## Conclusion
- Kesimpulan:
    - Solusi untuk mengatasi tingginya tingkat attrition ada dua pendekatan yaitu
        1. Pembuatan dashboard berguna untuk memonitor faktor-faktor apa saja yang mungkin terjadi seperti Dashboard yang telah dibuat dengan visualisasi Attrition berdasarkan departemen, pengaruh kepuasan karyawan terhadap Attrition rate serta keseimbangan kerja dan hidup.
        2. Menggunakan model machine learning yaitu dengan algoritma Linear SVC dengan akurasi 89.5% dan presisi 100% dalam memprediksi karyawan yang akan keluar.
    - Penyebab tingginya attrition rate
        1. Kebanyakan karyawan yang keluar juga dikarenakan mereka kerja melebihi jam kerja atau lembur dan ini adalah penyebab utama kenapa karyawan-karyawan sering keluar.
        2. Kebanyakan karyawan yang keluar memiliki gaji kurang dari atau sama dengan $5000 yang mengindikasikan bahwa gaji adalah penyebab kedua.
        3. Kebanyakan karyawan yang keluar berasal dari departemen sales yang mengindikasikan bahwa departemen sales adalah penyebab ketiga.
    - Karakteristik dari karyawan yang keluar
        1. Memiliki gaji dibawah atau sama dengan $5000.
        2. Berasal dari departemen sales.
        3. Sering banyak berpergian.
        4. Kebanyakan kerja melebihi jam kerja atau lembur.
        5. Kebanyakan dari mereka belum menikah atau lanjang.


### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Evaluasi dan Penyesuaian Kompensasi
    - Dengan mengevaluasi gaji atau jam kerja dapat membantu mengurangi kemungkinan karyawan keluar.
- Peningkatan Work-Life Balance
    - Untuk meningkatkan kepuasan kerja karyawan, perusahaan perlu mengimplementasikan kebijakan yang mendukung keseimbangan kehidupan kerja dengan begitu karyawan akan merasa puas dan dapat membantu mengurangi kemungkinan karyawan keluar.
-  Komunikasi
    - Adanya komunikasi baik perusahaan dapat mengetahui langsung masalah apa saja yang karyawan-karyawan hadapi dan itu akan membantu mengurangi kemungkinan karyawan keluar.
