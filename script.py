import json
import io
import sys
import re

file_name = sys.argv[1]
feed_type = sys.argv[2]


def clean_url(url):
    urlsub = url.find('url=')
    ct = url.find("&ct")
    return url[urlsub+4:ct]


def rss():
    with io.open(file_name, mode="r", encoding="utf-8") as f:
        data = json.load(f)
        messages = []

        for message in data["messages"]:
            for embed in message["embeds"]:
                clean_url(embed["url"])
                new_article = {
                    'title': embed["title"],
                    'url': clean_url(embed["url"]),
                    'description': embed["description"]
                }
                messages.append(new_article)

        f.close()

    messages.reverse()

    out = io.open('data\output_rss.json', mode="w", encoding="utf-8")
    out.write(json.dumps(messages, indent=4))


def reddit():
    with io.open(file_name, mode="r", encoding="utf-8") as f:
        data = json.load(f)
        messages = []
        for message in data["messages"]:
            for embed in message["embeds"]:
                new_article = {
                    'title': embed["author"]["name"],
                    'url': embed["author"]["url"],
                    'description': embed["description"]
                }
                messages.append(new_article)

        f.close()

    messages.reverse()

    out = io.open('data\output_reddit.json', mode="w", encoding="utf-8")
    out.write(json.dumps(messages, indent=4))


if feed_type not in ("reddit", "rss"):
    print("Wrong feed type, only reddit or rss")

elif feed_type == "reddit":
    reddit()
elif feed_type == "rss":
    rss()
