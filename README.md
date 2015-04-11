# Parse Foreign Foreign Data Wrapper for PostgreSQL

This data wrapper allows you to access your Parse object as a PostgreSQL foreign table.

## Installation

You will need to install and create the [multicorn](http://multicorn.org/) extension in your database:

```
$  pgxn install multicorn
...

$ psql my_database
psql (9.4.1)
Type "help" for help.

my_database=# CREATE EXTENSION multicorn;
```

After that you can install this wrapper via:

```
$ pip install git+https://github.com/spacialdb/parse_fdw.git
...
```

## Usage

To use this you must first create a `SERVER`:

```sql
my_database=# CREATE SERVER multicorn_parse FOREIGN DATA WRAPPER
  multicorn OPTIONS( wrapper 'parse_fdw.parse_fdw.ParseFdw');
```

and then create a `FOREIGN TABLE` with the following required options:

```sql
my_database=# CREATE FOREIGN TABLE test (
    speed float,
    course float
) server multicorn_parse options(
  application_id 'my_app_id',
  rest_api_key 'my_rest_api_key',
  class_name 'my_class_name' );

my_database=# SELECT * from test;
     speed      |  course
----------------+-----------
             -1 |        -1
             -1 |        -1
             -1 |        -1
              0 |        -1
              0 |        -1
             -1 |        -1
             -1 |        -1
             -1 |        -1
             -1 |        -1
             -1 |        -1
             -1 |        -1
             -1 |        -1
             -1 |        -1
             -1 |        -1
              0 |        -1
             -1 |        -1
  2.45000004768 | 14.765625
 0.879999995232 | 89.296875
 (18 rows)
```
