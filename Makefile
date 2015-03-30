test:
	./manage.py syncdb

run:
	./manage.py runserver

syncdb:
	./manage.py syncdb --noinput
	./manage.py loaddata su.json