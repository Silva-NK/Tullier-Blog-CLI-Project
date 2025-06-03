# Tullier Blog CLI Project

## Introduction

Tullier BLOG CLI is a blog manager that seeks to easily run and manage a small scale blog where members of the Tullier staff can share thoughts, ideas and other important messages and information. It manages users, posts and categories directly from the command line terminal with no need for a browser or web-server and perfect for small-scale, limited-resource use. 

It utilises SQLITE database and a OOP-based design to ensure a simple, clean and fast way to manage internal blog content.

### Problem I'm trying to solve
- If an organisation has limited resources and small-scale architecture they can still be able to run a small command-line-based blog without need for a web browser or web-server.


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
    │   ├── seed.py
    │   └── tullierdb.db
    ├── __pycache__
    │      ├── cli.cpython-38.pyc
    │      └── helpers.cpython-38.pyc
    ├── cli.py
    ├── debug.py
    └── helpers.py


### Data Model and CLI Functionality

This application uses a data model with three related tables:
- **Users**: Staff members who can create blog posts.
- **Posts**: Blog entries shared by users.
- **Categories**: Categorisation of the posts by topic.

Each table is represented by a model class with thorough data validation, relationship handling, and dynamic ORM methods for record management:

1. __User Model__

* Table: users

* Fields: id, name

* Relationships:

    * One user can have multiple posts (posts relationship).

* Key methods:

    * create(session, name)
    * get_all()
    * find_by_name(name)
    * find_by_id(id_)
    * update_name(session, new_name)
    * delete(session)

The model ensures:
- Name must be a string containing only letters and spaces.
- Name cannot be empty.

2. __Category Model__

* Table: categories

* Fields: id, name

* Relationships:

    * One category can have multiple posts (posts relationship).

* Key methods:

    * create(session, name)
    * get_all()
    * find_by_name(name)
    * find_by_id(id_)
    * update_name(session, new_name)
    * delete(session)

The model ensures:
- Name must be a unique, non-empty string.

3. __Post Model__

* Table: posts

* Fields: id, title, content, user_id, category_id

* Relationships:

    * Each post belongs to a single user and a single category.

* Key methods:

    * create(session, title, content, user_id, category_id)e
    * get_all()e
    * find_by_title(title)e
    * find_by_id(id_)e
    * update_post(session, new_title, new_content, new_user_id, new_category_id)
    * delete(session)

The model ensures:
- Titles and content are non-empty strings.
- User ID and Category ID must exist in the database to maintain referential integrity.

### Model Relationships

The relationships between the models are implemented using SQLAlchemy’s relationship and ForeignKey mechanisms:

* __User__ → Post: One-to-many relationship
A user can have multiple posts.

* __Category__ → Post: One-to-many relationship
A category can have multiple posts.

* __Post__: Belongs to one user and one category.
Foreign key references to users.id and categories.id ensure data consistency.

These relationships allow easy navigation between records in queries and enable dynamic loading of associated data.

### How It Works in the CLI
The CLI uses these dynamic models to provide functionality for creating, updating, listing, and deleting:
* Users
* Categories
* Posts

For example:

* **Create a new post**: The CLI will validate that the user ID and category ID exist before allowing creation.

* **List all posts**: The CLI will show post details, including the author (user) and category.

The CRUD ORM methods (create, delete, get_all, find_by_name, find_by_id) ensure data is always validated and consistent.



### Project starting necessities

1. Ensure PC has sqlite3, SQLAlchemy and alembic downloaded. if not:
    - Run `sudo apt-get install sqlite3` on the terminal
    - Open the project folder and run `pip install sqlalchemy alembic`

2. Ensure you install all project dependencies and create a virtual environment that the project will be ran on. For this use, `pipenv install`

3. Ensure that you enter the now created virtual environment using `pipenv shell`

4. If one wishes to create the EMPTY tables to be used, just run `python -m lib.db.create_tables`

5. (Optional to step 4) Otherwise, if you wish to create the tables and immediately populate them with example/test data, run `python -m lib.db.seed` to seed the data with constant data and editable example/test data.

6. In order to open the CLI menu, just run `python -m lib.cli`


## Conclusion

This project demonstrates a practical approach to managing a blog in a command-line environment. It leverages strong data models, built-in data validation, and database relationships to maintain data integrity. It’s perfect for scenarios where a lightweight, low-resource blog management tool is needed.

## Resources

- [Tullier-Blog-CLI-Project Git Repo](https://github.com/Silva-NK/Tullier-Blog-CLI-Project)