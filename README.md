# create_insert_sql
for postgresql

## use lib_py
need clone [lib_py](https://github.com/bigzhu/lib_py) in home path

##  use pipenv
```
pipenv install
```

## config file
db connect info must in `./conf/db.ini`

content like this
```
[db]
host=127.0.0.1
port=5432
db_name=test
user=test
password=test
```
