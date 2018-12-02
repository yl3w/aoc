# boxIds = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
# boxIds = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

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

print('Computed checksum is ' + str(computeChecksum(boxIds)))

def computeDifference(idOne, idTwo):
	if len(idOne) != len(idTwo):
		raise ValueError('Length of "' + idOne + '" does not match "' + idTwo + '"')

	difference = 0
	for index in range(0, len(idOne)):
		if idOne[index] != idTwo[index]:
			difference += 1

	return difference

def commonSequence(idOne, idTwo):
	if len(idOne) != len(idTwo):
		raise ValueError('Length of "' + idOne + '" does not match "' + idTwo + '"')

	sequence = ''
	for index in range(0, len(idOne)):
		if idOne[index] == idTwo[index]:
			sequence += idOne[index]

	return sequence

def findBoxes(boxIds):
	for idOne in boxIds:
		for idTwo in boxIds:
			if idOne == idTwo:
				continue

			difference = computeDifference(idOne, idTwo)
			if difference == 1:
				return commonSequence(idOne, idTwo)

	raise Exception("Something went wrong with the input or the logic")

print('Common sequence is ' + findBoxes(boxIds))
