1-Instalar virtualenv
```
pip install virtualenv
```	

2- Criar ambiente virtual
```
python -m venv .venv
```	

3- Ativar ambiente virtual
```
.\.venv\Scripts\Activate
```
Rodar o comando para instalar as dependências com ele ativo
```
pip install -r requirements.txt
```
Ou instalar manualmente

* Django e Bootstrap
```
pip install django

pip install django-bootstrap-v5
```
6- Sempre que instalar algum pacote novo, atualizar o arquivo requirements.txt com o comando:
```
pip freeze > requirements.txt
```
7- Criar projeto

django-admin startproject setup .

8- Rodar o projeto
python manage.py runserver
http://127.0.0.1:8000/

9- criar aplicativo

python manage.py startapp projeto



Views 
criar templates em meuprojeto 

pip install django-bootstrap-v5

## Criar
Tabela de banco de dados
python manage.py makemigrations