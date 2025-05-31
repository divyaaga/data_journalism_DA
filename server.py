# flask --app data_server run
#ASK ABOUT THE UNCLEAN DATA IS IT NECESSARY 
#DIVYA REMEMBER 
from flask import Flask
from flask import render_template
from flask import request
from data.format_data import dictionary 
import json


app = Flask(__name__, static_url_path='', static_folder='static')

with open("data/data.json") as f:
    crash_data = json.load(f)

@app.route('/')
def about():
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()

    year_list = []
    for k in data["Bronx"]: 
        this_year = k 
        year_list.append(this_year)

    return render_template("about.html", year_list = year_list)

@app.route('/index')
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

    year_list = []
    for k in data["Bronx"]: 
        this_year = k 
        year_list.append(this_year)

    return render_template(
    "index.html",
    bronx_endpoints=bronx_endpoints,
    brooklyn_endpoints=brooklyn_endpoints,
    manhattan_endpoints=manhattan_endpoints,
    queens_endpoints=queens_endpoints,
    staten_island_endpoints=staten_island_endpoints,
    years=years,
    year_list = year_list 
    )

@app.route('/year')
def year(): 
    f = open("data/data.json", "r")
    data = json.load(f)
    f.close()
    requested_year = request.args.get("year")
    print ("we've reached year")
    bronx_value = float(data["Bronx"][str(requested_year)])
    brooklyn_value = float(data["Brooklyn"][str(requested_year)])
    manhattan_value = float(data["Manhattan"][str(requested_year)]) 
    queens_value = float(data["Queens"][str(requested_year)]) 
    staten_island_value = float(data["Staten Island"][str(requested_year)]) 

    year_list = []
    for k in data["Bronx"]: 
        this_year = k 
        year_list.append(this_year)
    
    values = [bronx_value, brooklyn_value, manhattan_value, queens_value, staten_island_value]
    average = int(sum(values) / len(values)) 

    return render_template(
        "year.html",
        year=requested_year,
        bronx_value=int(bronx_value),
        brooklyn_value=int(brooklyn_value),
        manhattan_value=int(manhattan_value),
        queens_value=int(queens_value),
        staten_island_value=int(staten_island_value),
        bronx_scaled = 100 - int((bronx_value / 52000) * 100),
        brooklyn_scaled = 100 - int((brooklyn_value / 52000) * 100),
        manhattan_scaled = 100 - int((manhattan_value / 52000) * 100),
        queens_scaled = 100 - int((queens_value / 52000) * 100),
        staten_island_scaled = 100 - int((staten_island_value / 52000) * 100),
        year_list = year_list,
        average = average
    )

app.run(debug=True)