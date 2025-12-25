import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Bone Fracture Detection",
    page_icon="🦴",
    layout="wide"
)

# Judul Utama
st.markdown("<h1 style='text-align: center;'>🦴 Bone Fracture Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Sistem deteksi patah tulang otomatis berbasis Deep Learning (ResNet50)</p>", unsafe_allow_html=True)
st.divider()

# ==========================================
# 2. FUNGSI HELPER
# ==========================================

@st.cache_resource
def load_model():
    """Memuat model yang sudah dilatih (pastikan file .h5 tersedia)"""
    try:
        # Ganti nama file sesuai dengan model yang Anda simpan
        model = tf.keras.models.load_model('model_resnet50.h5')
        return model
    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
        return None

def medical_preprocessing(image_array):
    """
    Preprocessing yang sama dengan saat pelatihan:
    CLAHE -> Gaussian Blur -> Normalization
    """
    # Pastikan dalam format uint8 untuk OpenCV
    img = np.array(image_array, dtype='uint8')
    
    # Konversi ke Gray jika RGB
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img
        
    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=1.1, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # Gaussian Blur minimal
    blurred = cv2.GaussianBlur(enhanced, (3, 3), 0)
    
    # Balikkan ke RGB karena model menerima 3 channel
    final_img = cv2.cvtColor(blurred, cv2.COLOR_GRAY2RGB)
    
    # Resize ke ukuran input model
    final_img = cv2.resize(final_img, (224, 224))
    
    # Normalisasi [0, 1]
    return final_img.astype('float32') / 255.0

# ==========================================
# 3. ANTARMUKA PENGGUNA (UI)
# ==========================================

model = load_model()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Unggah Citra X-Ray")
    uploaded_file = st.file_uploader("Pilih file gambar (JPG, PNG, JPEG)...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_container_width=True)

with col2:
    st.subheader("🔍 Hasil Analisis")
    
    if uploaded_file is not None:
        if model is not None:
            with st.spinner('Sedang menganalisis...'):
                # Preprocessing
                processed_img = medical_preprocessing(image)
                
                # Tampilkan hasil pemrosesan medis (opsional untuk user)
                with st.expander("Lihat Hasil Preprocessing Medis (CLAHE)"):
                    st.image(processed_img, caption="Hasil Preprocessing", use_container_width=True)
                
                # Reshape untuk batch prediction
                input_arr = np.expand_dims(processed_img, axis=0)
                
                # Prediksi
                prediction = model.predict(input_arr)[0][0]
                
                # Tampilkan Hasil
                st.write("---")
                if prediction > 0.5:
                    st.error(f"### HASIL: FRACTURED (PATAH)")
                    st.write(f"**Confidence Score:** {prediction * 100:.2f}%")
                    st.warning("Catatan: Hasil ini hanyalah alat bantu. Silakan konsultasikan dengan ahli radiologi.")
                else:
                    st.success(f"### HASIL: NORMAL")
                    st.write(f"**Confidence Score:** {(1 - prediction) * 100:.2f}%")
                    st.info("Catatan: Tidak ditemukan indikasi patah tulang yang jelas pada gambar ini.")
        else:
            st.warning("Model belum dimuat. Pastikan file model_resnet50.h5 ada di folder aplikasi.")
    else:
        st.info("Silakan unggah gambar X-ray untuk memulai deteksi.")

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: grey;'>Developed for Medical Imaging Research Purpose</p>", unsafe_allow_html=True)