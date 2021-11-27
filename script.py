import json
import io
import sys

file_name = sys.argv[1]

print(file_name)
# Opening JSON file
f = io.open(file_name, mode="r", encoding="utf-8")

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list

# get all titles
messages = []
# for message in data["messages"]:
#     for embed in message["embeds"]:
#         print(embed["title"])

for message in data["messages"]:
    for embed in message["embeds"]:
        new_article = {
            'title': embed["title"],
            'url': embed["url"],
            'description': embed["description"]
        }
        messages.append(new_article)

# Closing file
f.close()

out = io.open('data\output.json', mode="w", encoding="utf-8")
out.write(json.dumps(messages, indent=4))
