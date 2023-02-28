#!/usr/bin/python3
"""
Using reddit's API
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returning top ten post titles recursively"""
    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    arg = {'after': after}
    response = requests.get(url, params=arg, headers=headers)
    list_after = response.json().get("data").get("after")
    titles = response.json().get("data").get("children")

    if list_after:
        if titles:
            for i in titles:
                hot_list.append(i.get("data").get("title"))
        if list_after:
            recurse(subreddit, hot_list, list_after)
        return hot_list
    else:
        return (None)
