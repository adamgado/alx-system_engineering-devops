#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed"""
    lnk = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(lnk, headers={"User-Agent": "simplemitten"}
                       ,params={"limit": 10}, allow_redirects=False)
    if req.status_code != 404:
        result = req.json().get("data")
        for a in results.get("children"):
            print(a.get("data").get("title"))
    else:
        print("None")
