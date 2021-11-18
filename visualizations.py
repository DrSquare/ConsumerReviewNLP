import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.title("AutoMR")

data = pd.DataFrame({
    'Key Product Attributes' : ['picture quality','battery life', 'weight','brand'],
    'Number of Mentions' : [400, 300, 100, 20]
})

st.write(data)
    
bars = alt.Chart(data).mark_bar().encode(
    x = alt.X('Number of Mentions:Q', scale=alt.Scale(domain=(0, 450))), 
    y = alt.Y('Key Product Attributes:O', sort='-x')
)


text = bars.mark_text(
    align='left',
    baseline='middle',
    color='orange'
).encode(
    text='Number of Mentions:Q'
)

st.write((bars + text).properties(height=600, width=600))

data2 = pd.DataFrame([
    ['resolution', 5, 'Product_1'],
    ['lens quality', 3, 'Product_1'],
    ['sensor sensitivity', 1, 'Product_1'],
    ['quick focus', 2, 'Product_1'],
    ['low light performance', 5, 'Product_1'],
    ['accessories', 4, 'Product_1'],
    ['TTL viewing', 1 , 'Product_1'],
    ['Dust Removal System', 4, 'Product_1'],
    ['Low Battery Consumption', 3, 'Product_1'],
    ['Customizability', 3, 'Product_1'],
    ['resolution', 3, 'Product_2'],
    ['lens quality', 5, 'Product_2'],
    ['sensor sensitivity', 5, 'Product_2'],
    ['quick focus', 4, 'Product_2'],
    ['low light performance', 5, 'Product_2'],
    ['accessories', 2, 'Product_2'],
    ['TTL viewing', 3 , 'Product_2'],
    ['Dust Removal System', 4, 'Product_2'],
    ['Low Battery Consumption', 1, 'Product_2'],
    ['Customizability', 1, 'Product_2'],
], columns=['Key Product Attributes', 'Rating','Product_type'])

st.write(data2)

chart = alt.Chart(data2).mark_bar().encode(
    column='Key Product Attributes:N',
    x=alt.X('Product_type'),
    y= alt.Y('Rating:Q', scale=alt.Scale(domain=[0,6])),
    color=alt.Color('Product_type', scale=alt.Scale(range=['#3399FF','#FF9966']))

)
st.altair_chart(chart)
