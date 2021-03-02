import json

# some dictionaries
shekar = { "name":"Shekar", "age":16, "birthplace":"San Diego", "height":69}
vinod = { "name":"Vinod", "age":19, "birthplace":"New Jersey", "height":69}
lalitha = { "name":"Lalitha", "age":50, "birthplace":"Chennai", "height":62}
ashok = { "name":"Ashok", "age":56, "birthplace":"Chennai", "height":66}

# a list of dictionaries
list_of_family = [shekar, vinod, lalitha, ashok]
# write some code to Print List of people one by one
print("List of family members:")
#print(type(list_of_family))
print(list_of_family)
print("Individual family members")
for person in list_of_family:
    print(person['name'] + "," + str(person['age']) + "," + person['birthplace'] + "," + str(person['height']))
print()

# turn list to dictionary of family
family = {'people': list_of_family}
print(family)
print("Dictionary of family:")
# write some code to Print Family from Dictionary-
# INSERT CODE HERE
dictionary_list_of_family = family['people']
print(dictionary_list_of_family)
print()

# turn dictionary to JSON
json_family = json.dumps(dictionary_list_of_family)
print("JSON family file")
print(json_family)
print(family)
# write some code to print a space between each character of JSON
# INSERT CODE HERE
for char in json_family:
    print(char, end ="_")
print()


# the result is a JSON file:
print()
print(json_family)
family = json.loads(json_family)


Nirmala = { "name":"Nirmala", "age":80, "birthplace":"India", "height":60}
Meenakshi = { "name":"Meenakshi", "age":88, "birthplace":"India", "height":65}
list_of_grandparents = [Nirmala, Meenakshi]
grandparents={'adults': list_of_grandparents}
dictionary_list_of_grandparents = grandparents['adults']
json_grandparents=json.dumps(dictionary_list_of_grandparents)
print(json_grandparents)





