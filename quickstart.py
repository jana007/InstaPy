""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy()

with smart_run(session):
    # general settings
    # session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["thumbsup"], amount=15)
    session.set_do_comment(enabled=True, percentage=75)
    session.set_comments(['thumbs up', u'thumbs up 👍', u'👍thumbs up👍', u'👍👍👍👍👍👍👍'])
    
    
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                  peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)
