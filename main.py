# -*- coding: utf-8 -*-
from utils import *
from spam_util import *

grupa_testowa_id = 561578050704724

graph = init()

feed_grupy_testowej = get_whole_feed(graph, grupa_testowa_id)

spam_post_with_comments(graph, "561578050704724_561624114033451")

#powtorzenia = licz_slowa(feed_grupy_testowej, "key")
#print(feed_grupy_testowej)


