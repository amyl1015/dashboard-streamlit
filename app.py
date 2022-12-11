import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json

st.header('This is a dashboard attempt')
st.text('The first data set is a table showing SARS-CoV-2 sequencing data.')
url = "https://lapis.cov-spectrum.org/open/v1/sample/aa-mutations"
# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())


# print the json response
print(data_json['data'])
df = pd.DataFrame.from_dict(data_json['data'])
st.dataframe(df)


#st.bar_chart(df)
#st.line_chart(df)

url = "https://mpox-lapis.genspectrum.org/v1/sample/nuc-mutations"

#------------------------
# Second Data set
# -------------------
st.text('The second data set is a table of results from the telehealth survey.')
telehealth = pd.read_csv("telehealth.csv")
pd.set_option('display.max_columns', None)
telehealth

#df = pd.DataFrame({'used telehealth':['yes', 'no', 'NaN'], 'val':[14, 4, 4]})
#ax = df.plot.bar(x='used telehealth', y='val', rot=0)
#st.dataframe(df)
#st.bar_chart(data=df, x='a', y='b')