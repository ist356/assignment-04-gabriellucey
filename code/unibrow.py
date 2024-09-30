'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file_upload = st.file_uploader("Upload a file", type=['csv', 'xlsx', 'json'])

if file_upload:
    df = pl.load_file(file_upload, pl.get_file_extension(file_upload.name))
    
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to display", cols)
    
    if selected_cols:
        filter_col = st.selectbox("Select a column to filter", selected_cols)
        filter_val = st.text_input("Enter a value to filter")
        
        if filter_val:
            df_filtered = df[selected_cols][df[selected_cols][filter_col] == filter_val]
        else:
            df_filtered = df[selected_cols]
        
        st.write(df_filtered)
        st.write("DataFrame Description:")
        st.write(df_filtered.describe())

