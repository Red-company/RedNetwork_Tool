"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import os


# Traceroute function.
def traceroute(host):
    print('\033[4mTraceroute will start. Press CTRL + C to cancel.\033[0m')
    os.system(f'traceroute {host}')