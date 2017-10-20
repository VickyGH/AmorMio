web: gunicorn AmorMio.wsgi --log-file -
web: python manage.py collectstatic --noinput; gunicorn --workers=4 --bind=0.0.0.0:$PORT AmorMio/settings.py