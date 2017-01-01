# -*- coding: utf-8 -*-
from utils import *

grupa_testowa_id = 561578050704724

graph = init()

feed_grupy_testowej = get_whole_feed(graph, grupa_testowa_id)

print(feed_grupy_testowej)


