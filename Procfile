web: gunicorn AmorMio.wsgi --log-file -
web: python AmorMio/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT AmorMio/settings.py