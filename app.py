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
@app.route("/rss")
def rss():
    # get args from url
    # in the form of /?search=query
    search = request.args.get('search')

    data = open_rss()

    # if no arguments, render with all data
    if not search:
        return render_template('index.html', json=data, length=len(data))

    # create empty list of articles
    found_articles = []

    # iterate over each article in data
    for article in data:

        # search in title, url and description
        find_in_title = re.search(search, article["title"])
        find_in_url = re.search(search, article["url"])
        find_in_description = re.search(search, article["description"])

        # if at least one match, add the article to `found_articles`
        if find_in_title or find_in_description or find_in_url:
            found_articles.append(article)

    # render with `found_articles``
    return render_template('index.html', json=found_articles, length=len(found_articles))


@app.route("/reddit")
def reddit():
    # get args from url
    # in the form of /?search=query
    search = request.args.get('search')

    data = open_reddit()

    # if no arguments, render with all data
    if not search:
        return render_template('index.html', json=data, length=len(data))

    # create empty list of articles
    found_articles = []

    # iterate over each article in data
    for article in data:

        # search in title, url and description
        find_in_title = re.search(search, article["title"])
        find_in_url = re.search(search, article["url"])
        find_in_description = re.search(search, article["description"])

        # if at least one match, add the article to `found_articles`
        if find_in_title or find_in_description or find_in_url:
            found_articles.append(article)

    # render with `found_articles``
    return render_template('index.html', json=found_articles, length=len(found_articles))


@app.route("/")
def index():
    # get args from url
    # in the form of /?search=query
    search = request.args.get('search')

    data = open_rss() + open_reddit()

    # if no arguments, render with all data
    if not search:
        return render_template('index.html', json=data, length=len(data))

    # create empty list of articles
    found_articles = []

    # iterate over each article in data
    for article in data:

        # search in title, url and description
        find_in_title = re.search(search, article["title"])
        find_in_url = re.search(search, article["url"])
        find_in_description = re.search(search, article["description"])

        # if at least one match, add the article to `found_articles`
        if find_in_title or find_in_description or find_in_url:
            found_articles.append(article)

    # render with `found_articles``
    return render_template('index.html', json=found_articles, length=len(found_articles))


# run the app
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
