"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import sys
from requests import get

# Reverseiplookup function.
def reverseiplookup():
    inp_str = input("\nEnter an ip: ")

    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % inp_str

    try:
        result = get(lookup).text
        sys.stdout.write('\n' + result + '\n')

    except:
        sys.stdout.write('%s Error' % bad)