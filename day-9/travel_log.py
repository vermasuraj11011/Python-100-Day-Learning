travel_log = [
    {
        "country": "India",
        "visits": 11,
        "cities": ["Delhi", "Indore", "Bhopal", "Mathura"]
    },
    {
        "country": "USA",
        "visits": 2,
        "cities": ["LA", "NY"]
    }
]


def addTravelLog(country, visits, cities):
    new_entry = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_entry)
    print(travel_log)


cities_list = ["London", "Manchister"]
addTravelLog("UK", 3, cities_list)
