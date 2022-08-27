
# Backend - Coffee Shop API

This API is part of my training on UDACITY, and allows students to place coffee orders.

The purpose of this application is to enable learners to have practical skills to configure and secure APIs.

#### The functionalities covered by the API are :

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.


## Getting started
To work with this project, you must know python precisely the FLASK framework

### Configuration for local development

#### Install depencies

1. **Python >= 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `api.py`and can reference `database/models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) is used for managing database migrations.

### Set up the Database

Using the Postgres command line to create a `coffee_shop` database by running the following command:

```bash
CREATE DATABASE coffee_shop
```

With the following commands, run migration and initialize database with test data:

```bash
flask db init
flask db migrate
flask db upgrade

flask init_data
```

### Update configurations

Connected to your Auth0 account to create your application and then your API, you create two roles: Barista and Manager.

assign the following permissions to roles

Barista : get:drinks-detail
Manager : get:drinks-detail, post:drinks, patch:drinks, delete:drinks

You have the application configurations in the .env file inside the backend folder. Adapt it to your case.

### Run the Server

First ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

Default URL should be http://127.0.0.1:5000/

### Testing
Tests are not required to run the API. But if you contribute, please run the tests before pushing to GitHub.

In this project, Postman is used to test the endpoints. You can download it from this link: https://www.postman.com/downloads.

You connect as Barista to get his token, repeat this process to get another token for Manager.

In the backend folder you have the Postman collection file named "udacity-fsnd-udaspicelatte.postman_collection.json" imported into the Postman.

Before trying to run the tests make sure you have changed the url, if you are not using the default base url, and tokens

Becarefull of PATCH and DELETE tests:

if the tests don't pass, make sure the ID given in the url exists in the database.

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
- Authentication: This the application require authentication and permissions for some actions.

### Error Handling
All HTTP errors are handled and returned as JSON objects in the following format:

```bash
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

#### Endpoints

#### Get drinks
```http
  GET /drinks
```
- General: returns the short representation of drinks, success value.
- Permissions: not require
- Sample: ```bash curl http://127.0.0.1:5000/drinks ```

```bash
  {
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "grey",
                    "parts": 1
                },
                {
                    "color": "green",
                    "parts": 3
                }
            ],
            "title": "Matcha shake"
        },
        {
            "id": 2,
            "recipe": [
                {
                    "color": "grey",
                    "parts": 3
                },
                {
                    "color": "brown",
                    "parts": 1
                }
            ],
            "title": "Flatwhite"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "white",
                    "parts": 1
                },
                {
                    "color": "grey",
                    "parts": 2
                },
                {
                    "color": "brown",
                    "parts": 3
                }
            ],
            "title": "Cap"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "brown",
                    "parts": 1
                }
            ],
            "title": "Coffee"
        },
        {
            "id": 5,
            "recipe": [
                {
                    "color": "blue",
                    "parts": 1
                }
            ],
            "title": "Water"
        }
    ],
    "success": true
}
```

#### Get drinks details
```http
  GET /drinks-detail
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**. Your authentication token |

- General: returns the long representation of drinks, success value.
- Permissions: this action require the following permission : `get:drinks-detail`
- Sample: `curl -H "Authorization: Bearer {token}" http://127.0.0.1:5000/drinks-detail `

```bash
  {
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 1
                },
                {
                    "color": "green",
                    "name": "matcha",
                    "parts": 3
                }
            ],
            "title": "Matcha shake"
        },
        {
            "id": 2,
            "recipe": [
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 3
                },
                {
                    "color": "brown",
                    "name": "coffee",
                    "parts": 1
                }
            ],
            "title": "Flatwhite"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "white",
                    "name": "foam",
                    "parts": 1
                },
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 2
                },
                {
                    "color": "brown",
                    "name": "coffee",
                    "parts": 3
                }
            ],
            "title": "Cap"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "brown",
                    "name": "coffee",
                    "parts": 1
                }
            ],
            "title": "Coffee"
        },
        {
            "id": 5,
            "recipe": [
                {
                    "color": "blue",
                    "name": "Water",
                    "parts": 1
                }
            ],
            "title": "Water"
        }
    ],
    "success": true
}
```

#### Create drink

```http
  POST /drinks
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Name of drink |
| `recipe`      | `list of json object` | **Required**. Recipe of drink |
| `token`      | `string` | **Required**. Your authentication token |

- General: Create a new drink using the submitted info, if title not exist. Returns a list with long representation of created drink and success value. 
- Permissions: this action require the following permission : `post:drinks`
- Sample: `curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {token}" -d '{"title": "Water3", "recipe": [{"name": "Water", "color": "blue", "parts": 1}]}' http://127.0.0.1:5000/drinks`
```bash
{
    "drinks": [
        {
            "id": 6,
            "recipe": [
                {
                    "color": "blue",
                    "parts": 1
                }
            ],
            "title": "Water3"
        }
    ],
    "success": true
}
```

#### Update drink

```http
  PATCH /drinks/{drink_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `drink_id`      | `int` | **Required**. Id of drink |
| `title`      | `string` | **Oprtional**. Name of drink |
| `recipe`      | `list of json object` | **Oprtional**. Recipe of drink |
| `token`      | `string` | **Required**. Your authentication token |

- General: Updates drink whose ID is passed in the URL using the submitted info. Returns a list with long representation of updated drink and success value. 
- Permissions: this action require the following permission : `patch:drinks`
- Sample: `curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer {token}" -d '{"title": "Water5"}' http://127.0.0.1:5000/drinks/1`
```bash
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "grey",
                    "name": "milk",
                    "parts": 1
                },
                {
                    "color": "green",
                    "name": "matcha",
                    "parts": 3
                }
            ],
            "title": "Water5"
        }
    ],
    "success": true
}
```

#### Delete drink

```http
  DELETE /drinks/{drink_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `drink_id`      | `int` | **Required**. Id of drink to delete |
| `token`      | `string` | **Required**. Your authentication token |

- General: Deletes drink whose ID is passed in the URL. Returns the ID of the deleted drink, success value.
- Permissions: this action require the following permission : `delete:drinks`
- Sample: `curl -X DELETE -H "Authorization: Bearer {token}" http://127.0.0.1:5000/drinks/1`
```bash
{
    "delete": 1,
    "success": true
}
```

## Authors
This project is the result of the work of the Udacity team and me.

The base of the project was made by the Udacity team and I made corrections to make it work

- [Udacity](https://www.udacity.com/)
- [Bakary FOFANA](https://github.com/FOFANA12)

## Acknowledgements

 - [Udacity](https://www.udacity.com/) 