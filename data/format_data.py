import json


f1 = open("data/cleaned_crashes.csv", "r")
lines = f1.readlines()
year_keys = lines[1].strip().split(",")[1:] #just to get rid of the other stuff before the years
print (year_keys)
#iteratre through list of lines (lines) 
#split each line into its own list 
# go through that list and create a dictionary with year being the key and left expectancy the value 
dictionary ={}

bronx = lines[2].split(",")[1:]
brooklyn = lines[3].split(",")[1:]
manhattan = lines[4].split(",")[1:]
queens = lines[5].split(",")[1:]
staten_island = lines[6].split(",")[1:]

bronx_dict = {}
brooklyn_dict = {}
manhattan_dict = {}
queens_dict = {}
staten_island_dict = {}


for i in range(len(year_keys)):
    year = year_keys[i]
    value = bronx[i]
    if value:
        bronx_dict[year] = float(value)
    else:
        bronx_dict[year] = None

for i in range(len(year_keys)):
    year = year_keys[i]
    value = brooklyn[i]
    if value:
        brooklyn_dict[year] = float(value)
    else:
        brooklyn_dict[year] = None

for i in range(len(year_keys)):
    year = year_keys[i]
    value = manhattan[i]
    if value:
        manhattan_dict[year] = float(value)
    else:
        manhattan_dict[year] = None

for i in range(len(year_keys)):
    year = year_keys[i]
    value = queens[i]
    if value:
        queens_dict[year] = float(value)
    else:
        queens_dict[year] = None

for i in range(len(year_keys)):
    year = year_keys[i]
    value = staten_island[i]
    if value:
        staten_island_dict[year] = float(value)
    else:
        staten_island_dict[year] = None

dictionary = {
    "Bronx": bronx_dict,
    "Brooklyn": brooklyn_dict,
    "Manhattan": manhattan_dict,
    "Queens": queens_dict,
    "Staten Island": staten_island_dict
}

f1.close()

#Save the json object to a file
f2 = open("data.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
