# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json

# app_id = '<my app_id>'
app_id = '22472a3a'
# app_key = '<my app_key>'
app_key = '974f6f66e3a9615a98a83be197c02346'
language = "en-us"
word_id = "betray"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
myresultJson = (r.text)
# print(type(myresultJson))
# print((myresultJson))

jsonDict = json.loads(myresultJson)

# print(type(jsonDict))
# print(jsonDict)

myresult = jsonDict["results"]

# print(type(myresult))

# print(myresult[0])
myresult_dictionary = myresult[0]
# print(type(myresult_dictionary))

# for replies_data in myresult_dictionary:
#     print(replies_data)


lexicon = myresult_dictionary["lexicalEntries"]
# print(lexicon)
# print(type(lexicon))
#
# print(len(lexicon))

lexicon_parse = lexicon[0]

# print(type(lexicon_parse))
# print(lexicon_parse)

word_derivatives = lexicon_parse["entries"]
# print(type(word_derivatives))
# print(len(word_derivatives))

contents_of_entries = word_derivatives[0]

all_senses = contents_of_entries["senses"]

# print(all_senses[0])

# print(type(all_senses))
# print(len(all_senses))

first_sense = all_senses[0]
short_definition_of_first_sense = first_sense["shortDefinitions"]
synonyms_list_of_first_definition = first_sense["subsenses"]

# print(synonyms_list_of_first_definition)
print(len(synonyms_list_of_first_definition))
print(type(synonyms_list_of_first_definition))


synonyms_list_ = synonyms_list_of_first_definition

for s in synonyms_list_:
    print(s)
