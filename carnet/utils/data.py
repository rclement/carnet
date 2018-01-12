import math

from flask import current_app

from .. import pages, posts


def get_all_pages():
    published_pages = [
        p for p in pages if p.meta.get('published', None) is not None
    ]

    sorted_pages = sorted(
        published_pages, reverse=True, key=lambda p: p.meta['published']
    )
    return sorted_pages


def get_page(path):
    return pages.get_or_404(path)


def get_all_posts():
    published_posts = [
        p for p in posts if p.meta.get('published', None) is not None
    ]

    sorted_posts = sorted(
        published_posts, reverse=True, key=lambda p: p.meta['published']
    )
    return sorted_posts


def get_latest_posts(offset=None):
    if offset is None:
        offset = 0

    published_posts = [
        p for p in posts if p.meta.get('published', None) is not None
    ]

    sorted_posts = sorted(
        published_posts, reverse=True, key=lambda p: p.meta['published']
    )

    num_posts = len(sorted_posts)
    post_per_page = current_app.config.get('POSTS_PER_PAGE', 10)
    post_page_max = int(num_posts / post_per_page)

    post_page = max(min(offset, post_page_max), 0)
    start = min(num_posts, post_per_page * post_page)
    end = min(num_posts, start + post_per_page)

    return sorted_posts[start:end], post_page, post_page_max


def get_post(path):
    return posts.get_or_404(path)


def get_all_categories():
    def fill_categories(items):
        for i in items:
            cats = i.meta.get('categories', None)
            if cats:
                for c in cats:
                    if c not in all_categories:
                        all_categories.append(c)

    all_categories = []
    fill_categories(pages)
    fill_categories(posts)
    return sorted(all_categories)


def get_all_tags():
    def fill_tags(items):
        for i in items:
            tags = i.meta.get('tags', None)
            if tags:
                for t in tags:
                    if t not in all_tags:
                        all_tags.append(t)

    all_tags = []
    fill_tags(pages)
    fill_tags(posts)
    return sorted(all_tags)


def get_global_config():
    return {
        'title': current_app.config.get('TITLE'),
        'subtitle': current_app.config.get('SUBTITLE'),
        'author': current_app.config.get('AUTHOR'),
        'all_pages': get_all_pages(),
        'all_posts': get_all_posts(),
        'all_categories': get_all_categories(),
        'all_tags': get_all_tags(),
    }
