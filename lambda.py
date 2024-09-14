
people = [
    {"name" : "Hope", "Home": "Narok"},
    {"name":"Aleks", "Home": "Nakuru"}
]

# There are two ways this boject can be sorted

# 1. using function

def f(people):
    return people["name"]

people.sort(key=f)

print(people)

# 2.Lambda

people.sort(key= lambda person: person["name"])

print(people)
