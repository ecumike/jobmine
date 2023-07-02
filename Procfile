release: python manage.py collectstatic --noinput
release: python manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT jobmine.wsgi:application