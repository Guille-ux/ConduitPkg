# SPDX-FileCopyrightText: 2025-present Guille on a Raspberry pi <guilleleiratemes@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import urllib
import pathlib

def get_repos():
    user_root = os.path.expanduser("~")
    repos_lists_path = pathlib.Path.joinpath(user_root, ".conduitpkg", "list.json")
    with open(repos_lists_path, "r") as f:
        repos_lists = json.load(f)
    return repos_lists