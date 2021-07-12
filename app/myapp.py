import streamlit as st
# Streamlit app running locally for now

##### SIDEBAR #####
st.sidebar.write('Choix de la page')
user = st.sidebar.radio ('',  ["Coach", "Client"])

def display_coach_page():
    selection = st.selectbox("Action",
                             ["Chosse action", "create a customer", 'display a customer', 'display all customers',
                              'delete customer', 'update a customer', "Display list of texts"], index=0)
    if selection == "display a customer":
        input_id = st.number_input('enter the customer id to display')
        if input_id > 0:
            input_id = int(input_id)
            display_cust_by_id(input_id)
    elif selection == "create a customer":
        create_cust()
    elif selection == "display all customers":
        display_all_cust()
    elif selection == 'delete customer':
        input_id = st.number_input('enter the customer id to delete')
        if input_id > 0:
            input_id = int(input_id)
            delete_cust_by_id(input_id)
    elif selection == 'update a customer':
        input_id = st.number_input('enter the customer id to update')
        if input_id > 0:
            input_id = int(input_id)
            update_cust_by_id(input_id)
    elif selection == "Display list of texts":
        display_all_text()

##### BODY #####
if user == 'Coach':
    st.write('Bienvenue Coach')
    display_coach_page()
elif user == 'Client':
    st.write('Bienvenue Client')
