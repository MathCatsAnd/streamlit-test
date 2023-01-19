import streamlit as st
import os

st.write('Test App')
output = os.popen('pip list').read()
st.markdown(output.replace('\n','  \n'))
