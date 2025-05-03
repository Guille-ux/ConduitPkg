# SPDX-FileCopyrightText: 2025-present Guille on a Raspberry pi <guilleleiratemes@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os
import shutil
import pathlib
from zynk_lite import interpreter

def extract(name):
    user_root = os.path.expanduser("~")
    packet_path = pathlib.Path.joinpath(user_root, ".conduitpkg", name)
    shutil.unpack_archive(name+".zip", packet_path)
    os.chdir(packet_path)
    intp = interpreter.ZynkLInterpreter()
    intp.eval_file("builder.zl")