#!/usr/bin/python3
'''Function that queries Reddit API and returns number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''Return total number of subscribers'''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/76.0.3809.132 '
               'Safari/537.36',
               'Content-Type': 'application/json'}
    request = requests.get(url, headers=headers, allow_redirects=False)
    if request.status_code < 300:
        request_json = request.json()
        request_data = request_json.get('data')
        return request_data.get('subscribers')
    else:
        return 0
