# <h1 align="center" id="title">🦴 BONE FRACTURE DETECTION SYSTEM 🦴</h1>

<div align="center">
<img src="https://images.unsplash.com/photo-1564725075388-cc8338732289?q=80&w=1271&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Bone X-Ray Header" width="600" height="350">
<p>
<small>
Sumber Image : <a href="https://unsplash.com/photos/x-ray-result-_GpJpHnyCSw">Unsplash Open Source Bone Fracture Image</a>
</small>
</p>
</div>

# <h1 align="center">TABLE OF CONTENT</h1>

1. [Deskripsi Project](#-deskripsi-project-)
2. [Sumber Dataset](#-sumber-dataset-)
3. [Preprocessing dan Pemodelan](#-preprocessing-dan-pemodelan-)
4. [Langkah Instalasi](#-langkah-instalasi-)
5. [Hasil dan Analisis](#-hasil-dan-analisis-)
6. [Sistem Sederhana Streamlit](#-sistem-sederhana-streamlit-)
7. [Biodata](#-biodata-)  

---

<h1 align="center" id="-deskripsi-project-">🏥 Deskripsi Project 🏥</h1>

Proyek ini berfokus pada **klasifikasi otomatis cedera patah tulang** melalui citra sinar-X (X-Ray). Dengan menggabungkan teknik pengolahan citra medis dan *Deep Learning*, sistem ini dirancang untuk mendeteksi keberadaan fraktur pada tulang manusia guna membantu tenaga medis dalam proses diagnosis awal.

---

<h1 align="center" id="-sumber-dataset-Sub">📊 Sumber Dataset 📊</h1>

Dataset yang digunakan merupakan kumpulan data citra medis publik yang telah dianonimkan, terdiri dari sekitar 8,863 citra X-Ray yang mencakup kategori `Normal` dan `Fractured`.

---

<h1 align="center" id="-preprocessing-dan-pemodelan-">🧑‍💻 Preprocessing dan Pemodelan 🧑‍💻</h1>

Citra medis diproses menggunakan teknik **CLAHE** untuk peningkatan kontras dan **Gaussian Blur** untuk pengurangan noise, guna memperjelas area retakan pada tulang sebelum dilakukan klasifikasi.

---

<h1 align="center" id="-hasil-dan-analisis-">🔍 Hasil dan Analisis 🔍</h1>

### Tabel Perbandingan Performa Model 
Berikut adalah ringkasan performa metrik evaluasi serta analisis hasil untuk setiap arsitektur model:

| Nama Model | Accuracy | Precision | Recall | F1-Score | Hasil Analisis |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Base CNN** | **0.79** | **0.82** | **0.82** | **0.79** | **Model Terbaik**, Walaupun model paling sederhana namun custom trainig dari awal memberikan kemampuan khusus untuk klasifikasi citra x-ray pada domain medis. |
| **MobileNetV2** | 0.62 | 0.62 | 0.62 | 0.61 | Model transfer learning yang paling ringan, namun dalam kasus ini belum mendapatkan akurasi yang cukup baik sehingga belum bisa diandalkan untuk klasifikasi. |
| **ResNet50** | 0.76 | 0.81 | 0.80 | 0.76 | Model transfer learning yang sedikit lebih baik dalam melakukan klasifikasi citra x-ray, namun masih belum sebaik model custom atau base yang di latih dari awal. |

#### Confusion Matrix 🔴🟢
Visualisasi prediksi benar dan salah untuk setiap kelas pada data pengujian:

| **Base CNN** | **MobileNetV2** | **ResNet50** |
| :---: | :---: | :---: |
| ![CM Base CNN](https://github.com/anindyaprayoga/bone-fracture-classification/blob/main/assets/confussion%20matrix%20cnn.png) | ![CM MobileNet](https://github.com/anindyaprayoga/bone-fracture-classification/blob/main/assets/confussion%20matrix%20mobilenetv2.png) | ![CM ResNet](https://github.com/anindyaprayoga/bone-fracture-classification/blob/main/assets/confussion%20matrix%20resnet-50.png) |

#### Learning Curves 📈
Grafik akurasi dan loss selama proses pelatihan (Training vs Validation):

| **Base CNN** | **MobileNetV2** | **ResNet50** |
| :---: | :---: | :---: |
| ![LC Base CNN](https://github.com/anindyaprayoga/bone-fracture-classification/blob/main/assets/learning%20curve%20cnn.png) | ![LC MobileNet](https://github.com/anindyaprayoga/bone-fracture-classification/blob/main/assets/learning%20curve%20mobilenetv2.png) | ![LC ResNet](https://github.com/anindyaprayoga/bone-fracture-classification/blob/main/assets/learning%20curve%20resnet-50.png) |

### Analisis Kesalahan
Berdasarkan hasil pengujian, model masih mengalami kesulitan pada:
1. Citra dengan noise yang sangat tinggi atau pencahayaan yang tidak merata.
2. *Hairline fracture* atau retakan tipis yang menyerupai garis sendi atau anatomi tulang normal.

---

<h1 align="center" id="-langkah-instalasi-">🔧 Langkah Instalasi 🔧</h1>

```bash
# Instalasi dependensi
pip install -r requirements.txt

# Menjalankan aplikasi
streamlit run app.py
```

---

<h1 align="center" id="-sistem-sederhana-streamlit-">🎓 Sistem Sederhana Streamlit 🎓</h1>

Aplikasi berbasis web ini memungkinkan pengguna untuk melakukan deteksi secara *real-time* dengan mengunggah file citra X-Ray.

### Tampilan Antarmuka
- **Upload Section**: Mendukung format JPG dan PNG.
- **Preprocessing View**: Menampilkan hasil filter CLAHE.
- **Prediction Result**: Menampilkan kategori (Normal/Fractured) disertai skor kepercayaan.

---

<h1 align="center" id="-biodata-">👤 Biodata 👤</h1>

👤 **[Nama Lengkap Anda]** 📘 **NIM**: [NIM Anda]  
🎓 **Program Studi**: [Prodi Anda]  
🏛️ **[Institusi Anda]**
