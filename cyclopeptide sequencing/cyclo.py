AMINO_ACIDS = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def expand(candidates):
	answer = []
	for candidate in candidates:
		for acid_mass in AMINO_ACIDS:
			temp_candidate = candidate + [acid_mass]
			answer.append(temp_candidate)
	return answer

def getSpectrum2(candidate):
	subPeptides = []
	for i in range(0, len(candidate)):
		for j in range(0, len(candidate)-i):
			subPeptides.append(candidate[i:i+j+1])

	spectrum = peptideSummer(subPeptides, [0])
	spectrum.sort()
	return spectrum

def peptideSummer(peptides, spectrum):
	for pep in peptides:
		mass_sum = 0 
		for mass in pep:
			mass_sum += mass
		spectrum.append(mass_sum)
	return spectrum

def getSpectrum(candidate):
	subPeptides = []
	subPeptides.append(candidate)
	extendedCandidate = candidate

	if len(candidate) > 2:
		extendedCandidate = extendedCandidate + candidate[0:len(candidate)-2]
	for i in range(0, len(candidate)):
		for j in range(0, len(candidate)-1):
			subPeptides.append(extendedCandidate[i:i+j+1])
	spectrum = peptideSummer(subPeptides, [0])
	spectrum.sort()
	return spectrum

def trim(candidates, spectrum):
	answer = []
	for candidate in candidates:
		my_spectrum = getSpectrum2(candidate)

		given = []+(spectrum)
		checker = True
		for mass in my_spectrum:
			if mass in given:
				given.remove(mass)
			else:
				checker = False
				break
		if checker:
			answer.append(candidate)
	return answer


fname = "rosalind_ba4e.txt"
file = open(fname, "r")
temp = file.read().split(" ")

# convert strings to ints
spectrum = []
for string in temp:
	spectrum.append(int(string))

candidates = [[]]
answer = []

# while there are candidates
while candidates:
	candidates = expand(candidates)

	matches = []
	for candidate in candidates:
		spec = getSpectrum(candidate)
		if(spec == spectrum):
			matches.append(candidate)

	for item in matches:
		answer.append(item)
	candidates = trim(candidates, spectrum)

answerfile = open("answer.txt", "w")
print answer
for peptide in answer:
	string = ""
	for thing in peptide:
		thing = str(thing)
		string = string + thing + "-"
	answerfile.write(string[0:len(string)-1]+"\n")

