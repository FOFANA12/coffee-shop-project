import json
import click
from flask.cli import with_appcontext
from .database.models import Drink, db

# data
feekData = [
    {
        "title": 'Matcha shake',
        "recipe": [
            {"name": "milk", "color": "grey", "parts": 1},
            {"name": "matcha", "color": "green", "parts": 3}
        ],
    },
    {
        "title": 'Flatwhite',
        "recipe": [
            {"name": "milk", "color": "grey", "parts": 3},
            {"name": "coffee", "color": "brown", "parts": 1}
        ],
    },
    {
        "title": 'Cap',
        "recipe": [
            {"name": "foam", "color": "white", "parts": 1},
            {"name": "milk", "color": "grey", "parts": 2},
            {"name": "coffee", "color": "brown", "parts": 3}
        ],
    },
    {
        "title": 'Coffee',
        "recipe": [{"name": "coffee", "color": "brown", "parts": 1}],
    },
    {
        "title": 'Water',
        "recipe": [{"name": "Water", "color": "blue", "parts": 1}],
    },

]

# create command function


@click.command(name='init_data')
@with_appcontext
def init_data():
    try:
        db.drop_all()
        db.create_all()

        for data in feekData:
            drink = Drink(
                title=data['title'],
                recipe=json.dumps(data['recipe'])
            )
            drink.insert()
    except:
        db.session.rollback()
    finally:
        db.session.close()
