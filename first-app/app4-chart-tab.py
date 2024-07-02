import streamlit as st
import pandas as pd
import plotly.graph_objects as go



# let's create a few charts using plotly
df = pd.read_csv('data/employees.csv', header=0).convert_dtypes()
st.dataframe(df)

labels, parents = df[df.columns[0]], df[df.columns[1]]


def makeTreemap(labels, parents):
    data =  go.Treemap(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color='lightgrey'
    )
    fig = go.Figure(data)
    return fig

def makeIcicle(labels, parents):
    data = go.Icicle(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color='lightgrey'
    )
    fig = go.Figure(data)
    return fig


def makeSunburst(labels, parents):
    data = go.Sunburst(
        ids=labels,
        labels=labels,
        parents=parents,
        root_color='lightgrey'
    )
    fig = go.Figure(data)
    return fig



def makeSankey(labels, parents):
    data = go.Sankey(
        node=dict(label=labels),
        link=dict(
            source=[list(labels).index(x) for x in labels],
            target=[-1 if pd.isna(x) else list(labels).index(x) for x in parents],
            label=labels,
            value=list(range(1, len(labels)))))
    fig = go.Figure(data)
    return fig


st.title('Hierarchical data viewer')

tabs = st.tabs(['Treemap','Icicle','Sunburst','Sankey'])

with tabs[0]:
    fig = makeTreemap(labels=labels, parents=parents)
    st.plotly_chart(fig, use_container_width=True)

# the other way of doing this is to have the expander in variables
fig = makeIcicle(labels=labels, parents=parents)
tabs[1].plotly_chart(fig, use_container_width=True)

with tabs[2]:
    fig = makeSunburst(labels=labels, parents=parents)
    st.plotly_chart(fig, use_container_width=True)


with tabs[3]:
    fig = makeSankey(labels=labels, parents=parents)
    st.plotly_chart(fig, use_container_width=True)
