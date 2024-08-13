#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """returns a list containing the titles of all hot articles"""
    lnk = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(lnk, headers={"User-Agent": "simplemitten"},
                       params={"after": after, "count": count, "limit": 10},
                       allow_redirects=False)
    if req.status_code != 200:
        return None
    result = req.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for a in results.get("children"):
        hot_list.append(a.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, next, count)
    return hot_list
