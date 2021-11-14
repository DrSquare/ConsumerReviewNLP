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




data2 = pd.DataFrame({
    'Key Product Attributes' : ['resolution', 'lens quality','sensor sensitivity','quick focus','low light performance','accessories','TTL viewing','Dust Removal System','Low Battery Consumption','Customizability'],
    'Product_1' : [5, 3, 1, 2, 5, 4, 1, 4, 3, 3],
    'Product_2' : [3, 5, 5, 4, 5, 2, 3, 4, 1, 1],
})

st.write(data2)

base = alt.Chart(data2).properties(
    width=250
)

left = base.encode(
    y=alt.Y('Key Product Attributes:O', axis=None, sort=None),
    x=alt.X('Product_1:Q', title='Product1',sort=alt.SortOrder('descending')),
).mark_bar().properties(title='Product1')

middle = base.encode(
    y=alt.Y('Key Product Attributes:O', axis=None, sort=None),
    text=alt.Text('Key Product Attributes:O'),
).mark_text(color='white').properties(width=150)

right = base.encode(
    y=alt.Y('Key Product Attributes:O', axis=None, sort=None),
    x=alt.X('Product_2:Q', title='Product2'),
).mark_bar().properties(title='Product2')

st.altair_chart(alt.concat(left, middle, right, spacing=5), use_container_width=True)