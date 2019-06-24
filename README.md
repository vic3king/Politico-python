# Politico python version is a spin off of my initial project Politico. This Project rebuilds the backend application with new technologies.

* [Politico-React](https://github.com/vic3king/Politico-React) - Frontend Application of the politico application. Built with React
* [Politico-Api-Node-Version](https://github.com/vic3king/politico) - Initial version of the politico application. Built with Javascript

## Features
* Users can sign up.


## API Documentation
- To view docs follow the setup steps for the application
- visit localhost/politico on you browser
- docs would be on the top right corner

## Requirements and Installation
**Via Cloning The Repository**
```
# Clone the app
git clone https://github.com/vic3king/Politico-python.git

# Setup Env
Follow the format specified in the .env example

# Switch to directory
cd Politico-python

# Install Package dependencies
pipenv install

# Run migrations
alembic init
alembic stamp head
alembic upgrade head

#Start the application
python3 manage.py runserver

#View the application
navigate to localhost:3000 to view the application
```
## Testing
```
$ coming soon
```

## Technologies 

### Backend

* [Python-Flask](http://flask.pocoo.org/) Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [GraphQl](https://graphql.org/) GraphQL is a new API standard that provides a more efficient, powerful and flexible alternative to REST.
* [SQLAlchemy](https://www.sqlalchemy.org/) SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
* [Alembic](https://alembic.sqlalchemy.org) Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.


#### Linter(s)

* [pep8](https://eslint.org/) - Linter Tool

### Style Guide
* coming soon

## Pivotal Tracker

Project is currently being managed with Pivotal Tracker, a project management tool. You can find the stories on the [politico Pivotal Tracker Board](https://www.pivotaltracker.com/n/projects/2238799)

## Authors

* **Akaniru victory** - *Initial work* - [Vic3king](https://github.com/vic3king)

See also the list of [contributors](https://github.com/vic3king/politico/settings/collaboration) who participated in this project.

