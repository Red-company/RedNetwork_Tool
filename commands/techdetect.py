"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import sys
import json
from requests import get

from config import wappalyzer_key


# DetectTech function.
def detectTech(url):
	# Info.
    headers = {'x-api-key' : wappalyzer_key}

    # Process.
    r = get('https://api.wappalyzer.com/v2/lookup/?urls=' + url, headers=headers)
    
    technologies  = []
    list_response = []

    # Response process.
    for one in r:
        list_response.append(r.json())

    technologies = list_response[0][0]['technologies']

    # Print.
    sys.stdout.write('\n')

    for tech in technologies:
        sys.stdout.write(tech['name'] + '\n')