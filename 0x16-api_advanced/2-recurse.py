#!/usr/bin/python3
"""A module that return the first 10 hot posts"""
import requests

def recurse(subreddit, hot_list=[], count=0, after=None):
    """Return a list of all hot articles"""
    headers = {'X-Modhash': 'Alx student subscribers', 'User-Agent': 'Alx subscriber task v1.01'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if count == 0:
        params = {'limit': 1, 'count':0}
    else:
        params = {'limit': 1, 'after': after, 'count': count}

    resp = requests.get(url, headers=headers, params=params)
    if count == 0 and resp.status_code != 200:
        return None
    after = resp.json()['data']['after']
    if count != 0 and after == None:
        return hot_list
    hot_list.append(resp.json()['data']['children'][0]['data']['title'])
    return recurse(subreddit, hot_list, count + 1, after)
