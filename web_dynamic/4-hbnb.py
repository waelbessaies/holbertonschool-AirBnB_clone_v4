#!/usr/bin/python3
""" Starts Flak"""
from uuid import uuid4
from models import storage
from models.state import State
from os import environ
from models.place import Place
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove Session """
    storage.close()


@app.route('/4-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('4-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid.uuid4())




if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
