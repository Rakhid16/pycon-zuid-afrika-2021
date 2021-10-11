# PyCon Zuid Afrika 2021
My code for Python Conference Zuid Afrika 2021

![Python version](https://img.shields.io/badge/Python-3.8.10-blue.svg)

## How to set up :notebook:
1. Clone the repo and get inside the directory
2. Create your virtual environment and activate it
```
$ virtualenv venv
$ source venv/bin/acitvate
```
3. Install the third party packages
```
$ pip install -r requirements.txt
```
4. Make your **.env** file on **src/** directory. So the files inside the **src/** directory will be like this :
```
...
    src/
    ├── .env
    ├── async_plain_sql.py
    ├── config.py
    ├── db_init.py
    ├── db_models.py
    ├── sync_plain_sql.py
    └── try_sqlalchemy.py
...
```
5. Content of the **.env** file:
```
username = your_username
password = your_password
address = your_address
db_name = your_db_name
```
6. Run the simple benchmark test
```
$ python3 main.py
```

## My own benchmark:
- Ubuntu 20.04, GCC 9.3.0
- CPU: Intel Core i5-7200U 2.5-3.1 GHz, 12GiB DDR4

| Rows | Sync time processing  | Async time processing |
------------- | ------------- | ------------- |
| 898 | 0.6498196125030518  | 0.1622464656829834  |
| 1796 | 0.4164566993713379  | 0.1117696762084961  |
| 3592 | 3.645622730255127  | 0.08057069778442383  |
| 7184 | 1.3551499843597412  | 0.1499958038330078  |
| 14368 | 4.4217565059661865  | 0.22365760803222656  |
| 28736 | 3.9319002628326416  | 0.41571688652038574  |
| 57472 | 8.055142164230347  | 0.7584617137908936  |
| 114944 | 15.577688932418823  | 1.9088993072509766  |
| 229888 | 30.813102960586548  | 5.105829477310181  |
| 459776 | 64.41133952140808  | 7.353327751159668  |
| 919552 | 123.6319043636322  | 16.71780300140381  |
| 1839104 | 244.02325177192688 | 37.45272207260132 |

*in a seconds