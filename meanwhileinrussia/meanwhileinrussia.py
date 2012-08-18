#!/usr/bin/env python
'''
This is just a stupid fun plugin for sevabot to parse random lines from a URL which gives us fresh videos from mother Russia <3
Pull requests for submitting new "meanwhile in Russia" videos can be submitted here https://github.com/lixef/glowing-octo-wight/tree/gh-pages
The default URL is hosted on GitHub pages.
'''

import urllib
import random

url = urllib.urlopen('http://felix.tl/glowing-octo-wight/').read().splitlines()
line = random.choice(url)
print(line)
