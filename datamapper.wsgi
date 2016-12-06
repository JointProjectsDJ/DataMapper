#!/usr/bin/python
import sys
sys.path.insert(0,'C:\Anaconda3\Lib\site-packages')
sys.path.append("/home/binoy/PycharmProjects/DataMapper/")

logging.basicConfig(stream=sys.stderr)

from rest_api.app import app as application