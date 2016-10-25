import timeit

# naive algorithm for counting matches in text
fname = 'randomdna.txt'
f = open(fname, 'r')
text = f.readline()
pattern = f.readline()
# fix pattern indexing somehow has an extra null chracter eg AAAAA-nul- intead of AAAAA
if pattern[len(pattern)-1] == "\n":
    pattern = pattern[0:len(pattern)-1]
print pattern
t_size = len(text)
p_size = len(pattern)

# start timer after preprocessing
start_time = timeit.default_timer()

curr_index = 0
num_match = 0

while curr_index + p_size <= t_size:
	i = 0
	while i < p_size:
		if text[curr_index + i] != pattern [i]:
			break
		i = i + 1

	if i == p_size:
		num_match = num_match + 1

	# increment index
	curr_index = curr_index + 1

print num_match
print "runtime: " + str(timeit.default_timer()-start_time)
