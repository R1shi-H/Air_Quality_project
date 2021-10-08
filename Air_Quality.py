import pandas as pd
country_AQI = pd.read_csv (r'C:\Users\r2hal\Downloads\data.csv',index_col=0).to_dict()
#print(country_AQI["Average AQI"]["India"])
print("Welcome to my air quality program! (To quit the program, simply type, exit)")
print("To understand the concept of AQI measurements relating to air quality, the higher the AQI value, the greater the level of air pollution and the greater the health concern. For example, an AQI value of 50 or below represents good air quality, while an AQI value over 300 represents hazardous air quality.")
question = ""
while question != "exit":
    question  = str(input("Which country would you like to learn about?: "))
    if question == "exit":
        break
    if question in country_AQI ["Average AQI"]:
        print("Average AQI in " + question + ": ")
        print(country_AQI["Average AQI"][question])
    else:
        print("Please enter a country within the database.")
        