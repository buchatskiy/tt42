test:
	./manage.py syncdb test

run:
	./manage.py syncdb runserver

syncdb:
	./manage.py syncdb --noinput
	./manage.py loaddata su.json