from re import S
from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)

# read file
with open('./data/output.json', 'r') as myfile:
    data = myfile.read()
    data = json.loads(data)


@app.route("/")
def index():
    search = request.args.get('search')

    if not search:
        return render_template('index.html', json=data, length=len(data))

    found = []
    for article in data:

        findInTitle = re.search(search, article["title"])
        findInUrl = re.search(search, article["url"])
        findInDescription = re.search(search, article["description"])

        if findInTitle or findInDescription or findInUrl:
            found.append(article)

    return render_template('index.html', json=found, length=len(found))


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
