#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    link = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/edev_)"
    }
    r = requests.get(link, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    a = r.json().get("data")
    return a.get("subscribers")
