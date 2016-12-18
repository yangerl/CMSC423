inpt = [0,1,0,5,1,0,2,2,1]
length = len(inpt)
answer = [0] * length

for i in range(length-1, 0, -1):
	answer[i+inpt[i]-1] = inpt[i]
	print answer




