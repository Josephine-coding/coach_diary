import streamlit as st
import requests
from datetime import datetime
from afinn import Afinn

afinn = Afinn()

import sys
sys.path.insert(0, "/home/apprenant/PycharmProjects/coach_diary")
#from app_utils import display_client_by_id, display_all_clients, create_a_client, delete_one_client_by_id, update_one_client_by_id

##### SIDEBAR #####
st.sidebar.write('Choix de la page')
user = st.sidebar.radio ('',  ["Coach", "Client"])

##### BODY #####
if user == 'Coach':

    st.write('Welcome Coach')
    selection = st.selectbox("Choose what you want to do",
                             [" ", "create a client", 'display a client', 'display all clients',
                              'delete a client', 'update a client', "display list of texts"], index=0)

    if selection == "display a client":
        input_id = st.number_input('enter the client id to display')
        if input_id > 0:
            input_id = int(input_id)
            #display_client_by_id(input_id)
            response = requests.get(" http://127.0.0.1:8000/clients/{}".format(input_id))
            if not response:
                st.write('No Data!')
            else:
                client = response.json()
                st.write('Name: ', client['name'])
                st.write('Firstname: ', client['firstname'])
                st.write('Information: ', client['info'])

    elif selection == "create a client":
        #create_a_client()
        input_name = st.text_input('Name:')
        if len(input_name) > 0:
            input_firstname = st.text_input('Firstname:')
            if len(input_firstname) > 0:
                input_information = st.text_input('Information:')
                if len(input_information) > 0:
                    if st.button('create client'):
                        client = {'name': input_name, 'firstname': input_firstname, 'information': input_information,
                                    'creation_date': datetime.today().strftime('%Y-%m-%d')}

                        response = requests.post("http://127.0.0.1:8000/clients/", json=client)
                        if not response:
                            st.write("request failed")
                        else:
                            st.write("client {} {} is created".format(input_name, input_firstname))

    elif selection == "display all clients":
        #display_all_clients()
        response = requests.get(" http://127.0.0.1:8000/clients")
        if not response:
            st.write('No Data!')
        else:
            clients = response.json()
            for client in clients:
                st.write('Customer number: ', client['id_client'])
                st.write('Name: ', client['name'])
                st.write('Firstname: ', client['firstname'])
                st.write('Information: ', client['info'])
                st.write('---------------------------------------')

    elif selection == 'delete a client':
        input_id = st.number_input('enter the client id to delete')
        if input_id > 0:
            input_id = int(input_id)
            #delete_one_client_by_id(input_id)
            response = requests.get(" http://127.0.0.1:8000/clients/{}".format(input_id))
            if not response:
                st.write('customex dont exist!')
            else:
                # call api to delete from database
                response = requests.delete("http://127.0.0.1:8000/clients/{}".format(input_id))
                if not response:
                    st.write('no response')
                else:
                    st.write('customer deleted')

    elif selection == 'update a customer':
        input_id = st.number_input('enter the client id to update')
        if input_id > 0:
            input_id = int(input_id)
            #update_one_client_by_id(input_id)
            response = requests.get(" http://127.0.0.1:8000/clients/{}".format(input_id))
            if not response:
                st.write('No Data!')
            else:
                old_dcustomer = response.json()

                # display original informatiosn about customer
                st.write('Name: ', old_dcustomer['name'])
                st.write('Firstname: ', old_dcustomer['firstname'])
                st.write('Information: ', old_dcustomer['information'])
                st.write('Creation date: ', old_dcustomer['creation_date'])
                st.write('Last modification date: ', old_dcustomer['modification_date'])

                # display inputs to make update
                input_name = st.text_input('Update name:')
                input_firstname = st.text_input('Update firstname:')
                input_information = st.text_input('Update information:')

                # save the updating
                if st.button('update customer'):
                    customer = {}
                    if input_name != "":
                        customer['name'] = input_name
                    else:
                        customer['name'] = old_dcustomer['name']

                    if input_firstname != "":
                        customer['firstname'] = input_firstname
                    else:
                        customer['firstname'] = old_dcustomer['firstname']

                    if input_information != "":
                        customer['information'] = input_information
                    else:
                        customer['information'] = old_dcustomer['information']

                    customer['modification_date'] = datetime.today().strftime('%Y-%m-%d')

                    # call api to save the updated customer in db
                    response = requests.put("http://127.0.0.1:8000/clients/{}".format(input_id), json=customer)
                    if not response:
                        st.write("request failed")
                    else:
                        st.write("Client {} {} is updated".format(input_name, input_firstname))

    elif selection == "display list of texts":
        #display_all_texts()
        response = requests.get(" http://127.0.0.1:8000/texts/all/")
        if not response:
            st.write('No text!')
        else:
            texts = response.json()
            for text in texts:
                # get the customer who registrer this text, for each text
                result = requests.get(" http://127.0.0.1:8000/clients/{}".format(text['id_customer']))
                if not result:
                    st.write('No writer')
                else:
                    writer = result.json()
                    st.write('Text Number: ', text['id_text'])
                    st.write('Writer: {} {} '.format(writer['name'], writer['firstname']))
                    st.write('Content: ', text['content'])
                    st.write('feeling: {}({}))'.format(text['feeling'], text['score']))
                    st.write('------------------------------------------------')


