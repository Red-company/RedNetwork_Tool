"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import re
import os
import requests
import platform


# Dns map function.
def dnsmap(dnsmap_inp):
    image = requests.get('https://dnsdumpster.com/static/map/%s.png' % dnsmap_inp)

    if image.status_code == 200:
        image_name = dnsmap_inp.replace(".com","")

        with open('%s.png' % image_name, 'wb') as f:
            f.write(image.content)

            print("\n%s.png DNS Map image stored to .../RedNetwok_Tool/ path" % image_name + ".")

    else:
        print("Sorry We Would not find the dnsmap")