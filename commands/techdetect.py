"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import sys
import json
from requests import get


# DetectTech function.
def detectTech(url):
	# Info.
    headers = {'x-api-key' : 'za8hSNwc9G3emtusKNyfP6kbc2Z32XZxaGd9q2By'}

    # Process.
    r = get('https://api.wappalyzer.com/v2/lookup/?urls=' + url, headers=headers)
    
    technologies  = []
    list_response = []

    # Response process.
    for one in r:
        list_response.append(r.json())

    technologies = list_response[0][0]['technologies']

    # Print.
    for tech in technologies:
        sys.stdout.write(tech['name'] + '\n')