import streamlit as st
import pandas as pd
import os, fnmatch, glob
import numpy as np
import plotly.express as px


st.markdown("<h1 style='text-align: center;'> Outlier Report 📝</h1>", unsafe_allow_html=True)
st.sidebar.markdown("# Outlier Report 📝")
st.markdown("")

cwd = os.getcwd()
df = pd.read_csv(f'{cwd}/pages/data.csv')

st.markdown("<h4 style='text-align: center;'> Raw data</h4>", unsafe_allow_html=True)
fig_1 = px.line(
        df,
        x="time",
        y=["facility"]
        #,color="Real Data"
        # barmode="group",
    )
st.plotly_chart(fig_1, use_container_width=True)

df['actual_facility'] = df['facility']
df['zscore'] = (df.facility - df.facility.mean())/df.facility.std(ddof=0)
outliers = df[df['zscore']>=2]

df['facility'] = np.where(df['zscore']>=2, None, df['facility'])
df['zscore'] = np.where(df['zscore']>=2, None, df['zscore'])
df = df.ffill()

st.markdown("<h4 style='text-align: center;'> step 1</h4>", unsafe_allow_html=True)
fig_2 = px.line(
        df,
        x="time",
        y=["facility"]
        #,color="Real Data"
        # barmode="group",
    )
st.plotly_chart(fig_2, use_container_width=True)

df['mean_50'] = df['facility'].rolling(51, center=True).mean()
df['diff'] = abs(df['mean_50']-df['facility'])
df['facility'] = np.where(df['diff']>=2, df['mean_50'], df['facility'])


st.markdown("<h4 style='text-align: center;'> step 2</h4>", unsafe_allow_html=True)
fig_3 = px.line(
        df,
        x="time",
        y=["facility"]
        #,color="Real Data"
        # barmode="group",
    )
st.plotly_chart(fig_3, use_container_width=True)


df['normalized_facility'] = df['facility']
st.markdown("<h4 style='text-align: center;'> Actual Facility VS Normalized Facility</h4>", unsafe_allow_html=True)
fig_4 = px.line(
        df,
        x="time",
        y=["actual_facility", "normalized_facility"]
        #,color="Real Data"
        # barmode="group",
    )
st.plotly_chart(fig_4, use_container_width=True)


st.markdown("<h4 style='text-align: center;'> outlier code:</h4>", unsafe_allow_html=True)
code = '''def outlier_normalizer(raw_data):
    raw_data['actual_facility'] = raw_data['facility']
    raw_data['zscore'] = (raw_data.facility - raw_data.facility.mean())/raw_data.facility.std(ddof=0)
    raw_data['facility'] = np.where(raw_data['zscore']>=2, None, raw_data['facility'])
    raw_data['zscore'] = np.where(raw_data['zscore']>=2, None, raw_data['zscore'])
    raw_data = raw_data.ffill()
    raw_data['mean_50'] = raw_data['facility'].rolling(51, center=True).mean()
    raw_data['diff'] = abs(raw_data['mean_50']-raw_data['facility'])
    raw_data['facility'] = np.where(raw_data['diff']>=2, raw_data['mean_50'], raw_data['facility'])
    raw_data['normalized_facility'] = raw_data['facility']
    raw_data.drop(columns=['facility'], inplace=True)
    return raw_data'''
st.code(code, language='python')

            
   
