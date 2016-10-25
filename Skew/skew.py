filename = "rosalind_ba1f.txt"
f = open(filename, 'r')
data = f.readline()
solution = []
skew = 0
for char in data:
	solution.append(skew)
	if char == 'C':
		skew = skew - 1
	elif char =='G':
		skew = skew + 1
	else:
		pass
min_skew_val = min(solution)
answer = ""
# add this so that if the value of (min_skew_val) doesnt exist, no error will be thrown
solution.append(min_skew_val)
end = len(solution)
sol_index = solution.index(min_skew_val)

while sol_index < end - 1:
	answer = answer + str(sol_index) + " "
	# so it wont get counted twice
	solution[sol_index] = min_skew_val + 1
	sol_index = solution.index(min_skew_val)
print answer


