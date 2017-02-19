from __future__ import unicode_literals

from collections import Counter


def replace_nonalnum(c):
    if c.isalnum():
        print(c)
        return c
    else:
        return ' '


def word_count(phrase):
    c = Counter(''.join(map(replace_nonalnum, phrase.lower())).split())
    return dict(c)