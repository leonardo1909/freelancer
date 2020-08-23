build:
	docker-compose up --build

run:
	docker-compose up

coverage:
	coverage erase;
	coverage run manage.py test;
	coverage report;