import streamlit as st
import os

st.write('Test App')
output = os.popen('pip list').read()
st.markdown(output.replace('\n','  \n'))

try:
  import matplotlib
  st.write('environment.yml correctly installed matplotlib')
except:
  st.write('environment not activated')
  out = os.popen('''conda activate myenv
pip list''')
