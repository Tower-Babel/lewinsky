import streamlit as st
from PIL import Image


st.set_page_config(layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a Page", ["Home", "Resources", "Project"])

st.title("Portfolio")

if page == "Home":
   


    def load_css():
        with open("style.css") as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    def st_button(icon, url, label, iconsize):
        if icon == 'cup':
            button_code = f'''
            <p>
                <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                    <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
                        <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                    </svg>  
                    {label}
                </a>
            </p>'''

            
       
        return st.markdown(button_code, unsafe_allow_html=True)

    load_css()

    col1, col2, col3 = st.columns(3)
    col2.image(Image.open('irobot.jpg'))

    st.header('Team 1 Project')

    st.info(" Search dashboard the decomposes a complex text-to-SQL task "+
            "into smaller sub-tasks using Large Language Model, Machine Learning, Opensearch and Streamlit  ")
    

    icon_size = 20

    st_button('cup', 'https://github.com/Tower-Babel/lewinsky', 'Github', icon_size)
   

elif page == "Resources":
    st.header("Resources")
    st.write("This is the Resource page.")
    
    

elif page == "Project":
    st.header("Project")
    st.write("Project page.")
    
    
    st.subheader("PDF Report")
    st.write("Click the button below to generate and download a PDF report.")
    if st.button("Generate PDF Report"):
        
        st.write("PDF report generated and downloaded.")
