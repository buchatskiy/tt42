DJANGO_SETTINGS_MODULE = testpr.settings

.PHONY: test run syncdb

test:
	python manage.py test

run:
	python manage.py runserver

syncdb:
	python manage.py syncdb --noinput
	python manage.py loaddata su.json