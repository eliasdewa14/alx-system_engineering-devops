#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import sys
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers
    """
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
        response = requests.get(url, headers=headers, allow_redirects=False)
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
