python manage.py migrate
python manage.py collectstatic --noinput
gunicorn django.wsgi:application