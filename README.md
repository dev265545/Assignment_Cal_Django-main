Clone the repo

git clone

Create virtual environment

python -m venv venv

Activate virtual environment

venv\Scripts\activate

Install Packages for running this API

pip install -r requirements.txt

### Executing the API

```
python manage.py runserver
```

### API Documentation

## Get Users Calendar Events

Asks for Authorisation and redirects to '/rest/v1/calendar/redirect'
