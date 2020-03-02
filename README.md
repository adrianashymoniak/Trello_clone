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
* Go to test_task_olymp_agency folder and run migration: `python manage.py migrate`
* Create super user: `python manage.py createsuperuser`
* Run server locally: `python manage.py runserver`
* Open browser and go to `http://127.0.0.1:8000/`

**Routes:**
* `api/v1/projects` - All projects page
* `api/v1/projects/<int:pk>/` - Project detail page
* `api/v1/projects/<int:project_id>/columns/` - All columns related to a project
* `api/v1/projects/<int:project_id>/columns/<int:pk>/` - Column details
* `api/v1/projects/<int:project_id>/tasks/` - All tasks related to a column
* `api/v1/projects/<int:project_id>/tasks/<int:pk>/` - Task detail
* `api/v1/rest-auth/login` - Login 
* `api/v1/rest-auth/logout` - Logout
* `api/v1/rest-auth/password/reset` - Reset password
* `api/v1/schema/` - Schema
* `api/v1/docs/` - API documentation