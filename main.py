import streamlit as st
import requests
# import handcalcs.render
# Judul Aplikasi
st.title("Interaktif API dengan Streamlit")

# Pilih agen berdasarkan keahlian bahasa pemrograman menggunakan st.radio
agent_options = [
    "Python Programmer",
    "JavaScript Developer",
    "Java Developer",
    "C++(cpp) Programmer",
    "Go Developer",
    "Math Solver"
]

selected_agent = st.radio(
    "Pilih agen berdasarkan keahlian bahasa pemrograman:", agent_options)

# Input untuk prompt
prompt = st.text_input(f"Masukkan prompt untuk {selected_agent}:", "")

# Tombol untuk mengirim permintaan dan menampilkan hasil
if st.button("Kirim"):
    if prompt:
        # URL API dengan parameter prompt
        url = f"https://api.ryzendesu.vip/api/ai/blackbox?chat=kamu adalah{selected_agent}terbaik maka tolong bantu saya,{prompt}(tanpa format latex)&options=gpt-4o"

        try:
            # Mengirim permintaan GET untuk mendapatkan data dari API
            response = requests.get(url)
            response.raise_for_status()  # Periksa apakah ada error HTTP

            # Menangani respons JSON
            try:
                data = response.json()  # Coba parsing sebagai JSON
                st.success("Hasil Diterima!")

                # Menampilkan hasil yang sesuai dengan bahasa pemrograman yang dipilih
                result = ("response", "")

                # Menampilkan data dalam format JSON jika perlu
                st.json(data)

            except ValueError:
                # Jika respons bukan JSON, tampilkan sebagai teks
                st.text(response.text)

        except requests.exceptions.RequestException as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Mohon masukkan prompt terlebih dahulu.")
