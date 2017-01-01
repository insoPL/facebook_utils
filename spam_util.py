# -*- coding: utf-8 -*-
import random


def spam_posts(graph, target_group_id):
    for x in range(20):
        graph.put_object(parent_object=str(target_group_id), connection_name='feed', message='post' + str(x))


def spam_post_with_comments(graph, post_id):
    for x in range(20):
        graph.put_comment(post_id, "komentarz"+str(x))


def spam_comment_with_comments(graph, comment_id):
    for x in range(15):
        if random.randint(0, 1) == 0:
            graph.put_comment(comment_id, "komentarz"+str(x))
        else:
            graph.put_comment(comment_id, "komenkeytarz" + str(x))


def spam_posts_with_key(graph, target_group_id):
    for x in range(20):
        if random.randint(0, 1) == 0:
            graph.put_object(parent_object=str(target_group_id), connection_name='feed', message='post' + str(x) + "key")
        else:
            graph.put_object(parent_object=str(target_group_id), connection_name='feed', message='post' + str(x))


def spam_comments(graph, posts):
    for post in posts:
        if random.randint(0, 1) == 0:
            graph.put_object(parent_object=post["id"], connection_name="comments", message=str(hash(random.randint(1,20)))+"key")

