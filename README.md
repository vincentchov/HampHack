# BreadCrumbs

## Environment Setup

First, make sure to install `mysql` and `libmysqlclient-dev`.

```bash
$ sudo apt-get install mysql-server
$ sudo apt-get install libmysqlclient-dev
```


To get the development environment setup, make sure the `python3-dev`, `virtualenv`, and `pip` are installed. Start by running

```bash
$ virtualenv -p python3
$ source env/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=run.py
```

To run the application:

```bash
$ flask run
```

## Database Configuration

Log into mysql as a root user:

```bash
$ mysql -u root -p
```

Create a new user (this will be you) and password. Then create the database:

```sql
mysql> CREATE USER 'mynewuser'@'localhost' IDENTIFIED BY 'goodPassword';
mysql> GRANT ALL PRIVILEGES ON * . * TO 'mynewuser'@'localhost';
mysql> CREATE DATABASE breadcrumbs;
```

To configure the database, make a copy of the example database config file:

```bash
$ cp db_config.py.example db_config.py
```

and change your username and password in `db_config.py`.

Now run the database migrations:

```bash
$ flask db upgrade
```

If you make any changes to the models, you can create new migrations by running

```bash
$ flask db migrate
```
