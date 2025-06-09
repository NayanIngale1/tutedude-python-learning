# PostgreSQL DATABASE tutorial

# create database test;

# \l to see list of database

# drop database test;

# CREATE TABLE table_name(key datatype, key datatype, key datatype);
# CREATE TABLE students(name text, number int, age int);    # -- example

# \d to see list of relations


# add data
# INSERT INTO students(name,number,age) VALUES('nayan',1,28);
# INSERT INTO students(name,number,age) VALUES('sam',14,25);


# Retrieving data from database
# SELECT * FROM students;    # -- gives all the entries

# SELECT name FROM students;  # --- you will get only name


# SELECT * FROM students WHERE age=20;   # --- get all the data where students age is equal to 20


# SELECT number FROM students WHERE name='sam';


# deleting contents in the table
# TRUNCATE TABLE students;


# Docker command to run a PostgreSQL container with custom configuration
# docker run --name learning-db \        # Name the container "learning-db"
#   -e POSTGRES_USER=myuser \            # Set the default PostgreSQL username to "myuser"
#   -e POSTGRES_PASSWORD=password \      # Set the password for the user to "password"
#   -p 8080:5432 \       # Map host port 8080 to container's default PostgreSQL port 5432
#   -d postgres                           # Run the container in detached mode using the official postgres image


# To access the PostgreSQL database inside the container:

# 1. Preferred (direct):
# docker exec -it learning-db psql -U myuser -d postgres


# - `docker exec -it`: Executes a command inside a running container interactively.
# - `learning-db`: The name of your running PostgreSQL container.
# - `psql -U myuser`: Launches the PostgreSQL interactive terminal using the username you set via POSTGRES_USER.
# - `-d postgres`: Connects to the `postgres` database (default database created in PostgreSQL).
# This command skips bash and goes directly into the database shell.

# 2. Alternative (step-by-step):
# docker exec -it learning-db bash

# - This opens a bash shell inside the container so you can manually interact with it.

# psql -U myuser -d postgres

# - Once inside the container, this command launches the PostgreSQL terminal, similar to the above.


# connect to database
import psycopg2

conn = psycopg2.connect(dbname='postgres', user='myuser',
                        password='password', host='localhost', port='8080')

print('connected successfully')


cursor = conn.cursor()


def create_table():

    cursor.execute(''' create table employees(Name Text, Id int,Age int); ''')
    print('Table created successfully')
    conn.commit()


def insert_data():
    id = int(input('Enter employee Id: '))
    name = input('Enter employee Name: ')
    age = int(input('Enter employee Age: '))

    # cursor.execute(
    #     f''' insert into employees(Name,Id,Age) values('{name}',{id},{age}); ''')

    query = ''' insert into employees(Name, Id, Age) values(%s,%s,%s); '''
    cursor.execute(query, (name, id, age))
    print('Data addedd successfully')
    conn.commit()


def get_data():
    cursor.execute(''' select * from employees; ''')
    print(cursor.fetchall())
    conn.commit()


insert_data()
get_data()
conn.close()
