def minsert(item, mlist):
	length = len(mlist)
	curr_index = 0

	for curr_index in range(0,length):
		if (mlist[curr_index] >= item):
			mlist.insert(curr_index, item)
			return mlist
	mlist.append(item)
	return mlist



fname = "rosalind_ba3a.txt"
f = open(fname, "r")
k = int(f.readline())
text = f.readlines()
text = text[0]

manswer = []
curr_index = 0
size = len(text)
answer = open("answer.txt", "w")
while curr_index < size-k:
	manswer = minsert(text[curr_index:curr_index+k], manswer)
	curr_index += 1

for string in manswer:
	answer.write(string+"\n")