from random import choice
f = open('randomdna.txt', 'w')
DNA=""
for count in range(10000000):
    DNA+=choice("CGTA")
f.write(DNA)
f.write("\nAGTGCGTTGCG")