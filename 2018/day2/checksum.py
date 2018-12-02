# boxIds = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

boxIds = []
with open('box_ids') as f:
	for line in f:
		boxIds.append(line)

def computeChecksum(boxIds):
	exactlyTwo = 0
	exactlyThree = 0
	for identifier in boxIds:
		identifier = identifier.lower()
		counts = {}
		for ch in identifier:
			count = counts.get(ch, 0)
			counts[ch] = count + 1


		countSet = set(counts.values())
		if 2 in countSet:
			exactlyTwo += 1
		if 3 in countSet:
			exactlyThree += 1

	return exactlyTwo * exactlyThree

print(computeChecksum(boxIds))
