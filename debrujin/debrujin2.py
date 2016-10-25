def my_break(kmer, k):
	return [kmer[0:k-1],kmer[1:k]]

def minsert(item, mlist):
	length = len(mlist)
	curr_index = 0
	for curr_index in range(0,length):
		if (mlist[curr_index] >= item):
			mlist.insert(curr_index, item)
			return mlist
	mlist.append(item)
	return mlist

fname = "rosalind_ba3d.txt"                                     
f = open(fname, "r")

k = int(f.readline())
text = f.readlines()
text = text[0]
curr_index = 0

my_dict = {}

while curr_index < len(text) - k:
	kmer = text[curr_index:curr_index+k]
	arr = my_break(kmer,k)
	
	if arr[0] not in my_dict.keys():
		my_dict[arr[0]] = [arr[1]]
	else:
		my_dict[arr[0]] = minsert(arr[1],my_dict[arr[0]])
	curr_index += 1

answer = open("answer.txt", "w")
keys = my_dict.keys()
keys.sort()
for key in keys:
	string = key + " -> "
	for kmer in my_dict[key]:
		string += kmer+","
	answer.write(string[0:len(string)-1]+"\n")
