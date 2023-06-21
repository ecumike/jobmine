# jobmine

Django app to track job openings you've posted for and their current status and history.

## 📖 Installation
```
$ git clone https://github.com/ecumike/jobmine.git
$ cd jobmine
```


### Pip

```
$ python -m venv .venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# macOS
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000
```

### ⭐️ Support
Give a ⭐️  if this project helped you!

### License
[Apache 2 license - Free to use and modify](LICENSE)

