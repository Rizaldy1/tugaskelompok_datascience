import streamlit as st
from datetime import date

# Set background image and styling
st.markdown(
    """
    <style>
        body {
            background-image: url('URL_GAMBAR'); /* Ganti URL_GAMBAR dengan URL gambar yang Anda inginkan */
            background-size: cover;
            background-repeat: no-repeat;
            padding: 20px;
            color: white; /* Ganti warna teks sesuai kebutuhan Anda */
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>VALUE BARANG TOKO</h1>", unsafe_allow_html=True)

# Input
Tanggal = st.date_input("Pilih Tanggal", date.today())
Nama = st.text_input("Masukkan Nama")
Awal = st.number_input("Jumlah Barang Awal", 0)
Masuk = st.number_input("Jumlah Barang Masuk", 0)
Keluar = st.number_input("Jumlah Barang Keluar", 0)
hitung = st.button("Hitung Value")

# Calculation and Output
if hitung:
    total_masuk = Awal + Masuk
    st.header("Total Barang Masuk")
    st.success(f"Total barang masuk pada {Tanggal}: {total_masuk}")

if hitung:
    total_barang = Awal + Masuk - Keluar
    st.header("Total Barang")
    st.success(f"Total barang pada {Tanggal}: {total_barang}")

    # Menampilkan informasi dengan tanda pembutan
    st.markdown("### Assodiqiyah Grup:")
    st.markdown("- Nuryanto Sidiq Saputro - 20670032.")
    st.markdown("- Rizaldy Novianto - 20670035.")
