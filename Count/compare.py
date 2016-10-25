# compare the two programs
import os
os.system("createDna.py 1")
print "========NAIVE======="
os.system("count.py 1")
print "========KMP========="
os.system("count_kmp.py 1")