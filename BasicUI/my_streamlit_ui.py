import streamlit as st

#User input for search query
user_input = st.text_input("Enter your search query")

#implementing SQL Logic from SQL database
import sqlite3 # importing the sqlite3 module

def run_query(query):
        conn = sqlite3.connect('lewinsky.db') #connects to the database
        result = conn.execute(query).fetchall() #runs the query and returns the results
        conn.close() #closes the connection
        return result #returns the results

#Needs to be adapted to SQL database and logic
if user_input: #Only run if user input is not empty
    query = f"SELECT * FROM your_table WHERE some_column LIKE '%{user_input}%'"
    results = run_query(query) #Define the results of the query
    for result in results: # 'results' is defined
        st.write(result)

        #we then run the folowing command in terminal/bash
        #streamlit run my_streamlit_ui.py