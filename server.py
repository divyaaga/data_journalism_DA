# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
from data.format_data import dictionary 
import json


app = Flask(__name__, static_url_path='', static_folder='static')

with open("data/data.json") as f:
    crash_data = json.load(f)

@app.route('/')
def index():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    
    bronx_endpoints = []
    brooklyn_endpoints = []
    manhattan_endpoints = []
    queens_endpoints = []
    staten_island_endpoints = []


    years = sorted([int(y) for y in data["Bronx"].keys()])

    for i in range(len(years) - 1):
        year1 = str(years[i])
        year2 = str(years[i + 1])

        bronx_y1 = float(data["Bronx"][year1])
        bronx_y2 = float(data["Bronx"][year2])
        bronx_endpoints.append([bronx_y1, bronx_y2])

        brooklyn_y1 = float(data["Brooklyn"][year1])
        brookyln_y2 = float(data["Brooklyn"][year2])
        brooklyn_endpoints.append([brooklyn_y1, brookyln_y2])

        manhattan_y1 = float(data["Manhattan"][year1])
        manhattan_y2 = float(data["Manhattan"][year2])
        manhattan_endpoints.append([manhattan_y1, manhattan_y2])

        queens_y1 = float(data["Queens"][year1])
        queens_y2 = float(data["Queens"][year2])
        queens_endpoints.append([queens_y1, queens_y2])

        staten_island_y1 = float(data["Staten Island"][year1])
        staten_island_y2 = float(data["Staten Island"][year2])
        staten_island_endpoints.append([staten_island_y1, staten_island_y2])

        
    return render_template("index.html" )
    print (data)

app.run(debug=True)