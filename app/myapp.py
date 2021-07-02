import streamlit as st
# Streamlit app running locally for now

##### SIDEBAR #####
st.sidebar.write('#choix de la page')
user = st.sidebar.radio ('',  ["Coach", "Client"])

##### BODY #####
if user == 'Coach':
    st.write('Bienvenue Coach')
elif user == 'Client':
    st.write('Bienvenue Client')