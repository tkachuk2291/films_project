# films_project_api_service
### Api service for show top 5 films  

### Live film  endpoint 

follow for https://films-project.onrender.com/films/

### Telegram bot film  endpoints 
https://t.me/films2291_bot

###  Install PostgresSQL and create db
```shell
git clone https://github.com/tkachuk2291/films_project.git
``` 
```shell
cd films_project 
```
```shell
python3 -m venv venv  
``` 
```shell
source venv/bin/activate  
```
```shell
pip install -r requirements.txt  
```
### Setting up Environment Variables
```shell
touch .env  
```
### Example of environment variables
``` 
 .env.sample 
```

``` 
set DJANGO_SECRET_KEY='your_secret_key'
set TELEGRAM_BOT_KEY='your_secret_key'
set DATABASE_URL="url for db postgres"
set TG_REQUEST="https://films-project.onrender.com/films/ or http://127.0.0.1:8002/(if local)"
```
```shell
python manage.py migrate  
```
```shell
python manage.py runserver 8002 
```

### Getting endpoints Live
follow for https://films-project.onrender.com/films/
### Local
http://127.0.0.1:8002/














