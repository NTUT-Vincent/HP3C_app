# HTTCS-app

## 如果你第一次建環境
0. 這是一個Django app，所以你要裝Django
```
pip install django
pip install djangorestframework
pip install django-rest-polymorphic
```
1. 你要先建立虛擬環境
   `python3 -m venv env`
2. 要抓到虛擬環境下的變數，__**每一次離開回來這個環境都要跑**__
   `source env/bin/activate`

3.  Set up database
```
./manage.py makemigrations product_management transaction_management user_management
./manage.py migrate
./manage.py migrate --database=httcs
```
*****
## 如果你DBMS跑不起來才要這個：
1. In Sqlite console: 

   ```sql
   CREATE TABLE IF
   NOT EXISTS "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL
   );
   ```
*****
## Run server

`python manage.py runserver`

   

