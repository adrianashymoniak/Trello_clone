**Required:**
* python 3.8
* django 3.0
* django rest framework 3.11
* django-ordered-model 3.3.0
* django-rest-auth 0.9.5
* coreapi 2.3.3
* drf-yasg 1.17.1

**Optional:**
* virtual env

**Installation process:**
* Clone repository: `git clone https://github.com/adrianashymoniak/Trello_clone.git`
* Create virtual env: run command in terminal `python -m venv myvenv`
* Activate virtual env (optional): `source myvenv/bin/activate`
* run: `pip install -r requirements.txt` (for installing required libraries in your virtual env)
* Make sure your virtual environment is activated and requirements are installed
* Go to Trello_clone folder and run migration: `python manage.py migrate`
* Create super user: `python manage.py createsuperuser`
* Run server locally: `python manage.py runserver`
* Open browser and go to `http://127.0.0.1:8000/api/v1/projects`

**All routes we can find here: `api/v1/schema/` and `api/v1/docs/`**