1-Instalar virtualenv -> pip install virtualenv

2- Criar ambiente virtual -> python -m venv .venv

3- Ativar ambiente virtual -> .\.venv\Scripts\Activate

4- Instalar Django -> pip install django e pip install django-bootstrap-v5 com venv ativado
(adicionar 'bootstrap5' em settings.py)

5- Criar projeto -> django-admin startproject setup .

6- criar aplicativo -> python manage.py startapp nomeapp

(adiconar app em settings.py)

7- Rodar o projeto -> python manage.py runserver

8- Criar super usuário -> python manage.py createsuperuser

9 - Criar Tabela de banco de dados, rodar:

python manage.py makemigrations

python manage.py migrate