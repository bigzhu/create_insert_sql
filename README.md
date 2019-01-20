# create_insert_sql
for postgresql

## use lib_py
need clone [lib_py](https://github.com/bigzhu/lib_py) in home path

```
git clone https://github.com/bigzhu/lib_py ~/lib_py
```

##  use pipenv
```bash
pip install pipenv
pipenv --python 3.7 install
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

## run
example: 

In to pipenv and  run like this:
```bash
pipenv shell
python main.py table_name old_table_name
```
