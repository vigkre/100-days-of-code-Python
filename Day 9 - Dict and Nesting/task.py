# Nesting a List inside a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

# Nesting Lists inside other Lists
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# Nesting a Dictionary inside a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

print(travel_log["Germany"]["cities_visited"][2])
