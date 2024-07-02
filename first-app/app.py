import webbrowser
import urllib.parse
import pandas as pd
import streamlit as st

st.title('Hierarchical Data Viewer')

df = pd.read_csv('data/employees.csv', header=0).convert_dtypes()

st.dataframe(df)

# Create a graph dataframe in pandas
edges = ""
for _, row in df.iterrows():
    if not pd.isna(row.iloc[1]):
        edges += f'\t"{row.iloc[0]}" -> "{row.iloc[1]}";\n'

d = f'digraph {{\n{edges}}}'
st.graphviz_chart(d)

# rendering it through graphviz visual editor
# url = f'HTTP://magjac.com/graphviz-visual-editor/?dot={urllib.parse.quote(d)}'
# webbrowser.open(url)

