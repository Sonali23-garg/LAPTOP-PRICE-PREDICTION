import streamlit as st 
import joblib 
import pandas as pd 
import numpy as np
pipe = joblib.load("pipe.joblib")
df = joblib.load("df.joblib")
st.title("laptop price predictor")
company_name=st.selectbox("Brand",df["Company"].unique())
Type=st.selectbox("Type",df["TypeName"].unique())
ram=st.selectbox("Ram",[2,4,6,8,12,16,32,64])
weight=st.number_input("enter weight in kg: ")
Touch_screen=st.selectbox("Touch Screen",[1,0])
Ips=st.selectbox("IPS",[1,0])
Screen_size= st.number_input("enter screen size: ")#ppi hai
cpu=st.selectbox('CPU',df["Cpu brand"].unique())
HDD=st.selectbox("hdd in gb",[0,128,256,512,1024,2024])
SDD=st.selectbox("ssd in gb",[0,8,128,256,512])
gpu_brand=st.selectbox("GPU Band",df["Gpu brand"].unique())
os=st.selectbox("OS",df["os"].unique())
if st.button("predict"):
    prediction=pipe.predict([[company_name,Type,ram,weight,Touch_screen,Ips,Screen_size,cpu,HDD,SDD,gpu_brand,os]])
    st.title(f"The pakage will be : {prediction}")