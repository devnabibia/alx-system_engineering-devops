#!/usr/bin/python3

"""
importing requests module
"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    """

    params = {'show': 'all'}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                  after)

    response = get(url, headers=user_agent, params=params)

    if (response.status_code != 200):
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in sub_info.json()
                        .get("data")
                        .get("children")]

    info = sub_info.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))