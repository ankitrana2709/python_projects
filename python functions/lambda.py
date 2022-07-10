people = [
    {"name":"Harry", "house": "Gryffindor"},
    {"name":"ank", "house":"rana niwas"}
]


people.sort(key=lambda person: person["name"])
print(people)