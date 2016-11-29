


def getSubPeptides(candidate):
	subPeptides = [candidate]
	extendedCandidate = []
	if len(candidate) > 2:
		extendedCandidate = candidate[0:len(candidate)-2]


def getSpectrum(candidate, isLinear):
	subPeptides = getLinearSubPeptides(candidate) if isLinear else getSubPeptides(candidate)
	spectrum = [0]
	for subPeptide in subPeptides:
		sumMass = 0
		for mass in subPeptide:
			sumMass += mass
		spectrum.append(sumMass
	spectrum.sort(0)
	return spectrum

def check(candidates, spectrum):
	matchedCandidates = []
	for candidate in candidates:
		if getSpectrum(candidate, False) == spectrum:
			matchedCandidates.append(candidate)
	return matchedCandidates
def expand(candidates):
	expanded = []
	for candidate in candidates:
		for acid in AMINO_ACIDS:
			expandedC = [candidate].append(acid)
			expanded.append(expandedC)
	return expanded

def sequencing(spectrum):
	candidates = [[]]
	output = []

	while candidates:
		candidates = expand(candidates)
		toadd = check(candidates, spectrum)
		output = output + toadd
		candidates = trim(candidates, spectrum)

def toStringWithDelimiter(peptide, deli):
	str = ""
	for integer : peptide:
		str = str + str(integer) + deli
	return str[0:len(str)-1]

AMINO_ACIDS = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

fname = "test.txt"
file = open(fname, "r")
temp = file.read().split(" ")

# convert strings to ints
spectrum = []
for str in temp:
	spectrum.append(int(str))

result = sequencing(spectrum)

for peptide : result:
	print toStringWithDelimiter(peptide,"-")