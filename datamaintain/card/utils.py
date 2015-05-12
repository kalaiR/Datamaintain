from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_paginator_obj(object_list, page, per_page):
    paginator = Paginator(object_list, per_page, orphans=0)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects