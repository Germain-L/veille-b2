from flask import Flask, render_template, request
import json
import re

app = Flask(__name__)


def open_reddit() -> list:
    with open('data/output_reddit.json', 'r') as reddit_file:
        data = reddit_file.read()
        data = json.loads(data)

        return data


def open_rss() -> list:
    with open('data/output_rss.json', 'r') as rss_file:
        data = rss_file.read()
        data = json.loads(data)

        return data


# only route available
@app.route("/")
@app.route("/rss")
@app.route("/reddit")
def index():
    # get args from url
    # in the form of /?search=query
    search = request.args.get('search')

    route = request.path
    print(route)

    if route == "/reddit":
        data = open_reddit()
    elif route == "/rss":
        data = open_rss()
    else:
        data = open_reddit() + open_rss()

    # if no arguments, render with all data
    if not search:
        return render_template('index.html', json=data, length=len(data), route=request.path)

    # create empty list of articles
    found_articles = []

    search = search.split(" ")

    # iterate over each article in data
    for article in data:
        for arg in search:
            # search in title, url and description
            find_in_title = re.search(arg, article["title"])
            find_in_url = re.search(arg, article["url"])
            find_in_description = re.search(arg, article["description"])

            # if at least one match, add the article to `found_articles`
            if find_in_title or find_in_description or find_in_url:
                found_articles.append(article)

    # render with `found_articles``
    return render_template('index.html', json=found_articles, length=len(found_articles), route=request.path)


# run the app
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
