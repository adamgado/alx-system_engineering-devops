#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
  """Fetches the subscriber count of a given subreddit using the Reddit API.

  Args:
    subreddit_name: The name of the subreddit.

  Returns:
    The number of subscribers for the subreddit, or None if an error occurs.
  """

  url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    return data['data']['subscribers']
  else:
    return 0
