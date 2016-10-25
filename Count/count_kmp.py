import timeit

# kmp algorithm for counting matches in text
fname = 'randomdna.txt'
f = open(fname, 'r')
text = f.readline()
pattern = f.readline()
# fix pattern indexing somehow has an extra null chracter eg AAAAA-nul- intead of AAAAA
if pattern[len(pattern)-1] == "\n":
    pattern = pattern[0:len(pattern)-1]
p_size = len(pattern)
print pattern
# start timer after file preprocessing, includes time to build sp array
start_time = timeit.default_timer()
# t_size = len(text)
# compute SP array
sp = [0]  # Base case
for curr_char in pattern[1:]:
    # set J to the latest element of SP array
    sp_val = sp[len(sp)-1]

    # iterate backwards until a match in the suffix and prefix is found
    # for current chracter
    while sp_val > 0 and curr_char != pattern[sp_val]:
        sp_val = sp[sp_val - 1]

    # check if there is a match with the 'potentially' first elements
    # in other words, check if the current character matches the cahracter that 
    # causes the while loop to break. If so then add 1 to this SP value
    if curr_char == pattern[sp_val]:
        sp_val += 1
    sp.append(sp_val)
# define sp[0] = -1 for easy manipulation during mismatches
spbuilt = timeit.default_timer()
sp[0] = 0
matches = 0
char_matches = 0
t_index = 0
p_index = 0

# begin pattern matching walkthrough
while (p_index + t_index < len(text)):
    if text[t_index + p_index] != pattern[p_index]:
        if (p_index == 0):
            p_index = 0   
            t_index = t_index + p_index + 1
        else:
            t_index = t_index + p_index - sp[p_index-1]
            p_index = 0
    elif (p_index == p_size - 1):
        matches = matches + 1
        t_index = t_index + 1
        p_index = 0
    else:
        p_index = p_index + 1


print matches
print "runtime: " + str(timeit.default_timer()-start_time)




