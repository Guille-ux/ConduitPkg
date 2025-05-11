# SPDX-FileCopyrightText: 2025-present Guille on a Raspberry pi <guilleleiratemes@gmail.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .. import install
from .. import postinstall
from .. import packaging
from .. import builder
import shutil
import os

def install_pkg(name, local=False, protocol="http"):
    if local:
        local_advanced_install(name, protocol)
    elif not local:
        advanced_install(name, protocol)
    else:
        print("[!] Unknown Method [!]")

def advanced_install(name, protocol="http"):
    print("[+] Installing Globally [+]")
    install.get_pkg.get_packet(name, protocol)
    install.dependencies.resolve(name)

def local_advanced_install(name, protocol="http"):
    print("[+] Installing Locally [+]")
    install.get_pkg.local_get_packet(name, protocol)
    install.dependencies.local_resolve(name)

def exec_entry(command):
    print("[+] Running Global Entry [+]")
    current=os.getcwd()
    entry=install.entries.get_entry(command)
    cpkg_root = os.path.join(os.path.expanduser("~"), ".conduitpkg")
    os.chdir(cpkg_root)
    os.system(entry)
    os.chdir(current)

def local_exec_entry(command):
    print("[+] Running Local Entry [+]")
    entry=install.entries.get_entry(command)
    cpkg_root = ".conduitpkg"
    os.chdir(cpkg_root)
    os.system(entry)
    os.chdir("..")

def compress(dir):
    print("[+] Compressing [+]")
    os.chdir(dir)
    packaging.comp.compress.compress()
    os.chdir("..")
    shutil.copytree(os.path.join(dir, "dist"), ".")
    shutil.rmtree(os.path.join(dir, "dist"))

def extract(name, local=False, zipped=True):
    if zipped:
        print("[+] Extracting from zip... [+]")
        if local:
            print("[+] Installing Locally [+]")
            packaging.extr.extract.local_extract(name)
        elif not local:
            print("[+] Installing Globally [+]")
            packaging.extr.extract.extract(name)
        else:
            return
    elif not zipped:
        print("[+] Installing from folder [+]")
        if local:
            print("[+] Installing Locally [+]")
            packaging.extr.extract.local_gextract(name)
        elif not local:
            print("[+] Installing Globally [+]")
            packaging.extr.extract.gextract(name)
        else:
            return
    else:
        print("[!] Unknown Method [!]")
        return
    
def post_install(local=True):
    if local:
        print("[+] Initializing Locally... [+]")
        postinstall.local_post_install()
    elif not local:
        print("[+] Initializing Globally... [+]")
        postinstall.post_install()
    else:
        return
    
def init_pkg(name):
    if name in os.listdir("."):
        print("[!] Packet Already Exists [!]")
        return
    builder.new_packet(name)