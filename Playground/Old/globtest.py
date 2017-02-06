import time, os, sys, datetime, glob

directory='./testfolder'
os.chdir(directory)
files=glob.glob('*.txt')
for filename in files:
    os.remove(filename)
