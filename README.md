# Tullier Blog CLI Project

## Introduction

Tullier BLOG CLI is a blog manager that seeks to easily run and manage a small scale blog where memeber of Tullier can share thoughts, ideas and other important message and information. It manages users, posts and categories directly from the command line terminal, no need for a browser or web-server and perfect for small-scale, limited resource use. 

It utilises SQLITE database and a modular, OOP-based design to ensure a simple, clean and fast way to manage internal blog content.


### Project Map
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── db
    │   ├── migrations
    │   │      ├── versions
    │   │      ├── README.md
    │   │      ├── env.py
    │   │      └── script.py.mako
    │   ├── alembic.ini
    │   ├── models.py
    │   └── seed.py
    ├── cli.py
    ├── debug.py
    └── helpers.py




### Removing Existing Git Configuration



### Creating Your Own Git Repo



## Generating Your Pipenv



## Generating Your Database



## Generating Your CLI



## Updating Your README.md



### What Goes into a README?



## Conclusion

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

## Resources

- [Tullier-Blog-CLI-Project Git Repo](https://github.com/Silva-NK/Tullier-Blog-CLI-Project)
