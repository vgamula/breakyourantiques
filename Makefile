bootstrap:
	pip install -r requirements-dev.txt

run:
	python manage.py runserver

deploy:
	fab deploy
