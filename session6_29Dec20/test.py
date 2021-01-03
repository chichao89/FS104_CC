import json

employee = '{"first_name":"Chi Chao", "last_name":"See"}'
person_dict = json.loads(employee)

print(person_dict)
print(person_dict["last_name"])