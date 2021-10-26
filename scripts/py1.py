#!/usr/bin/env python3

import argparse, glob, json, re, subprocess, urllib.request, os, sys
from sys import platform
from pathlib import Path

def shell(cmd, check=True):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, check=check )
    return result.stdout.decode('utf-8').strip()

shell("echo -n {} | secret-tool store --label='Test tool' Test tool".format('Itsme1'))
access_token = shell('secret-tool lookup Test tool')
print(f'From python {sys.version_info} {access_token}')
