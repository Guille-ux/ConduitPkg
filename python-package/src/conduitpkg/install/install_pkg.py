# SPDX-FileCopyrightText: 2025-present Guille on a Raspberry pi <guilleleiratemes@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import git
import os
import json
from . import search_packet as search
from . import dependencies

def get_packet(name):
    print("[+] Searching Packet [+]")
    print("[+] Listing Repos [+]")
    repos_list = search.get_repos()
    where = []
    print("[+] Searching on repos [+]")
    for repo in repos_list:
        print(f"[+] Searching on Repo {repo} the packet {name} [+]")
        if search.is_in_repo(repo, name):
            where.append(repo)
            print(f"[+] Package {name} is in {repo} [+]")
    if len(where) > 1:
        print("[!] Warning: this is i various repos [!]")
    # tengo que hacer la parte de descarga del paquete
    # primero averiguar donde esta el paquete, y despues descargarlo