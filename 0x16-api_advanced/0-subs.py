#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import sys
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers
    """
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {
            'User-Agent': 'Google Chrome Version 110.0.5481.177'}
        response = requests.get(url, headers=headers).json()
        return response.get('data').get('subscribers')
    except Exception:
        return 0
