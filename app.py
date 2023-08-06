import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Streamlit learn", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
with st.sidebar:
    selected = option_menu("Main Menu", ["Dashboard","Data Visualization"], 
        icons=['house','pie-chart'], menu_icon="cast", default_index=0)
    selected

if selected == 'Dashboard':
    st.markdown("---")
    st.title('Welcome To Streamlit Learn Dashboard')

    st.write(" Streamlit Learn Dashboard merupakan tampilan visual yang dapat digunakan untuk mempresentasikan informasi mengenai produk secara ringkas dan terstruktur. Dashboard ini dapat digunakan untuk memantau produk, menganalisis tren penjualan produk, dan dapat digunakan sebagai bahan untuk pengambilan keputusan .")
    
    st.write('Silahkan Upload File dan Pilih Menu Sidebar untuk mulai melakukan analisa')
    # st.write('')
    st.markdown("---")
elif selected == 'Data Visualization':
    uploaded_file = st.file_uploader("Choose a file")
    ###### Transactions and Product Category datasets have no null cells.
    df_new = pd.read_csv(uploaded_file)
    df_new.drop_duplicates(inplace = True)
    sdf = df_new[df_new['Qty'] >= 0]
    """Books, Electronics and Home & Kitchen were the most purchased product categories."""
    category1 = sdf.groupby(by=['prod_cat'], as_index = False)['Qty'].count()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig = plt.figure(figsize=(8,4))
    savefig = plt.savefig('orderperproduct.png')
    sns.set_style('whitegrid')
    sns.barplot(x = "prod_cat", y = 'Qty', data = category1,  palette= "plasma")
    plt.xlabel('Product Category')
    plt.ylabel('Total Orders')
    plt.title('Total successful orders per product category')
    st.pyplot(savefig)