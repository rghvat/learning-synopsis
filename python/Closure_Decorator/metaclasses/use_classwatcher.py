# file: use_classwatcher.py

from classwatcher import ClassWatcher

watcher = ClassWatcher()

import argparse
import doctest
import logging
import os
import shutil
import subprocess
import sys
import threading

import numpy
import matplotlib
import pandas
import scipy
import sqlalchemy

watcher.report(20)
