install:
	uv sync

migrate:
	python manage.py makemigrations
	python manage.py migrate

start-l:
	uv run python manage.py runserver
start-r:
	uv run gunicorn task_manager.wsgi:application --bind 127.0.0.1:8000
start-render:
	gunicorn task_manager.wsgi:application --bind 0.0.0.0:8000
build:
	./build.sh
