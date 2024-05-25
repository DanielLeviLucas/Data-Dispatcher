ENV_FILE=.envs/.env
.PHONY: up down watch

db_up:
	docker compose --env-file $(ENV_FILE) up -d

db_down:
	docker compose --env-file $(ENV_FILE) down

serve:
	python manage.py runserver 0.0.0.0:8000

shell:
	python manage.py shell_plus

migrate:
	python manage.py migrate
