import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precip():
    """Return a list of precipitation data for 2016"""
    # Query precipitation data for 2016
    precip_results = session.query(measurements.date,measurements.prcp).\
    filter(func.strftime("%Y", measurements.date) == "2016").\
    group_by(measurements.prcp).\
    order_by(measurements.date).all()

    # Convert list of tuples into normal list
    precip = list(np.ravel(precip_results))
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def station():
    """Return a list of all station names"""
    # Query station names
    station_results = session.query(stations.name).\
    order_by(stations.name).all()

    # Convert list of tuples into normal list
    station = list(np.ravel(station_results))
    return jsonify(station)

@app.route("/api/v1.0/tobs")
def tobs():
        """Return a list of temperature data"""
    tobs_results = session.query(measurements.date,measurements.tobs).\
    filter(func.strftime("%Y", measurements.date) == "2016").\
    group_by(measurements.tobs).\
    order_by(measurements.date).all()

    # Convert list of tuples into normal list
    precip = list(np.ravel(tobs_results))
    return jsonify(precip)
   
@app.route("/api/v1.0/<start>")
def start():
   
@app.route('/api/v1.0/start/end')
def end():
   

if __name__ == '__main__':
    app.run(debug=True)
