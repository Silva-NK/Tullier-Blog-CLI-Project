# Tullier Blog CLI Project

## Introduction

Tullier BLOG CLI is a blog manager that seeks to easily run and manage a small scale blog where memeber of Tullier can share thoughts, ideas and other important message and information. It manages users, posts and categories directly from the command line terminal, no need for a browser or web-server and perfect for small-scale, limited resource use. 

It utilises SQLITE database and a OOP-based design to ensure a simple, clean and fast way to manage internal blog content.


### Project Map
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── db
    │   ├── __pycache__
    │   │      ├── connection.cpython-38.pyc
    │   │      ├── models.cpython-38.pyc
    │   │      ├── seed.cpython-38.pyc
    │   │      ├── create_table.cpython-38.pyc
    │   ├── migrations
    │   │      ├── versions
    │   │      ├── README.md
    │   │      ├── env.py
    │   │      └── script.py.mako
    │   ├── alembic.ini
    │   ├── connection.py
    │   ├── create_tables.py
    │   ├── models.py
    │   └── seed.py
    ├── __pycache__
    │      ├── cli.cpython-38.pyc
    │      └── helpers.cpython-38.pyc
    ├── cli.py
    ├── debug.py
    └── helpers.py


### Data Model and CLI Functionality

This application uses a data model with three related tables: 
 - `users`
 - `posts`
 - `categories`

This application uses 2 dynamic model classes with full ORM methods (`create`, `delete`, `get all`, `find by name` and `find by id`) and corresponding CLI options for managing these records: 
 - `User`
 - `Post`

`Category`, on the other hand, is a static, pre-seeded table model that contains fixed categories relevant to posts. It functions as a lookup table, with no need for runtime creation, editing or deletion of category entries via the CLI but maintains the ORM methods and corresponding CLI options for `get all`, `find by name` and `find by id` for lookup purposes.

While the project requirements specify that *each* model class should have full CRUD CLI support, in this implementation, `Category` serves purely as seed data, ensuring data consistency and preventing unintended modification.  
This approach maintains the integrity of the application and simplifies the user experience, while still adhering to the general project guidelines for dynamic data models.


### Project starting necessities
1. Ensure PC has sqlite3, SQLAlchemy and alembic downloaded. if not:
    - Run 'sudo apt-get install sqlite3' on the terminal
    - Open the project folder and run 'pip install sqlalchemy alembic'

2. Ensure you install all project dependencies and create a virtual environment that the project will be ran on. For this use, 'pipenv install'

3. Ensure that you enter the now created virtual environment using 'pipenv shell'

4. If one wishes to create the EMPTY tables to be used, just run 'python -m lib.db.create_tables'

5. (Optional) If you wish to create the tables and immediately populate them with example/test data, run 'python -m lib.db.seed' to seed the data with constant data and editable example/test data.

6. In order to open the CLI menu, just run 'python -m lib.cli'

### Creating Your Own Git Repo



## Generating Your Pipenv



## Generating Your Database



## Generating Your CLI



## Updating Your README.md



### What Goes into a README?



## Conclusion



## Resources

- [Tullier-Blog-CLI-Project Git Repo](https://github.com/Silva-NK/Tullier-Blog-CLI-Project)
