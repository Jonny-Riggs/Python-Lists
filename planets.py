planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

print(planet_list)

planet_list_2 = ["Uranus", "Neptune"]

planet_list.extend(planet_list_2)

print(planet_list)

planet_list.insert(2, "Earth")

print(planet_list)

planet_list.insert(1, "Venus")

print(planet_list)

planet_list.append("Pluto")

print(planet_list)

rocky_planets = planet_list[0:9]

print(rocky_planets)

planet_list.remove("Pluto")

print(planet_list)