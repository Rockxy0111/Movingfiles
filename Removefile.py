import os
import shutil
import time

path = input("enter file name")


if os.path.exists(path):
    ctime = os.stat(path).st_ctime
