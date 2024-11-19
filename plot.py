import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

st.header(" 1. Altair Scatter Plot")
chart_data= pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart=alt.Chart(chart_data).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart)




st.header('2.Interactive Charts')

st.subheader('2.1 Line charts')
df= pd.read_csv(r'C:\Users\dell\Desktop\dataScience\Streamlit\iris.csv')
iris_list=df.columns.tolist()
iris_choices= st.multiselect('Choose Your Option',iris_list)
new_df=df[iris_choices]
st.line_chart(new_df)

st.subheader('2.2 Area Chart')
st.area_chart(new_df)

st.header('3.Data Visualization with plotly')

st.subheader('3.1 Displaying the dataset')
df=pd.read_csv(r'C:\Users\dell\Desktop\dataScience\Streamlit\iris.csv')
st.dataframe(df.head())

st.subheader('3.2 Pie Chart')
fig=px.pie(df, values = 'SepalLengthCm' , names= 'Species')
st.plotly_chart(fig)

st.subheader('3.3 Pie Chart With Multiple Parameters')
fig=px.pie(df, values = 'SepalLengthCm' , names= 'Species',opacity=.7,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

st.header('3.4 Histogram')
x1=np.random.randn(200)
x2=np.random.randn(200)
x3=np.random.randn(200)

hist_data = [x1,x2,x3]
group_labels=['Group-1','Group-2','Group-3']
fig=ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)