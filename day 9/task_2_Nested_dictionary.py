capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome"
}

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lyon", "Marseille"],
        "total_visits": 3
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Munich"],
        "total_visits": 3
    },
}

print(travel_log["France"]["cities_visited"][1])