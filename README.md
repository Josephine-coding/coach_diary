## coach_diary

## Goals
Create a database to store information, an API REST to interact with this database and a web application as a graphical interface


## Project management
You can find the project management, MPD and API map on this link : 
https://docs.google.com/spreadsheets/d/18OjktjL0UNmBUXAV2fcbG5-AGhNaoemgDJV8UNP3gDs/edit?usp=sharing


## Files structure
```
.
├── api                     # api files 
    ├── api                 # Contains api requests
├── app                     # Streamlit app files 
    ├── app_utils           # Contains functions to refactor code of streamlit page
    ├── myapp               # Contains code of streamlit page
├── database                # Database files 
    ├── crud                # Contains the CRUD needed for the API
    ├── database            # Script to create the database and tables
    └── models              # Contains the models needed for the API
    └── schemas             # Contains the schemas needed for the API
├── src                     # Source files 
    ├── utils               # Utils file
        ├── sql_fonctions   # Contains sql fonctions
├── test                    # Automated tests 
    └── conftest            # Define testing environment  
    └── test_api            # Define test of api
```
