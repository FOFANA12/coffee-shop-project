from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS
from dotenv import load_dotenv
import os

from .seeder import init_data
from .database.models import setup_db, Drink
from .auth.auth import AuthError, requires_auth
from werkzeug.exceptions import HTTPException

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
setup_db(app)
app.cli.add_command(init_data)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers",
                         "Content-Type,Authorization,true")
    response.headers.add("Access-Control-Allow-Methods",
                         "GET,PUT,POST,DELETE,OPTIONS")
    return response


'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one

    The following command initializes the database with some data
'''
# flask init_data

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route("/drinks", methods=["GET"])
def retrieve_drinks():
    drinks = Drink.query.order_by(Drink.id).all()
    return jsonify(
        {
            'success': True,
            'drinks': [drink.short() for drink in drinks]
        }
    ), 200


'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drink_detail(payload):
    drinks = Drink.query.all()

    return jsonify(
        {
            'success': True,
            'drinks': [drink.long() for drink in drinks]
        }
    ), 200


'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route("/drinks", methods=["POST"])
@requires_auth('post:drinks')
def create_drink(payload):
    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)

    if (not title) or (not recipe):
        abort(400)

    try:
        data = json.dumps(recipe)
        drink = Drink(
            title=title,
            recipe=data,
        )
        drink.insert()

        return jsonify(
            {
                "success": True,
                "drinks": [drink.short()],
            }
        ), 200

    except:
        abort(422)


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route("/drinks/<int:drink_id>", methods=["PATCH"])
@requires_auth('patch:drinks')
def update_drink(payload, drink_id):
    drink = Drink.query.get_or_404(drink_id)

    body = request.get_json()
    title = body.get('title', None)
    recipe = body.get('recipe', None)

    try:
        if title:
            drink.title = title
        if recipe:
            drink.recipe = json.dumps(recipe)

        drink.update()

        return jsonify(
            {
                "success": True,
                "drinks": [drink.long()],
            }
        ), 200

    except:
        abort(422)


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route("/drinks/<int:drink_id>", methods=["DELETE"])
@requires_auth('delete:drinks')
def delete_drink(payload, drink_id):
    drink = Drink.query.get_or_404(drink_id)

    try:
        drink.delete()
    except:
        abort(422)

    return jsonify(
        {
            "success": True,
            "delete": drink_id,
        }
    ), 200


# Error Handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTTP errors."""

    return jsonify({
        "success": False,
        "error": e.code,
        "message": e.description,
    })


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code


if __name__ == "__main__":
    app.run()
