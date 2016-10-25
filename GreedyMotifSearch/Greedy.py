from collections import deque
def calc_probability(motif):
	transpose = map(list, zip(*motif))
	prob_array = []
	for char_list in transpose:
		score_dict = {
			# pseudocount so starts at 1 instead of 0
			"A" : 1,
			"C" : 1,
			"G" : 1,
			"T" : 1
		}

		for char in char_list:
			if char != " ":
				score_dict[char] += 1
		total_ntides = score_dict["A"] + score_dict["G"] \
			+ score_dict["C"] + score_dict["T"]

		score_dict["A"] = float(score_dict["A"])/float(total_ntides)
		score_dict["C"] = float(score_dict["C"])/float(total_ntides)
		score_dict["G"] = float(score_dict["G"])/float(total_ntides)
		score_dict["T"] = float(score_dict["T"])/float(total_ntides)

		prob_array.append(score_dict)
	return prob_array

def score_seq(seq, entropy, k):
	scores = []

	i = 0
	best_score = 0
	best_index = 0

	while (i <= len(seq) - k):
		score = 1.0

		for j in range(0,k):
			temp = entropy[j][seq[i+j]]
			score = score * temp

		scores.append(score)

		if score > best_score:
			best_index = i
			best_score = score
		i += 1

	return best_index

def score_motif(motif):
	transpose = map(list, zip(*motif))
	score = 0
	for char_list in transpose:
		score_dict = {
			"A" : 0,
			"C" : 0,
			"G" : 0,
			"T" : 0
		}

		for char in char_list:
			score_dict[char] += 1

		total_ntides = score_dict["A"] + score_dict["G"] \
			+ score_dict["C"] + score_dict["T"]

		freq = max(score_dict.values())
		score += total_ntides-freq

	return score

def probabilify(scores):
	temp = []
	answer = []
	my_sum = 0 
	for score in scores:
		temp.append(score)
		my_sum += score

	for temp1 in temp:
		answer.append(temp1/my_sum)
	return answer

fname = "rosalind_ba2e.txt"
f = open(fname, 'r')
data = f.readline()
temp = data.split(" ")
k = int(temp[0])
t = int(temp[1])
lines = f.read().splitlines()

best_motifs = []

for line in lines:
	best_motifs.append(line[0:k])
best_score = score_motif(best_motifs)
i = 0
while (i <= len(lines[0])-k):
	motif = []
	motif.append(lines[0][i:i+k])
	for j in range(1, t):
		
		prob = calc_probability(motif)

		score = score_seq(lines[j], prob, k)	
		motif.append(lines[j][score:score+k])

	m_score = score_motif(motif)

	if m_score < best_score:
		best_motifs = motif
		best_score =  m_score
	i += 1

print best_motifs

f = open("answer.txt", "w")
for string in best_motifs:
	f.write(string+"\n")
