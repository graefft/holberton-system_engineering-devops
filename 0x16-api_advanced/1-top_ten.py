#!/usr/bin/python3
'''Function that queries Reddit API and returns top 10 hot posts'''
import requests


def top_ten(subreddit):
    '''Returns top 10 hot posts'''
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/76.0.3809.132 '
               'Safari/537.36',
               'Content-Type': 'application/json'}
    request = requests.get(url, headers=headers, allow_redirects=False)
    if request.status_code == requests.codes.ok:
        request_json = request.json()
        request_data = request_json.get('data')
        hot_posts = request_data.get('children')
        for post in hot_posts:
            hot_data = post.get('data')
            print(hot_data.get('title'))
    else:
        print('None')
