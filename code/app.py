import streamlit as st
import pandas as pd
import numpy as np
#from prediction import predict
import pickle

st.title('Catalytic Reformer')
st.markdown('Predict the Values like Reformate RON, C5+ RON, C6+ RON')

st.header('Parameters')
col1, col2, col3 = st.columns(3)
with col1:
    st.text('Feed Volume Flow')
    ff = st.slider('Feed-1', min_value=600, max_value=1500, value=700)
with col2:
    st.text('Reactor Temperature')
    r1T = st.slider('Reactor 1 Inlet Temperature', min_value=420, max_value=540, value=450)
    r2T = st.slider('Reactor 2 Inlet Temperature', min_value=420, max_value=540, value=450)
    r3T = st.slider('Reactor 3 Inlet Temperature', min_value=420, max_value=540, value=450)
    PST = st.slider('Product Separator Temperature', min_value=30, max_value=50, value=40)
with col3:
    st.text('H2HC Ratio')
    ratio = st.slider('H2HC Ratio - Mol/Mol', min_value=2, max_value=5, value=4)

if st.button('Predict'):
    rf = pickle.load(open(r'..\model\model_v1.pkl','rb'))
    result = rf.predict(np.array([[ff, r1T, r2T, r3T,PST, ratio]]))
    st.text(result[0])
