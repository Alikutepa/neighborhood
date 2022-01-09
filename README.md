## Hood Watch
[Juliana Alikutepa](https://github.com/Alikutepa)

## Description
A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## User Story
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
## Setup and Installation


[Clone](https://github.com/Alikutepa/neighborhood.git) the repository:

Navigate into the folder and install requirements  


## Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate  

## Install Dependencies
pip install -r requirements.txt 

## Setup Database
SetUp your database User,Password, Host then make migrate

python manage.py makemigrations hood
## Migrate

python manage.py migrate 

## Run the application
python manage.py runserver 

## Testing the application
python manage.py test 

Open the application on your browser 127.0.0.1:8000.

## Technology used
* Python3.6
* Django 2.2.6
* Heroku

## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug
## Contact Information
If you have any question or contributions, please email me at [jalikutepa@gmail.com]

## License
[MIT](LICENSE)
Copyright (c) 2022 Juliana Alikutepa