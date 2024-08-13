#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    lnk = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(lnk, headers={"User-Agent": "simplemitten"}, allow_redirects=False)
    if req.status_code != 404:
        return req.json().get("data").get("subscribers")
    else:
        return 0
