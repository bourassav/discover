#!/usr/bin/env python3
"""Retrieve and print words from URL.

Usage:

    python3 chap3_smallshire.py <URL>

"""
# %% ANCHOR IMPORTS

from urllib.request import urlopen
import sys

# %% ANCHOR MAIN

def main(url):
    """Print each word from a text document at a URL.

    Args:
        url: The URL of a UTF-8 text document.    
    """
    words = fetch_words(url)
    print_items(words)

# %% All the functions

# This fetches the words and returns them as a list
# I'm keeping this for later :'http://sixty-north.com/c/t.txt'
def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
        
    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    
    return story_words


# This prints a list of words
def print_items(items):
    """Print items one per line.

    Args:
        items: An iterable series of printable items.
    """
    for item in items:
        print(item)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename.
