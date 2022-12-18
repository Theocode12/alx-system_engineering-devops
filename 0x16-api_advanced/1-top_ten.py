#!/usr/bin/python3
"""A module that return the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """Return the top 10 hot posts"""
    headers = {'X-Modhash': 'Alx student subscribers',
               'User-Agent': 'Alx subscriber task v1.01'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 10}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code != 200:
        print('None')
        return
    children = resp.json()['data']['children']
    for child in children:
        print(child['data']['title'])
