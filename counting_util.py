# -*- coding: utf-8 -*-


def licz_slowa_w_feedzie(graph, target_group_id, key):
    count = 0
    posts = graph.get_object(id=str(target_group_id)+'/feed?limit=100')
    while True:
        if "paging" not in posts:
            break

        count += licz_slowa_w_postach(graph, posts["data"], key)

        next_page = posts["paging"]["next"]
        next_page = next_page.lstrip("https://graph.facebook.com/v2.7/")
        posts = graph.get_object(next_page)
        print(count)
    return count


def licz_slowa_w_postach(graph, posts, key):
    count = 0
    for post in posts:
        if 'message' in post and key in post['message'].lower():
            count += 1
        count += licz_slowa_w_komentarzach_do_posta(graph, post["id"], key)
    return count


def licz_slowa_w_komentarzach_do_posta(graph, post_id, key):
    comments = graph.get_object(post_id+"/comments?limit=500")
    comments = comments["data"]
    count = 0
    for comment in comments:
        if 'message' in comment and key in comment['message'].lower():
            count += 1
        count += licz_slowa_w_komentarzach_do_komentarza(graph, comment["id"], key)
    return count


def licz_slowa_w_komentarzach_do_komentarza(graph, post_id, key):
    comments = graph.get_object(post_id+"/comments?limit=500")
    comments = comments["data"]
    count = 0

    for comment in comments:
        if 'message' in comment and key in comment['message'].lower():
            count += 1
    return count
