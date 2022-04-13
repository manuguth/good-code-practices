cities = {"London", "Paris", "Bern"}  # Unordered collection


def get_new_cities():
    new_cities = []
    new_cities.append("Oslo")
    new_cities.append("Praque")
    return set(new_cities)

cities.union(get_new_cities())

print(cities)  # Does not include Oslo, Praque!
