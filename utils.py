# -*- coding: utf-8 -*-
import facebook


def init(key=None):
    if key is None:
        file = open("keys", "r")
        key = file.read()
        file.close()
    return facebook.GraphAPI(access_token=key, version='2.7')


def remove_posts(graph, posts):
    for post in posts:
        graph.delete_object(post["id"])


def get_whole_feed(graph, target_group_id):
    whole_feed = list()
    posts = graph.get_object(id=str(target_group_id)+'/feed?limit=100')
    while True:
        if "paging" not in posts:
            break

        whole_feed.extend(posts["data"])

        next_page = posts["paging"]["next"]
        next_page = next_page.lstrip("https://graph.facebook.com/v2.7/")
        posts = graph.get_object(next_page)
    return whole_feed
