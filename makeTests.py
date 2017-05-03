import sys
import random
from optimal_fingerings import N2F

ALL_NUMS = N2F.keys()

with open("test_files/test_"+sys.argv[1]+".txt", 'w') as file:
    for i in range(int(sys.argv[1])):
        file.write(str(random.randrange(min(ALL_NUMS), max(ALL_NUMS)+1))+"\n")