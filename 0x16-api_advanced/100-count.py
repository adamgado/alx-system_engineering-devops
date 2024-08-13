#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def count_words(subreddit, word_list, count=0, after="", instances={}):
    """prints a sorted count of given keywords"""
    lnk = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(lnk, headers={"User-Agent": "simplemitten"},
                       params={"after": after, "count": count, "limit": 100},
                       allow_redirects=False)
    try:
        results = req.json().get("data")
        if req.status_code != 200:
            raise Exception
    except Exception:
        print("")
        return
    after = results.get("after")
    count += results.get("dist")
    for a in results.get("children"):
        title = a.get("data").get("title").lower().split()
        for b in word_list:
            if b.lower() in title:
                num = len([c for c in title if c == b.lower()])
                if instances.get(b) is None:
                    instances[b] = num
                else:
                    instances[b] += num
    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(key, value)) for key, value in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
