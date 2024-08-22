import pandas






































# # Create a csv file with data on Squirrel count with their Fur color

# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# # gray_fur_color_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count()
# # black_fur_color_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]["Primary Fur Color"].count()
# # cinnamon_fur_color_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].count()

# gray_fur_color_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# black_fur_color_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
# cinnamon_fur_color_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

# squirrel_data_dict = {
#     "Fur Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [gray_fur_color_data, black_fur_color_data, cinnamon_fur_color_data]
# }

# squirrel_count_csv = pandas.DataFrame(squirrel_data_dict)
# squirrel_count_csv.to_csv("squirrel_count.csv")



# # Create a dataframe from scratch

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [10, 50, 100]
# }

# tab_data = pandas.DataFrame(data_dict)
# tab_data.to_excel("new_excel.xlsx")


# # Convert Monday's temperature to Fahrenheit

# monday = data[data.day == "Monday"]
# print(monday.temp.get(0) * 9/5 + 32)


# # Print the row where the temperature is MAX

# print(data[data.temp == data.temp.max()])


# # Get the data in Row

# print(data[data.day == "Monday"])


# # Find the average temperature 

# temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)

# print(round(average))


# # Get the column data

# print(data['temp'])


# # Using CSV module to access csv data from file

# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)