# HTTCS-app

## 如果你第一次建環境

0. 你要先建立虛擬環境，設定才不會和外面相互影響
   `python3 -m venv env`

但如果你超可憐沒辦法做 那請到群組載env.zip放進去ＱＡＱ

1. 這是一個Django app，又是一個全新的虛擬環境，所以你要在這個資料夾下裝Django
```
pip install django
pip install djangorestframework
pip install django-rest-polymorphic
```

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

## 幫空空如以的資料庫加些資料

1. 用 DB Browser For SQLITE，打開，
2. 選取DB，要選httcs.sqlite
3. 把insert_data.sql中的指令放入執行（最上面delete from那邊不要複製到）
4. 執行完畢，確認沒有錯誤，資料有進去
5. 存檔，關閉DB Browser
   
## Run server

`python manage.py runserver`

## APIs

在localhost下執行：
`http://127.0.0.1:8000/` 為前綴，有`admin/`, `api/user/`, `api/product/`, `api/transaction/` 等進入點

### admin/

示範：`http://127.0.0.1:8000/admin/`
在瀏覽器中輸入，會帶你到一管理頁面

### api/user/
*以下操作在Postman中*  
`http://127.0.0.1:8000/api/user/`：取得所有的user  

...待更新




