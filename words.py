#! /usr/bin/env python3

"""
Retrieve and print words from a URL.
Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """
    Fetch a list of words from a URL.
    :param url: the url of a UTF-8 document.
    :return: A list of strings containing the words from the document.

    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """
    Print lines one per line
    :param items: an iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """
    Print each word from a text document from a url.
    :param url: the url of a UTF-8 document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # The 0th arg is the module filename.
