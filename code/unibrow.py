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
    selected_cols = st.multiselect("Select columns to display", cols, default=cols)
    
    df_filtered = df[selected_cols]
    include_filter = st.toggle("Include filter")

    if include_filter:
        text_cols = pl.get_columns_of_type(df_filtered, 'object')
        filter_col1 = st.selectbox("Select the first column to filter", text_cols)
        if filter_col1:
            unique_vals1 = pl.get_unique_values(df_filtered, filter_col1)
            filter_val1 = st.selectbox("Select a value to filter for the selected column", unique_vals1)
            df_filtered = df_filtered[df_filtered[filter_col1] == filter_val1]
                
        
    st.write(df_filtered)
    st.write("DataFrame Description:")
    st.write(df_filtered.describe())

