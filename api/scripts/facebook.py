from facebook_scraper import get_posts

from fb_parsing.settings import EMAIL
from fb_parsing.settings import PASSWORD


def fb_posts(post_urls):
    data = []

    for post in get_posts(
        post_urls=post_urls,
        credentials=(EMAIL, PASSWORD),
        options={
            "reactions": True,
            }
    ):
        post_id = post.get('post_id')
        post_url = post.get('post_url')
        published_time = post.get('time')
        content = post.get('text')
        likes = post.get('likes')
        reactions = post.get('reactions')
        reaction_count = post.get('reaction_count')
        comment_count = post.get('comments')

        post_info = ({
            'post_id': post_id,
            'post_link': post_url,
            'published_time': published_time.strftime("%Y-%m-%d %H:%M:%S") if published_time else None,
            'content': content,
            'likes': likes,
            'reactions': reactions,
            'reaction_count': reaction_count,
            'comment_count': comment_count
        })

        data.append(post_info)

    return data
