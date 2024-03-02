import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Baca data Anda
day_df = pd.read_csv('day_baru.csv')
hour_df = pd.read_csv('hour_baru.csv')

def main():
    # Tambahkan gambar sepeda di atas
    st.image('sepeda.jpeg', use_column_width=True)

    # Tambahkan judul dengan emoticon senyum dan warna font
    st.markdown("<h1 style='text-align: center; color: red;'>Bike sharing analysis 😊</h1>", unsafe_allow_html=True)
    
    # Tambahkan sidebar dengan judul rentang waktu
    st.sidebar.title("Rentang Waktu: 2011/01/01 - 2012/12/31")
    
    st.markdown("<h2 style='text-align: center; color: white;'>Pertanyaan 1: Bagaimana pola penggunaan sepeda berfluktuasi sepanjang hari? Pada jam berapa terjadi puncak penggunaan sepeda dan kapan penggunaan sepeda cenderung paling sedikit?</h2>", unsafe_allow_html=True)
    plot_hourly_trend(hour_df)
    
    st.markdown("<h2 style='text-align: center; color: white;'>Pertanyaan 2: Bagaimana perubahan pola penggunaan sepeda berkaitan dengan pergantian musim? Apakah terdapat perbedaan yang signifikan dalam jumlah penyewaan sepeda antara musim semi, musim panas, musim gugur, dan musim dingin?</h2>", unsafe_allow_html=True)
    plot_seasonal_trend(day_df)
    
    # Anda bisa menambahkan kode untuk pertanyaan lain dan visualisasi lainnya di sini

def plot_hourly_trend(df):
    group_hour_sum = df.groupby('hour')['total_count'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(group_hour_sum.index, group_hour_sum.values, marker='o', linestyle='-', color='blue')
    ax.set_xlabel('Jam dalam Sehari')
    ax.set_ylabel('Jumlah Penyewaan Sepeda')
    ax.set_title('Tren Penyewaan Sepeda dari Jam ke Jam')
    ax.set_facecolor('lightgrey')
    plt.grid(True)
    st.pyplot(fig)

def plot_seasonal_trend(df):
    group_season_sum = df.groupby('season')['total_count'].sum()
    seasons = ['Fall', 'Spring', 'Summer', 'Winter']
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(seasons, group_season_sum, color=['lightblue', 'lightgreen', 'orange', 'grey'])
    ax.set_xlabel('Musim', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.set_title('Perbandingan Jumlah Penyewaan Sepeda Berdasarkan Musim', fontsize=14)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    ax.set_facecolor('lightgrey')
    plt.grid(True)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
