def parse_data(data, mmap):
	for line in data:
		temp = line.split(" -> ")
		mmap[temp[0]] = temp[1].split(",")
	return mmap

def combine_cycles(cycle1, cycle2):
	f = open("mytest.txt", "a")

	f.write("hi" + cycle1 + "break"+cycle2 +"\n")
	temp = cycle2.split("->")
	temp.pop()
	temp2 = cycle1.split("->")
	location = temp2.index(temp[0])
	temp2[location] = "*****"
	blah = "->".join(temp2)
	location = blah.find("*****")

	return cycle1[:location] + "->".join(temp) + "->" + cycle1[location:]

def find_cycle(cycles, mmap, key):
	cycle = ""
	if key == "none":
		# find node that has open edges and set it as start
		for key in mmap.keys():
			if mmap[key]:
				cycle = key
				break

		# set key to cycle

		key = cycle
	else:
		cycle = key

	# walk through until there is no edge left
	while mmap[key]:
		cycle += "->"
		# always choose first from the list
		key = mmap[key].pop(0)
		cycle += key
	if cycles != "":
		cycles = combine_cycles(cycles, cycle)
	else:
		cycles = cycle
	return (cycles, mmap)

def find_y(cycles, mmap):
	temp = cycles.split("->")
	for node in temp:
		if mmap[node] != []:
			return node
	return "completed"


def done(values):
	for val in values:
		if val != []:
			return False
	return True


# process data
fname = "rosalind_ba3f.txt"
dataset = open(fname, "r")
data = dataset.read().splitlines()

# map contains all the verticies->edges
mmap = {}
mmap = parse_data(data, mmap)

# cycles will hold all cycles found
cycles = ""
# data is parsed into a dictionary and processing is ready to begin
answer = open("answer.txt", "w")

# first run through to find main cycle
temp = find_cycle(cycles, mmap, "none")
cycles = temp[0]
mmap = temp[1]
next = find_y(cycles, mmap) 
answer = open("answer.txt", "w")
while next != "completed":
	temp = find_cycle(cycles, mmap, next)
	cycles = temp[0]
	mmap = temp[1]
	next = find_y(cycles, mmap)

# print "after while"




answer.write(cycles)
