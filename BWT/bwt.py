fname = 'rosalind_ba9j.txt'
f = open(fname, 'r')
original = f.read().splitlines()[0]
length = len(original)
# replace $ with a so sorting is easier
transform = list(original)
original_arr = list(original)

for i in range(0, len(transform)-1):
	transform.sort()
	for j in range(0,len(transform)):
		transform[j] = original[j] + transform[j]
for string in transform:
	if string[length-1] == "$":
		answer = open('answer.txt', "w")
		answer.write(string)


