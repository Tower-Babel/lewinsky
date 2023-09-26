import streamlit as st
import pandas as pd
import io
import requests
from streamlit_searchbox import st_searchbox
from typing import Any, List


st.set_page_config(layout="wide")

# Search bar
text_search = st.text_input("Search here", value="")

# import database/csv currently using dummy data
url="https://raw.githubusercontent.com/mydgd/snowflake-table-catalog/main/sample_data.csv"
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')))

df['CREATED'] = pd.to_datetime(df['CREATED'])
df['LAST_ALTERED'] = pd.to_datetime(df['LAST_ALTERED'])

#st.write(df)

m2 = df['TABLE_NAME'].str.contains(text_search)
df_search = df[m2]

col_values = df["TABLE_NAME"].astype(str).tolist()


def autocomplete(text_search: str) -> List[any]:
    match = [value for value in col_values if value.startswith(text_search)]
    return match

# pass search function to searchbox
selected_value = st_searchbox(
    autocomplete,
    key="searchbox",
)    

#results schema -> https://blog.streamlit.io/create-a-search-engine-with-streamlit-and-google-sheets/
#trending search schema-> https://github.com/mydgd/snowflake-table-catalog
#console command -> streamlit run projectp1.py
