"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import sys
from requests import get

# Censys function.
def censys(ip):
    dirty_response = get('https://censys.io/ipv4/%s/raw' % ip).text
    clean_response = dirty_response.replace('&#34;', '"')

    response = clean_response.split('<code class="json">')[1].split('</code>')[0]

    sys.stdout.write('\n' + response + '\n')