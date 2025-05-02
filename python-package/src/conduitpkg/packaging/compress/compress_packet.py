# SPDX-FileCopyrightText: 2025-present Guille on a Raspberry pi <guilleleiratemes@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import shutil
import os
import json
import pathlib

def compress():
    try:
        with open("package.json", "r") as f:
            name = json.load(f)["name"]
    except Exception:
        print("[!] Not in a package directory [!]")
    os.mkdir("dist")
    os.mkdir(f"dist/{name}")
    dist_path=pathlib.Path.joinpath("dist", name)
    shutil.copy("package.json", pathlib.Path.joinpath("dist", name))
