release: python manage.py migrate
web: gunicorn oc_lettings_site.settings.wsgi --preload --log-file -
