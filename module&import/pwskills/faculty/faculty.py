import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from courses import batches

def faculty():
    print('this is faculty funciton')

batches.batches()