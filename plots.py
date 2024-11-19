import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['Line-1','Line-2','Line-3'])

st.header('1. Charts with Random Numbers')

st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar Chart')
st.bar_chart(chart_data)

st.header('2. Data visualization with matplotlib and seaborn')
st.subheader('2.1 Loading the Dataframe')
df=pd.read_csv(r'C:\Users\dell\Desktop\dataScience\Streamlit\iris.csv')
st.dataframe(df)

st.subheader('2.2 Bar graph with Matplotlib')
fig=plt.figure(figsize=(15,8))
df['Species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('2.3 Distribution plot with Seaborn')
fig=plt.figure(figsize=(15,8))
sns.distplot(df['SepalLengthCm'])
st.pyplot(fig)

st.header('3 multiple Graphs in One coloumn')
col1,col2=st.columns(2)
with col1:
    col1.header='KDE = False'
    fig1=plt.figure()
    sns.distplot(df['SepalLengthCm'],kde=False)
    st.pyplot(fig1)
with col2:
    col2.header='Hist = False'
    fig2=plt.figure()
    sns.distplot(df['SepalLengthCm'],hist=False)
    st.pyplot(fig2)

st.header("4. Changing Styles")
col1,col2=st.columns(2)
with col1:
    fig=plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['PetalLengthCm'],hist=False)
    st.pyplot(fig)
with col2:
    fig=plt.figure()
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['SepalLengthCm'],hist=False)
    st.pyplot(fig)

st.header('5. Exploring different graphs')
st.subheader('5.1 Scatter Plot')
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count Plot')
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x='Species')
st.pyplot(fig)

st.subheader('5.3 Box Plot')
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x='Species',y='PetalLengthCm')
st.pyplot(fig)

st.subheader('5.4 Violin-Plot')
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x='Species',y='PetalLengthCm')
st.pyplot(fig)

