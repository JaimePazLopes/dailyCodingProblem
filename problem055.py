# Problem #55 [Easy]
# Implement a URL shortener with the following methods:
#
#     shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
#     restore(short), which expands the shortened string into the original url.
#           If no such shortened string exists, return null.
#
# Hint: What if we enter the same URL twice?

import random
import string


class URL_Shortner:

    def __init__(self):
        # dictionary to save all the shortned url and its full url
        self.url_dict = dict()

    def shorten(self, url):
        # use the full url as a seed to the random function
        random.seed(url)
        # make a 6 digits string by taken multiple characters randomly
        shortned = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        # if the short url is no the dict, return it
        if shortned in self.url_dict:
            return shortned

        # if it is not, add and return it
        self.url_dict[shortned] = url

        return shortned

    # the restore is just the value of the short url key
    def restore(self, short):
        return self.url_dict[short]


url_shortner = URL_Shortner()
long_url = "www.google.com"
short_url = url_shortner.shorten(long_url)
assert long_url == url_shortner.restore(short_url)

long_url2 = "www.google.com"
short_url2 = url_shortner.shorten(long_url2)
assert long_url2 == url_shortner.restore(short_url2)
assert short_url == short_url2
assert url_shortner.restore(short_url) == url_shortner.restore(short_url2)

long_url3 = "www.dailycodingproblem.com"
short_url3 = url_shortner.shorten(long_url3)
assert long_url3 == url_shortner.restore(short_url3)

# cool problem to do, i dont know if the random way to do the short url might give different long urls the same short
# one. but i think that for this problem is a good enough solution. everything took less than 20 minutes
