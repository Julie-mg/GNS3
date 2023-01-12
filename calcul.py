import json
import re

#Opening JSON file
with open('config.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

print(json_object['AS1']['routeurs'])

for routeur in json_object['AS1']['routeurs']:
	for connection in json_object['AS1']['connections']:
		if routeur in connection:
			num_connection_list = re.findall('\d+',connection)
			print(routeur,num_connection_list)