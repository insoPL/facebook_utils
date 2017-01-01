# -*- coding: utf-8 -*-
from utils import *

graph = init()

whole_feed = list()
posts = graph.get_object(id='561578050704724/feed?limit=10')
while True:
    if "paging" not in posts:
        break

    whole_feed.extend(posts["data"])

    next = posts["paging"]["next"]
    next = next.lstrip("https://graph.facebook.com/v2.7/")
    posts = graph.get_object(next)
print(whole_feed)


