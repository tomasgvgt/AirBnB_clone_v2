#!/usr/bin/python3
"""
 script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present
                    in DBStorage sorted by name (A->Z)
                LI tag: description of one State:
                    <state.id>: <B><state.name></B>
    Import this 7-dump to have some data
    You must use the option strict_slashes=False in your route definition

"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    states = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext(error):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
