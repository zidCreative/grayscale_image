import streamlit as st
from PIL import Image

st.sidebar.image("zidCreative_putih.png")

st.title("Program Konversi gambar Grayscale")
gamb = st.file_uploader("Upload gambar yang ingin anda konversi", type=['jpg' , 'png' ])

if gamb is not None :
    fileg = Image.open(gamb)
    st.text("Gambar Original")
    st.image(fileg)
    
    size = fileg.size
    st.text(size)
    greyscale = fileg.convert("L")
        
    tombol = st.button("Konversi Gambar")
    if tombol :
        st.text("Gambar Grayscale")
        st.image(greyscale)
        st.success("Gambar berhasil dikonversi, klik kanan pada gambar untuk untuk menyimpan")
        
            

