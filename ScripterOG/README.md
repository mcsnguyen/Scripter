# Scripter

### This is the login system development branch for Scripter

To run:

* cd into the dev folder
* run the following command:

    python3 manage.py runserver

* then go to the following url : http://127.0.0.1:8000

#### Working Urls (*May not be current*):

try:
    http://127.0.0.1:8000/account/login/

    http://127.0.0.1:8000/account/logout/

    http://127.0.0.1:8000/register/

    http://127.0.0.1:8000/profile/

    http://127.0.0.1:8000/profile/edit/

    http://127.0.0.1:8000/change-password/

    http://127.0.0.1:8000/password_reset/

*Check urls.py for built paths*

### Try creating new users, loging in and out, and changing profile information!

### Password changes requires email logout form provided by Django
We need to create custom forms for this eventually but for now you can test by running a local smtp server

run

    python -m smtpd -n -c DebuggingServer localhost:1025

and go to http://127.0.0.1:8000/password_reset/   to try resetting

the server will send a dummy email message with the link (not an actual email). Follow link for password reset

#### For administration:

    http://127.0.0.1:8000/admin/

Super User name: polygenesis

Super User PW: cs480_2018

Test profile name: test

Test profile PW: cs480_2018

### Running In IDE:
Make sure that Crispy Forms is installed inside site-packages in the external libraries
* pip install django-crispy-forms

-----

10/1/2018 - 5:39 pm
Made a .py for the A4. I try to not interfere with the main back end stuff so
I made sure the project stil works with what I added. I added a RequestTest.py,
a test.txt, and a requirements.txt.

Specific Steps I took (just in case things go wrong/just to keep track off/idk what I did)
-Downloaded Python & Django
-Downloaded pip
-Change my Windows user PATH variable to the files containing python and pip
-Use pip to install virtualenv & pipenv
-Use virtualenv to create an environment to work in a copied version of the project
-Activated new environment
-Installed python in Eclipse IDE to open/edit .py files
-Use pipnev to install Requests, a dependency like java's jsoup.
-Create a .py file & .txt file in Eclipse for A4.
-Use pip freeze > requirements.txt to create a .txt file of necessary files used in project
-Deactivated environment
-git pull - git status - git add - git commit - git push