import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_color = data["Primary Fur Color"]

dict_squirrel = {
    "Fur Color": [],
    "Count": []
}

for color in data_color:
    if (not dict_squirrel["Fur Color"].__contains__(color)) and (color is not None):
        dict_squirrel["Fur Color"].append(color)
        dict_squirrel["Count"].append(1)
    else:
        dict_squirrel["Count"][dict_squirrel["Fur Color"].index(color)] += 1

pandas.DataFrame(dict_squirrel).to_csv("squirrel_count.csv")
