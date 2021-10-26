#!/usr/bin/env python3

import logging
import argparse
from tkinter import *
from tkinter import ttk
from enum import Enum
from numpy.lib.function_base import select
import pathlib
from datetime import datetime
import re
import sys
from pathlib import Path
import shutil
import subprocess
import zipfile
import os
import glob
import getpass
logger = logging.getLogger(__name__)

import argparse, glob, json, re, subprocess, urllib.request, os, sys
from sys import platform
from pathlib import Path

print(f'py1 print {sys.version_info}')
logger.info("py1 info")
