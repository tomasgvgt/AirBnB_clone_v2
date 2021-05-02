#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
To load all cities of a State:
    If your storage engine is DBStorage, you must use cities relationship
    Otherwise, use the public getter method cities
After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
Routes:
    /states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
            LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
            H1 tag: “State: ”
            H3 tag: “Cities:”
            UL tag: with the list of City objects linked to the State
                LI tag: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
            H1 tag: “Not found!”

"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """display html page with all states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda s: s.name)
    return render_templates('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state():
    """ display html page with cities for that state"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda s: s.name)
    for state in states:
        if state.id = id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown_appcontext(error):
    """teardown"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
