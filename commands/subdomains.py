"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import requests, sys, json


# Subdomains function.
def subdomains(domain):
    # Process.
    with open ("subdomain_list.txt", encoding="utf-8") as f:
        content = f.read()
    
    subdomains = content.splitlines()
    discovered_subdomains = list()

    print("")

    for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"

        try:
            requests.get(url)

        except requests.ConnectionError:
            pass

        else:
            print ("[\033[91m*\033[0m] Subdomain found: ", url)
            discovered_subdomains.append(url)
    