elif user == 'Client':
    st.write('Welcome Client')
    #name = st.text_input('Name')
    #firstname = st.text_input('Firstname')
    input_id = st.number_input('What is your id?')
    input_id = int(input_id)
    if input_id:
        response = requests.get(" http://127.0.0.1:8000/clients/{}".format(input_id))
        if not response:
            st.write('Customer not found')
        else:
            customer = response.json()

            # only if customer exist in db, initialization of choices
            selection = st.selectbox("What do you want to do?",
                                     [" ", "Create a text", "Display list of texts", "Display a text",
                                      "Delete a text"])

            # one choice call one display method
            if selection == "Create a text":
                #create_text(customer['id_customer'])
                text = st.text_input('')
                if text:
                    if st.button('save text'):
                        feeling = afinn.score(text)
                        #feeling = "positif" if score > 0 else "négatif"
                        new_text = {
                            'content': text,
                            'id_client': input_id,
                            'feeling': feeling,
                            'creation_date': datetime.today().strftime('%Y-%m-%d'),
                            'modification_date': datetime.today().strftime('%Y-%m-%d')
                        }

                        # call api to create text in db
                        response = requests.post("http://127.0.0.1:8000/texts/", json=new_text)
                        if not response:
                            st.write("request failed")
                        else:
                            st.write("the text is save")


            elif selection == "Display list of texts":
                #display_all_text_by_cust(customer['id_customer'])
                response = requests.get(" http://127.0.0.1:8000/texts/all/{}".format(input_id))
                if not response:
                    st.write('No text!')
                else:
                    texts = response.json()
                    if len(texts) > 0:
                        for text in texts:
                            # call to api to get the customer writer of thoses texts
                            result = requests.get(" http://127.0.0.1:8000/clients/{}".format(text['input_id']))
                            if not result:
                                st.write('No writer')
                            else:
                                writer = result.json()
                                st.write('Text Number: ', text['id_text'])
                                st.write('Writer: {} {} '.format(writer['name'], writer['firstname']))
                                st.write('Content: ', text['content'])
                                st.write('feeling: {}({})'.format(text['feeling'], text['score']))
                                st.write('------------------------------------------------')
                    else:
                        st.write("this customer has no texts yet")

            elif selection == "Delete a text":
                input_id = st.number_input('Enter the number of the text you want to delete')
                if input_id > 0:
                    input_id = int(input_id)
                    #delete_text_by_id(input_id)
                    response = requests.get(" http://127.0.0.1:8000/texts/{}".format(id_text))
                    if not response:
                        st.write('text dont exist!')
                    else:
                        # call from api to crud to delete the text from db
                        response = requests.delete("http://127.0.0.1:8000/texts/{}".format(id_text))
                        if not response:
                            st.write('no response')
                        else:
                            st.write('text deleted')

            elif selection == "Display a text":
                input_id = st.number_input('Enter the number of the text you want to display')
                if input_id > 0:
                    input_id = int(input_id)
                    #display_text_by_id(input_id)
                    response = requests.get(" http://127.0.0.1:8000/texts/{}".format(id_text))
                    if not response:
                        st.write('No text!')
                    else:
                        text = response.json()
                        # request to api to get the customer writer of the asked text
                        result = requests.get(" http://127.0.0.1:8000/clients/{}".format(text['id_customer']))
                        if not result:
                            st.write('No writer')
                        else:
                            writer = result.json()
                            st.write('Text Number: ', text['id_text'])
                            st.write('Writer: {} {} '.format(writer['name'], writer['firstname']))
                            st.write('Content: ', text['content'])
                            st.write('feeling: {}({})'.format(text['feeling'], text['score']))