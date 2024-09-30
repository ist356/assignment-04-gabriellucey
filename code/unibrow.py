'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file_upload = st.file_uploader("Upload a file", type=['csv', 'xlsx', 'json'])
#The UniBrow application is a streamlit application which displays a data from a file.

#It consists of 3 inputs:

#upload a file in Excel (XLSX), Comma-Separared, with Header (CSV), or Row-Oriented Json (JSON) into a dataframe
#select which columns to display from the dataframe
#build a fiter on the dataframe based on a text column and one of the values in the column.
#And 2 outputs:

#the dataframe with column / row filters applied.
#the describe of the dataframe (to see statistics for the numerical columns)

if file_upload:
    df = pl.load_file(file_upload, pl.get_file_extension(file_upload.name))
    
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to display", cols)
    
    if selected_cols:
        df_filtered = df[selected_cols]
        st.write(df_filtered)
        st.write("DataFrame Description:")
        st.write(df_filtered.describe())
        
        filter_col = st.selectbox("Select a column to filter", selected_cols)
        filter_val = st.text_input("Enter a value to filter")
        
        if st.button("Filter"):
            st.write(df_filtered[df_filtered[filter_col] == filter_val])


