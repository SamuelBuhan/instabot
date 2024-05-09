from instapy import InstaPy
from instapy import smart_run

def run_instagram_bot(username, password, hashtags):
    session = InstaPy(username=pers, password=password)

    with smart_run(session):
        # Set up your bot's actions here
        session.like_by_tags(hashtags, amount=5)

run_instagram_bot()