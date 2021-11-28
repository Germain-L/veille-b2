from re import S
from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)

# read data file
with open('./data/output.json', 'r') as myfile:
    data = myfile.read()
    data = json.loads(data)

# only route available
@app.route("/")
def index():
    
    # get args from url
    # in the form of /?search=query
    search = request.args.get('search')

    # if no arguments, render with all data
    if not search:
        return render_template('index.html', json=data, length=len(data))

    # create empty list of articles
    foundArticles = []
    
    # iterate over each article in data
    for article in data:

        # search in title, url and description 
        findInTitle = re.search(search, article["title"])
        findInUrl = re.search(search, article["url"])
        findInDescription = re.search(search, article["description"])
        
        # if at least one match, add the article to `foundArticles`
        if findInTitle or findInDescription or findInUrl:
            foundArticles.append(article)

    # render with `foundArticles``
    return render_template('index.html', json=foundArticles, length=len(foundArticles))


# run the app
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
