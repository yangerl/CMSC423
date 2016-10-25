def minsert(item, mlist):
	length = len(mlist)
	curr_index = 0
	for curr_index in range(0,length):
		if (mlist[curr_index] >= item):
			mlist.insert(curr_index, item)
			return mlist
	mlist.append(item)
	return mlist


def compose(k, text):
	manswer = []
	curr_index = 0
	size = len(text)
	while curr_index < size-k:
		manswer = minsert(text[curr_index:curr_index+k], manswer)
		curr_index += 1

	return manswer

def create_string(kmer, tail, dict):
	my_string = kmer + " -> "
	mlist = dict[tail]
	for kmer in mlist:
		my_string += kmer+","
	if my_string == kmer + " -> ":
		return ""
	else:
		return my_string[0:len(my_string)-1]+"\n"



#fname = "rosalind_ba3d.txt"
fname = "test.txt"
f = open(fname, "r")

k = int(f.readline())
text = f.readlines()
text = text[0]

kmers = compose(k-1, text)			
keys = compose(k-2, text)
f2 = open("kmers.txt" , "w")
f2.write(str(kmers))

# set up the dictionary
# key = k-2mer (basically the start of the kmer)
# value = k-1mer 

my_dict = {}
for key in keys:
	my_dict[key] = []

# add the kmers into the dictionary
for kmer in kmers:
	head = kmer[0:len(kmer)-1]
	#if kmer not in my_dict[head]:
	my_dict[head].append(kmer)

# pass through dictionary to create the edges
answer = open("answer.txt", "w")
done_already = []
for kmer in kmers:
	if kmer not in done_already:
		tail = kmer[1:len(kmer)]
		my_string = create_string(kmer, tail, my_dict)
		answer.write(my_string)
		done_already.append(kmer)




