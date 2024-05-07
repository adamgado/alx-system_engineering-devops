#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit"""
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
    try:
        a = r.json()
        if r.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    a = a.get("data")
    after = a.get("after")
    count += a.get("dist")
    for x in a.get("children"):
        title = x.get("data").get("title").lower().split()
        for w in word_list:
            if w.lower() in title:
                times = len([t for t in title if t == w.lower()])
                if instances.get(w) is None:
                    instances[w] = times
                else:
                    instances[w] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
