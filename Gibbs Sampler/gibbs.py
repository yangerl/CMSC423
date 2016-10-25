import random, math
from collections import deque
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
	my_probs = []
	score = 1.0

	i = 0
	while (i <= len(seq) - k):
		# 1st case special, no reuse capabilities
		if i == 0:
			for j in range(0,k):
				temp = entropy[j][seq[j]]
				score = score * temp
				my_probs.append(temp)
			my_probs = deque(my_probs)
			scores.append(score)

		# other cases, reuse info 
		else:
			# divide by the entropy of previous
			previous = my_probs.popleft()
			score /= previous

			# update previous
			my_probs.append(entropy[k-1][seq[i+k-1]])

			# multiply by new entropy
			score *= entropy[k-1][seq[i+k-1]]
			scores.append(score)
		i += 1

	return scores

# turns scores into probabilities
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

# roll biased die
# used method to simulated a biased die from this resource:
# http://stackoverflow.com/questions/479236/how-do-i-simulate-biased-die-in-python

def roll_biased(probs):
    randRoll = random.random() # in [0,1)
    sum = 0
    result = 1
    for prob in probs:
        sum += prob
        if randRoll < sum:
            return prob





fname = "test.txt"
f = open(fname, 'r')
data = f.readline()
temp = data.split(" ")
k = int(temp[0])
t = int(temp[1])
N = int(temp[2])
lines = f.read().splitlines()

# randomly create first motif
best_Motif = []
first_motif = []
for dna_str in lines:
	start = random.randint(0, len(dna_str) - k)
	best_Motif.append(dna_str[(start):(start+k)])
	first_motif.append(dna_str[(start):(start+k)])

for i in range(0,N):
	remove = random.randint(0,t-1)
	# remove random line
	best_Motif[remove] = " "*len(best_Motif[remove])

	# calculate score
	my_scores = score_seq(lines[remove], calc_probability(best_Motif), k)
	
	# determine probabilities for kmers
	my_probs = probabilify(my_scores)
	
	# roll biased die
	# my_roll = my_probs.index(roll_biased(my_probs))

	# pick best
	best = my_probs.index(max(my_probs))


	# select random k-mer using weighted distribution
	curr_line = lines[remove]
	#my_kmer = curr_line[my_roll:my_roll+k]
	my_kmer = curr_line[best:best+k]
	best_Motif[remove] = my_kmer
	



print score_motif(best_Motif)
print score_motif(first_motif)
f = open('motif.txt', 'w')
for string in best_Motif:
	f.write(string+"\n")

