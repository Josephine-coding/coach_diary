import streamlit as st
import requests

def display_client_by_id(id):
    """
    request api to get one client by its id
    """
    response = requests.get(" http://127.0.0.1:8000/clients/{}".format(id))
    if not response:
        st.write('No Data!')
    else:
        customer = response.json()
        st.write('Name: ', customer['name'])
        st.write('Firstname: ', customer['firstname'])
        st.write('Information: ', customer['information'])
        st.write('Creation_date: ', customer['creation_date'])


def display_all_clients():
    """
    request api for the list of all clients
    """
    response = requests.get(" http://127.0.0.1:8000/clients")
    if not response:
        st.write('No Data!')
    else:
        customers = response.json()
        for customer in customers:
            st.write('Customer number: ', customer['id_customer'])
            st.write('Name: ', customer['name'])
            st.write('Firstname: ', customer['firstname'])
            st.write('Information: ', customer['information'])
            st.write('Creation_date: ', customer['creation_date'])
            st.write('---------------------------------------')


def create_a_client():
    """
    dsplay the inputs to create a customer and request api to create in db
    :return: none
    """
    input_name = st.text_input('Name:')
    if len(input_name) > 0:
        input_firstname = st.text_input('Firstname:')
        if len(input_firstname) > 0:
            input_information = st.text_input('Information:')
            if len(input_information) > 0:
                if st.button('create customer'):
                    customer = {'name': input_name, 'firstname': input_firstname, 'information': input_information,
                                'creation_date': datetime.today().strftime('%Y-%m-%d')}

                    response = requests.post("http://127.0.0.1:8000/customer/", json=customer)
                    if not response:
                        st.write("request failed")
                    else:
                        st.write("Customer {} {} is created".format(input_name, input_firstname))


def update_one_client_by_id(id):
    """
    display customer, save update (via api)
    """
    response = requests.get(" http://127.0.0.1:8000/customer/{}".format(id))
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
            response = requests.put("http://127.0.0.1:8000/customer/{}".format(id), json=customer)
            if not response:
                st.write("request failed")
            else:
                st.write("Customer {} {} is updated".format(input_name, input_firstname))


def delete_one_client_by_id(id):
    """
    choose a customer to delete from the db
    """

    # verify the customer exist in db
    response = requests.get(" http://127.0.0.1:8000/customer/{}".format(id))
    if not response:
        st.write('customex dont exist!')
    else:
        # call api to delete from database
        response = requests.delete("http://127.0.0.1:8000/customer/{}".format(id))
        if not response:
            st.write('no response')
        else:
            st.write('customer deleted')


# ##########################################TEXT##################################################""

def create_text(id_customer: int):
    """
    create a text and save it in db
    :param id_customer: int, id from the customer who wants to save his text
    :return: none
    """
    text = st.text_input('')
    if text:
        if st.button('save text'):
            score = afinn.score(text)
            feeling = "positif" if score > 0 else "négatif"
            new_text = {
                'content': text,
                'creation_date': datetime.today().strftime('%Y-%m-%d'),
                'feeling': feeling,
                'score': score,
                'id_customer': id_customer
            }

            # call api to create text in db
            response = requests.post("http://127.0.0.1:8000/text/", json=new_text)
            if not response:
                st.write("request failed")
            else:
                st.write("the text is save")


def display_all_text():
    """
    display all the text from all the customers
    :return: none
    """
    # get the list of all the texts via api
    response = requests.get(" http://127.0.0.1:8000/text/all/")
    if not response:
        st.write('No text!')
    else:
        texts = response.json()
        for text in texts:
            # get the customer who registrer this text, for each text
            result = requests.get(" http://127.0.0.1:8000/customer/{}".format(text['id_customer']))
            if not result:
                st.write('No writer')
            else:
                writer = result.json()
                st.write('Text Number: ', text['id_text'])
                st.write('Writer: {} {} '.format(writer['name'], writer['firstname']))
                st.write('Content: ', text['content'])
                st.write('feeling: {}({}))'.format(text['feeling'], text['score']))
                st.write('------------------------------------------------')


def delete_text_by_id(id_text: int):
    """
    delete a text from db
    :param id_text: int, id of text we want to delete
    :return: none
    """
    # call from api to et the text in db to be sure it exists
    response = requests.get(" http://127.0.0.1:8000/text/{}".format(id_text))
    if not response:
        st.write('text dont exist!')
    else:
        # call from api to crud to delete the text from db
        response = requests.delete("http://127.0.0.1:8000/text/{}".format(id_text))
        if not response:
            st.write('no response')
        else:
            st.write('text deleted')


def display_text_by_id(id_text: int):
    """
    display a choosen text
    :param id_text: int, id of the choosen text
    :return: none
    """
    # request to api to get the text asked
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


def display_all_text_by_cust(id_customer: int):
    """
    display the list of all the texts writen by one customer
    :param id_customer: int, id of the customer choosen
    :return: none
    """
    # request to api to get the list of the texts written by one customer
    response = requests.get(" http://127.0.0.1:8000/texts/all/{}".format(id_customer))
    if not response:
        st.write('No text!')
    else:
        texts = response.json()
        if len(texts) > 0:
            for text in texts:
                # call to api to get the customer writer of thoses texts
                result = requests.get(" http://127.0.0.1:8000/clients/{}".format(text['id_customer']))
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