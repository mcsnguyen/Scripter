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

