from collections import Counter, OrderedDict
from datetime import date

from flask import current_app

from .. import pages, posts


_meta_title = 'title'
_meta_author = 'author'
_meta_published = 'published'
_meta_categories = 'categories'
_meta_tags = 'tags'
_meta_header_image = 'header-image'


def get_all_pages():
    published_pages = [
        p for p in pages if p.meta.get(_meta_published, None) is not None
    ]

    sorted_pages = sorted(
        published_pages, reverse=True, key=lambda p: p.meta[_meta_published]
    )
    return sorted_pages


def get_page(path):
    return pages.get_or_404(path)


def get_tagged_pages(tag):
    all_pages = get_all_pages()
    return [p for p in all_pages if tag in p.meta.get(_meta_tags, [])]


def get_categorized_pages(category):
    all_pages = get_all_pages()
    return [p for p in all_pages
            if category in p.meta.get(_meta_categories, [])]


def get_all_posts():
    published_posts = [
        p for p in posts if p.meta.get(_meta_published, None) is not None
    ]

    sorted_posts = sorted(
        published_posts, reverse=True, key=lambda p: p.meta[_meta_published]
    )
    return sorted_posts


def get_latest_posts(offset=None):
    if offset is None:
        offset = 0

    published_posts = [
        p for p in posts if p.meta.get(_meta_published, None) is not None
    ]

    sorted_posts = sorted(
        published_posts, reverse=True, key=lambda p: p.meta[_meta_published]
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


def get_tagged_posts(tag):
    all_posts = get_all_posts()
    return [p for p in all_posts if tag in p.meta.get(_meta_tags, [])]


def get_categorized_posts(category):
    all_posts = get_all_posts()
    return [p for p in all_posts
            if category in p.meta.get(_meta_categories, [])]


def get_all_categories():
    def fill_categories(items):
        for i in items:
            cats = i.meta.get(_meta_categories, None)
            if cats:
                for c in cats:
                    category = {
                        'name': c,
                        'pages': get_categorized_pages(c),
                        'posts': get_categorized_posts(c),
                    }
                    if category not in all_categories:
                        all_categories.append(category)

    all_categories = []
    fill_categories(pages)
    fill_categories(posts)
    return sorted(
        all_categories, key=lambda c: c['name']
    )


def get_all_tags():
    def fill_tags(items):
        for i in items:
            tags = i.meta.get(_meta_tags, None)
            if tags:
                for t in tags:
                    tag = {
                        'name': t,
                        'pages': get_tagged_pages(t),
                        'posts': get_tagged_posts(t),
                    }
                    if tag not in all_tags:
                        all_tags.append(tag)

    all_tags = []
    fill_tags(pages)
    fill_tags(posts)
    return sorted(
        all_tags, key=lambda t: t['name']
    )


def get_archives():
    all_posts = get_all_posts()

    dated_posts = [
        (p.meta[_meta_published].year, p.meta[_meta_published].month, p)
        for p in all_posts if p.meta.get(_meta_published)
    ]

    dates = [(p.meta[_meta_published].year, p.meta[_meta_published].month)
             for p in all_posts if p.meta.get(_meta_published)]

    yearly = sorted(Counter([d[0] for d in dates]).items(), reverse=True)
    monthly = sorted(Counter([d for d in dates]).items(), reverse=True)

    archives = []
    for y in yearly:
        year = y[0]
        year_count = y[1]
        year_archive = {
            'date': date(year=year, month=1, day=1),
            'count': year_count,
            'months': [
                {
                    'date': date(year=year, month=m[0][1], day=1),
                    'count': m[1],
                    'posts': [
                        p[2] for p in dated_posts
                        if p[0] == year and p[1] == m[0][1]
                    ]
                } for m in monthly if m[0][0] == year
            ]
        }
        archives.append(year_archive)

    return archives


def get_yearly_posts(year):
    all_posts = get_all_posts()
    return [p for p in all_posts if p.meta.get(_meta_published).year == year]


def get_monthly_posts(year, month):
    all_posts = get_all_posts()
    return [p for p in all_posts
            if p.meta.get(_meta_published).year == year and
            p.meta.get(_meta_published).month == month]


def get_global_config():
    return {
        'debug': current_app.config.get('DEBUG', False),
        'title': current_app.config.get('TITLE'),
        'subtitle': current_app.config.get('SUBTITLE'),
        'author': current_app.config.get('AUTHOR'),
        'posts_per_page': current_app.config.get('POSTS_PER_PAGE', 10),
        'all_pages': get_all_pages(),
        'all_posts': get_all_posts(),
        'all_categories': get_all_categories(),
        'all_tags': get_all_tags(),
        'archives': get_archives(),
    }
