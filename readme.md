### Set up database

1. ```./manage.py makemigrations && ./manage.py migrate && ./manage.py migrate --database=httcs```

2. In Sqlite console: 

   ```sql
   CREATE TABLE IF
   NOT EXISTS "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL
   );
   ```

   

