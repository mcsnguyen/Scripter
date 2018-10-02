#Scripter 

Testing Vim for Windows.


How to run for now

using terminal :

cd into the Scripter root folder
run the following command: python manage.py runserver
then go to the following url : http://127.0.0.1:8000



HTML file for homepage will be located in Scripter-master/Scripter/scripter_app/templates/index.html

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