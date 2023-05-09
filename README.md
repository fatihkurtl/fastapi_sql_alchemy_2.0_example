# FastAPI SQLAlchemy 2.0 Example

This is a simple example project that demonstrates how to use FastAPI with SQLAlchemy 2.0.

## Features

- A RESTful API for creating an admin user
- A SQLite database with SQLAlchemy 2.0 ORM
- A uvicorn server with gunicorn
- A poetry dependency manager

## Installation

To install this project, you need to have Python 3.6 or higher and poetry installed on your system. Then follow these steps:

- Clone this repository: `git clone https://github.com/fatihkurtl/fastapi_sql_alchemy_2.0_example.git`
- Enter the project directory: `cd fastapi_sql_alchemy_2.0_example`
- Install the dependencies: `poetry install`
- Activate the virtual environment: `poetry shell`

## Usage

To run this project, follow these steps:

- Create the database tables: `python models.py`
- Start the server: `uvicorn api.main:app --reload`
- Open your browser and go to http://localhost:8000/docs to see the API documentation

You can also test the API using curl or any other HTTP client. For example:

- To create an admin user: `curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://localhost:8000/admin/`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
