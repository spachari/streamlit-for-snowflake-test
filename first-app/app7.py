import urllib.parse
import pandas as pd
import streamlit as st
from io import StringIO


def getGraph(df):

    # Create a graph dataframe in pandas
    edges = ""
    for _, row in df.iterrows():
        if not pd.isna(row.iloc[1]):
            edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'
    return f'digraph {{\n{edges}}}'


@st.cache_data
def loadFile(filename):
    return pd.read_csv(filename, header=0).convert_dtypes()


st.title('Hierarchical Data Viewer')

filename = 'data/employees.csv'
uploaded_file = st.sidebar.file_uploader(
    "Upload a csv file", type=['csv'], accept_multiple_files=False
)
if uploaded_file is not None:
    filename = StringIO(uploaded_file.getvalue().decode('UTF-8'))

df_orig = loadFile(filename=filename)

st.dataframe(df_orig)
cols = list(df_orig.columns)

# form
# with st.sidebar:
#     with st.form('my-form'):
#         child = st.selectbox("Child Column Name", cols, index=0)
#         parent = st.selectbox("Parent Column Name", cols, index=1)
#         df = df_orig[[child, parent]]
#         st.form_submit_button("Refresh")


with st.sidebar:
    child = st.selectbox("Child Column Name", cols, index=0)
    parent = st.selectbox("Parent Column Name", cols, index=1)
    df = df_orig[[child, parent]]


print(uploaded_file)

tabs = st.tabs(["Source", "Graph", "Bot Code"])

tabs[0].dataframe(df_orig)


chart = getGraph(df)
tabs[1].graphviz_chart(chart)



# rendering it through graphviz visual editor
url = f'HTTP://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(chart)}'


tabs[2].link_button("Visualise Online", url)
tabs[2].code(chart)


# @st.cache_data
# 1. used for serializable objects like dataframe
# 2. always copy the data

# @st.cache_resource
# 1. used for non-serializable data like connection
# 2. does not copy the data