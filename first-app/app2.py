import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('Hierarchical data viewer')

st.header('this is a header')

st.subheader('this is a sub header')

st.caption('this is a caption')

st.write('this is write')

st.code('v = variable()\nanother_call()', 'python')

st.markdown('**bold**')

st.markdown('*italics*')

st.divider()

st.error('this is an error')

st.info('this is an info')

st.warning('this is a warning')

st.success('this is an success')

st.balloons()

st.snow()

