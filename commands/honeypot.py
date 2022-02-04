"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import sys
from requests import get

from config import shodan_key


# Honeypot function.
def honeypot(inp):
    honey = 'https://api.shodan.io/labs/honeyscore/' + inp + '?key=' + shodan_key

    try:
        result = get(honey).text
        probability = str(float(result) * 10)

    except:
        result = None
        sys.stdout.write('\033[93m[!]\033[0m No information available\n')

    if result:
        if float(result) < 0.5:
            sys.stdout.write('[\033[91m*\033[0m]\033[93m[!]\033[0m Honeypot Probabilty: \033[92m' + str(float(result)) + '\033[0m %\n')

        else:
            sys.stdout.write('[\033[91m*\033[0m]\033[93m[!]\033[0m Honeypot Probabilty: \033[91m' + str(float(result)) + '\033[0m %\n')