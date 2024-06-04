#!/usr/bin/python3
"""Querying Reddit"""

import requests


def number_of_subscribers(subreddit):
    """Quering a subreddit and retrieving the no of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User=Agent': 'example.myredditapp:v1.2.3 (by u/Trevor)'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
