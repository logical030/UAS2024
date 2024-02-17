import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from GitHub
url = 'https://raw.githubusercontent.com/username/repository/main/data-kejadian-bencana-banjir.csv'
data = pd.read_csv(url)

# Handling missing or zero values in 'nilai_kerugian' column
data['nilai_kerugian'] = data['nilai_kerugian'].replace(0, data['nilai_kerugian'].mean())

# Pertanyaan 1: Total Nilai Kerugian per Wilayah
st.subheader('Pertanyaan 1: Total Nilai Kerugian per Wilayah')

nilai_kerugian = data.groupby('wilayah')['nilai_kerugian'].sum().reset_index()

plt.figure()
plt.bar(nilai_kerugian['wilayah'], nilai_kerugian['nilai_kerugian'])
plt.title('Total Nilai Kerugian per Wilayah')
plt.xlabel('Wilayah')
plt.ylabel('Total Nilai Kerugian (Rp)')
st.pyplot(plt)

# Pertanyaan 2: Jumlah Pengungsi per Bulan
st.subheader('Pertanyaan 2: Jumlah Pengungsi per Bulan')

data['bulan'] = pd.to_datetime(data['bulan'], format='%m').dt.month_name()

pengungsi = data.groupby('bulan')['jumlah_pengungsi'].sum().reset_index()

plt.figure()
plt.plot(pengungsi['bulan'], pengungsi['jumlah_pengungsi'])
plt.title('Jumlah Pengungsi per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengungsi')
st.pyplot(plt)
