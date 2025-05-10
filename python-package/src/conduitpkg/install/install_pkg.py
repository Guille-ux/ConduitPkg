# SPDX-FileCopyrightText: 2025-present Guille on a Raspberry pi <guilleleiratemes@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from git import Repo
import os
import json
from . import search_packet as search
from . import dependencies
from urllib.request import urlopen, urlretrieve
from ..packaging.extracting import extract
import shutil

def get_packet(name, protocol):
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
    if len(where) < 1:
        print("[!] Packet doesn't exist [!]")
    elif len(where) > 1:
        print("[!] Warning: this is i various repos [!]")
        # añadir manejo para elegir
        return
    else:
        repo = repos_list[0]
    pkg_list = search.get_pkg_list(repo)
    pkg_url = pkg_list[name]
    # tengo que hacer la parte de descarga del paquete
    # primero averiguar donde esta el paquete, y despues descargarlo
    if protocol == "git":
        print("[+] Cloning [+]")
        Repo.clone_from(pkg_url, ".")
        extract.gextract(name)
        print(f"[+] Packet '{name}' Installed [+]")
    elif protocol=="http":
        urlretrieve(pkg_url, name+".zip")
        extract.extract(name)