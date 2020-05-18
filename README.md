# flask_mega_tutorial

**set up and first commit**

 - echo "# flask_mega_tutorial" >> README.md
 - git init
 - git add README.md
 - git commit -m "first commit"
 - git remote add origin https://github.com/rmania/flask_mega_tutorial.git
In order to avoid annoying required username password when pushing
 - git remote set-url origin git+ssh://git@github.com/rmania/ml_deployment.git
 - git push -u origin master

Ch4 Key concepts:
**flask-sqlalchemy** Flask-friendly wrapper to the popular SQLAlchemy package, which is an Object Relational Mapper or 
ORM. ORMs allow applications to manage a database using high-level 
entities such as classes, objects and methods instead of tables and SQL. The job of the ORM is to translate the 
high-level operations into database commands. 
**flask-migrate** Flask wrapper for Alembic, a database migration framework for SQLAlchemy
**https://ondras.zarovi.cz/sql/demo/** a SQL designer tool to make diagrams. 
**Migratation Repository** using ##Alembic** a lightweight database migration tool for usage with the SQLAlchemy 
Database Toolkit for Python (https://alembic.sqlalchemy.org/en/latest/)

Ch13 Key concepts:
Internationalization and Localization, commonly abbreviated I18n and L10n. 
**Flask-Babel** is an extension to Flask that adds i18n and l10n support to any Flask application with the
 help of babel, pytz and speaklater. https://pythonhosted.org/Flask-Babel/
Adding `_()` and `_l()` wrapper objects in the html code to render translations pybabel command to 
extract them to a .pot file (portable object template). this generates a Language Catalog.
Create `flask translate init <language-code>` , `flask translate update` and `flask translate compile` 
sub-commands with a new `cli.py` file (relying on click module)
 
 


