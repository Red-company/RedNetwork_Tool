"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import requests


# Mac address lookup function.
def macaddresslookup(mac):
    url = ("https://macvendors.co/api/" + mac)
    response=requests.get(url)
    result=response.json()

    if result["result"]:
        final=result['result']

        print("")
        print("Company: " + str(final["company"]))
        print("Address: " + str(final["address"]))
        print("Country: " + str(final["country"]))
        print("")

    else:
        print("Error: Something Went Wrong")