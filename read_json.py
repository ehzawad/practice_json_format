import json

file_path = 'data_proces.json'
print(file_path)

with open(file_path, 'r', encoding='utf8') as f:
    data = json.load(f)

print(type(data))
# print(data['intents'])

for i in data['intents']:
    for j in data['intents'][i]['utterances']:
        print(j['data'])
