Created on Django 1.3.X

Installation
============

	git clone git://github.com/tanelikaivola/limu.git
	cd limu
	git submodule init
	git submodule update
	cd limuweb
	./manage.py syncdb --noinput
	./manage.py runserver
