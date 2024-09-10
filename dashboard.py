import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(
    layout='wide',
    page_icon="🎉",
    page_title="pokemon dashboard",
)

@st.cache_data
def load_data():
    file = "pokemon.csv"
    data = pd.read_csv(file)
    return data

def main():
    st.image("hero.jpeg",use_column_width=True)
    st.title("pokemon dashboard")
    with st.spinner("loading pokemons..."):
      df =load_data()

     # st.snow()
    rows, columns = df.shape
    col_names = df.columns.tolist()
    c1,c2,c3 = st.columns(3)
    c1.subheader(f"Total rows: {rows}")
    c2.subheader(f"Total columns: {columns}")
    c3.subheader(f"columns:{",".join(col_names)}")


    

# yaha double underscore h 4 baaar

if __name__=="__main__":
    main()

# run command= streamlit run dashboard.py
