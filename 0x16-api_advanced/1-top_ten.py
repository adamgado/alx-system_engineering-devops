#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """returns a list containing the titles of all hot articles for a given subreddit"""
    link = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/edev_)"
    }
    prm = {
        "limit": 10
    }
    r = requests.get(link, headers=headers, params=prm,
                            allow_redirects=False)
    if r.status_code == 404:
        print("None")
        return
    a = r.json().get("data")
    [print(x.get("data").get("title")) for x in a.get("children")]
