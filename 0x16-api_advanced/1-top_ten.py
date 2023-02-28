#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    params = {"limit": 10}
    response = requests.get(url, params=params, headers=headers).json()

    try:
        result = response.get('data').get('children')

        for i in result:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
