# -*- coding: utf-8 -*-
from utils import *
from spam_util import *

grupa_testowa_id = 561578050704724
grupa_nsdap = 1407624762867787

graph = init()

powtorzenia = licz_slowa_w_feedzie(graph, grupa_nsdap, "hitler")
print(powtorzenia)


