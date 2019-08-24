import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import pandas as pd
import numpy as np
from flask import Flask
app = Flask(__name__)

@app.route("/")
def data():
    return render_template('data.html')

@app.route('/display_city_data')
def display_data():
    df = pd.read_csv("db/CHDB_data_city_all v6_0.csv")
    df_dict= df.to_dict('records')
    resp = jsonify(df_dict)
    return resp


@app.route("/line")
def test():
    data = [{
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 4, 8, 16]}]

    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)