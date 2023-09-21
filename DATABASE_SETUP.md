# Fitness Telegram Bot
A Telegram bot built with Python that allows you to track your progress at the gym.


## Description
The instruction is designed to connect the database using the SQLAlchemy ORM


## Installation
  *Check if PIR is installed
1. Install the necessary packages

     ```shell
     pip install SQLAlchemy
     ```
    
2. Install the database adapter

     ```shell
     pip install psycopg2
     ```

3. Install the module

     ```shell
    pip install python-dotenv

     ```

4. It is necessary to create a separate Postgres database for your bot, you can see how to do this in the database lessons. Data that will be used in the config files
username
password
localhost
database_name
example URL below


5. You need to add a config file to the project
.env
in which the configs will be placed, namely - the TG bot token and the database URL, an example of adding a database URL
DATABASE_URL = "postgresql://admin_fitness:password@localhost/fitness_bot_db"

6. A models.py file was also created in the project
Where you need to create models for the DB.
An example of creation is in the file

7.An example of a function for creating a user has been added to the main.py file, use ORM to work with the database according to the same principle.

8. Added in the db file
Module for installation and configuration of connection to the database.

This module performs the following actions:
1. Downloads the database configuration from environment variables using the python-dotenv library.
2. Creates a connection to the database using SQLAlchemy.
3. Creates a SQLAlchemy session factory for interacting with the database.
Use the `SessionLocal` variable to create database sessions in your code.


More details on SQLAlchemy https://docs.sqlalchemy.org/en/20/index.html