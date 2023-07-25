# jobmine

Django app to track job openings you've posted for and their current status and history.

## 📖 Installation
```
$ git clone https://github.com/ecumike/jobmine.git
$ cd jobmine
```


### Setup

```
$ python -m venv .venv
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ ./manage.py migrate
(.venv) $ ./manage.py createsuperuser
(.venv) $ ./manage.py runserver

# Load the site at http://127.0.0.1:8000
```

### Sample data

```
# Generate a sample data set of ## job postings (minimum 20)
(.venv) $ ./manage.py generate_sample_data 39

# Clear sample data
(.venv) $ ./manage.py clear_sample_data
```

### ⭐️ Support
Give a ⭐️  if this project helped you!

### License
[Apache 2 license - Free to use and modify](LICENSE)

