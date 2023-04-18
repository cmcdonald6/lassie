import lassie
import json

val = input("Enter a url: ")
info = lassie.fetch(val)

json_object = json.dumps(info, indent = 4)
print(json_object)

with open('result.json', 'w') as fp:
    json.dump(json_object, fp)