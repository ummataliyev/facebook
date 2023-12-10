from facebook_scraper import set_cookies
from facebook_scraper import get_posts

from fb_parsing.settings import FACEBOOK_COOKIES


def more_pages(account, start_date, end_date):
    set_cookies(FACEBOOK_COOKIES)

    data = []

    for post in get_posts(
        account=account,
        base_url="https://mbasic.facebook.com",
        start_url=f"https://mbasic.facebook.com/{account}?v=timeline",
        pages=6,
        options={
            "posts_per_page": 10,
            "allow_extra_requests": False,
            "comments": False,
            "reactors": False,
            "progress": False
        }
    ):
        post_date = post['time']

        if start_date <= post_date <= end_date:
            post_data = {
                "post_counter": len(data) + 1,
                "text": post["text"],
                "post_date": post_date
            }
            data.append(post_data)

            if len(data) >= 10:
                break
        elif post_date < start_date:
            break

    return data
