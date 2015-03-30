test:
	./manage.py syncdb

run:
	./manage.py syncdb runserver

syncdb:
	./manage.py syncdb --noinput
	./manage.py loaddata su.json