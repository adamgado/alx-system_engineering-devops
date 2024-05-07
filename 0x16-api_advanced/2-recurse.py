#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], next_one="", nb=0):
    """returns a list containing the titles of all hot articles for a given subreddit"""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/edev_)"
    }
    prm = {
        "after": after,
        "count": count,
        "limit": 100
    }
    r = requests.get(link, headers=headers, params=prm,
                            allow_redirects=False)
    if r.status_code == 404:
        return None

    a = r.json().get("data")
    next_one = a.get("after")
    nb += a.get("dist")
    for x in a.get("children"):
        hot_list.append(x.get("data").get("title"))

    if next_one is not None:
        return recurse(subreddit, hot_list, next_one, nb)
    return hot_list
