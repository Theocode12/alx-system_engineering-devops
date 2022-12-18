#!/usr/bin/python3
"""A module that returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    headers = {'X-Modhash': 'Alx student subscribers',
               'User-Agent': 'Alx subscriber task v1.01'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return 0
    return resp.json()['data']['subscribers']
