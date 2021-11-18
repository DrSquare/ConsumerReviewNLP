import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


st.title("AutoMR")

data = pd.DataFrame({
    'Key Product Attributes' : ['picture quality','brand', 'LCD and viewfinder','Battery', 'Lens', 'Stablization', 
                               'Video and sound', 'Shuttter Speed', 'Software', 'Warranty', 'Zoom and Flash'],
    'Number of Mentions' : [72521, 38709, 29186, 28244, 23152, 23114, 22139, 21576, 15397, 15226, 14014]
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

'picture quality','brand', 'LCD and viewfinder','Battery', 'Lens', 'Stablization', 
                               'Video and sound', 'Shuttter Speed', 'Software', 'Warranty', 'Zoom and Flash'

data2 = pd.DataFrame([
    ['picture quality', 5, 'Nikon D7000'],
    ['brand', 5, 'Nikon D7000'],
    ['LCD and viewfinder', 5, 'Nikon D7000'],
    ['Battery', 5, 'Nikon D7000'],
    ['Lens', 5, 'Nikon D7000'],
    ['Stablization', 5, 'Nikon D7000'],
    ['Video and sound', 5 , 'Nikon D7000'],
    ['Shuttter Speed', 5, 'Nikon D7000'],
    ['Software', 5, 'Nikon D7000'],
    ['Warranty', 1, 'Nikon D7000'],
    ['Zoom and Flash', 5, 'Nikon D7000'],
    
    ['picture quality', 5, 'Canon EOS 6D'],
    ['brand', 5, 'Canon EOS 6D'],
    ['LCD and viewfinder', 5, 'Canon EOS 6D'],
    ['Battery', 1, 'Canon EOS 6D'],
    ['Lens', 5, 'Canon EOS 6D'],
    ['Stablization', 5, 'Canon EOS 6D'],
    ['Video and sound', 5 , 'Canon EOS 6D'],
    ['Shuttter Speed', 5, 'Canon EOS 6D'],
    ['Software', 5, 'Canon EOS 6D'],
    ['Warranty', 5, 'Canon EOS 6D'],
    ['Zoom and Flash', 5, 'Canon EOS 6D']
  ], columns=['Key Product Attributes', 'Rating','Product_type'])

st.write(data2)

chart = alt.Chart(data2).mark_bar().encode(
    column='Key Product Attributes:N',
    x=alt.X('Product_type'),
    y= alt.Y('Rating:Q', scale=alt.Scale(domain=[0,6])),
    color=alt.Color('Product_type', scale=alt.Scale(range=['#3399FF','#FF9966']))

)
st.altair_chart(chart)
