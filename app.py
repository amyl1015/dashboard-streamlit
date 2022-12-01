import streamlit as st
import pandas as pd
import numpy as np
import urllib.request import urlopen
import json

url = "https://lapis.cov-spectrum.org/open/v1/sample/aa-mutations"
# store the repsonse of url
repsonse = urlopen(url)

# storing the JSON response
# from url in data
data_jason = json.loads(response.read())

# print the json response
print(data_json['data'])
df = pd.DataFrame.from_dict(data_json['data'])
st.dataframe(df)


st.bar_chart(df)
st.line_chart(df)

# df 2
url = "https://mpox-lapis.genspectrum.org/v1/sample/nuc-mutations"
# store the repsonse of url
repsonse = urlopen(url)

# storing the JSON response
# from url in data
data_jason = json.loads(response.read())

# print the json response
print(data_json['data'])
df_mp = pd.DataFrame.from_dict(data_json['data'])
st.dataframe(df_mp)
