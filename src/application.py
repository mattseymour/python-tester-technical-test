# Python 2,3 support
from __future__ import print_function
from six.moves import input

import os
import sys
import re
import requests
from bs4 import BeautifulSoup

def get(a):
    # Performs a http request, returning a string
    response = requests.get(a)
    return response.text

def element_count(a, b):
    # element count
    output = get(a)

    soup = BeautifulSoup(output)

    return len(soup.find_all(b))

def fizz_or_buzz(number):
    # Return fizz or buzz or fizzbuzz
    # number/3 then fizz
    # number/5 then buzz
    # number/(3,5) then fizz buzz
    # number !/ (3,5) then <empty>
    is_three = True if number % 3 == 0 else False
    is_five = True if number % 5 == 0 else False

    if is_three:
        return 'fizz'
    elif is_five:
        return 'buzz'
    elif is_three and is_five:
        return 'fizzbuzz'
    else:
        return ''

def app_output(*args):
    with open('output.txt', 'a') as fd:
        fd.write('{} = {} = {} = {}\n'.format(*args))
    print('{} = {} = {} = {}\n'.format(*args))

def app(a,b):
    count = element_count(a,b)
    FizzBuzz = fizz_or_buzz(count)
    app_output(a,b,count,FizzBuzz)

import sys
if __name__ == '__main__':
        # application will take two args url, html tag type (a, ul, div, ...etc)
        if len(sys.argv) < 3:
            url = input('Url: ')
            tag = input('Tag: ')
        else:
            url = sys.argv[1]
            tag = sys.argv[2]

        app(url, tag)
