# -*- coding: utf-8 -*-
# Created by Kelly Reddington 1/11/2017

import pytumblr
import os
import sys
import urllib
import re
from tumblr_keys import *
if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlretrieve

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

def media_download(mylikes, dirname):
    for i in range(0, len(mylikes['liked_posts'])):
        if mylikes['liked_posts'][i]['type'] == 'photo':
            for j in range(0, len(mylikes['liked_posts'][i]['photos'])):
                url = mylikes['liked_posts'][i]['photos'][j]['original_size']['url']
                name = re.findall(r'tumblr_\w+.\w+', url)
                urlretrieve(url, dirname + '/' + name[0])
            print('[' + str(i+1) + ':' + str(len(mylikes['liked_posts'])) + ']')
        elif mylikes['liked_posts'][i]['type'] == 'video':
            url = mylikes['liked_posts'][i]['video_url']
            name = re.findall(r'tumblr_\w+.\w+', url)
            urlretrieve(url, dirname + '/' + name[0])
            print('[' + str(i+1) + ':' + str(len(mylikes['liked_posts'])) + ']')
        else:
            print('[' + str(i+1) + ':' + str(len(mylikes['liked_posts'])) + ']')

def main():
    info = client.info()
    dirname = info['user']['name']
    blogurl = info['user']['blogs'][0]['url']
    likescount = info['user']['likes']
    if not os.path.exists(dirname):
        os.makedirs(dirname)
        mylikes = client.likes(limit=50)
        media_download(mylikes, dirname)

if __name__ == '__main__':
    main()
    print('Done!')
