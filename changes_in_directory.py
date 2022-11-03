import time
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", action="store", default=".", help="Path to the directory")
args = parser.parse_args()
files = set(os.listdir(args.path))
while True:
    files1 = set(os.listdir(args.path))
    t = time.asctime()
    for new_file in files1 - files:
        print(t.split(' ')[4] + " file '" + new_file + "' was created")
    for deleted_file in files - files1:
        print(t.split(' ')[4] + " file '" + deleted_file + "' was removed")
    files = files1
    time.sleep(1)
