# chatbot-for-interview-scheduling

    pipenv shell

Rasa playground
https://rasa.com/docs/rasa/playground

    pipenv install rasa
    pipenv install python-socketio==4.6.1
    pipenv install python-engineio==3.13.2
    pipenv install rasa-x --extra-index-url https://pypi.rasa.com/simple
    pipenv install pandas
    pipenv install sanic==19.9.0
    https://github.com/rasahq/rasa/issues/5019

    at the time of installation, faced issues installing rasa x (https://forum.rasa.com/t/pip-takes-long-time/39274/3)
    pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple

To run duckling server (as DucklingHTTPExtractor is used)

    docker run -p 8000:8000 rasa/duckling

Install sqlite3, if you don't have it installed already on your system

    sudo apt install sqlite3

<!-- open sqlite3 -->

sqlite3 faqsdb //creates a database

    .mode csv
    .import groww_faqs_utf-8.csv growwfaqs
    .tables //to list all the tables under current db

rasa shell commands

    rasa run actions -vv //before running this make sure you've also added required config in endpoints.yml
    rasa run -m models --enable-api --cors "*" --debug
    rasa data validate // to check if there are conflicts

