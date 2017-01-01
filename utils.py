# -*- coding: utf-8 -*-
import facebook
import random


def init():
    file = open("keys", "r")
    key = file.read()
    file.close()
    return facebook.GraphAPI(access_token=key, version='2.7')


def spam_posts(graph):
    for x in range(20):
        graph.put_object(parent_object='561578050704724', connection_name='feed', message='post' + str(x))


def spam_posts_with_key(graph):
    for x in range(20):
        if random.randint(0, 1) == 0:
            graph.put_object(parent_object='561578050704724', connection_name='feed', message='post' + str(x) + "key")
        else:
            graph.put_object(parent_object='561578050704724', connection_name='feed', message='post' + str(x))


def spam_comments(graph, posts):
    for post in posts:
        if random.randint(0, 1) == 0:
            graph.put_object(parent_object=post["id"], connection_name="comments", message=str(hash(random.randint(1,20)))+"key")


def remove_posts(graph, posts):
    for post in posts:
        graph.delete_object(post["id"])
