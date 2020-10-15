import pathlib
import os
import sys

p1 = str(pathlib.Path(os.path.abspath(__file__)).parent)
sys.path.append(p1)
# p2 = str(p1)+'/data/corpus/people_daily/people.dev'
print(p1)
