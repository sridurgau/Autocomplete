import operator
Count = {}
words = []



with open('word_search.tsv') as file:
	for row in file:
		# splitting into word
		word, frequency = row.split('\t')
		#insert word as key and frequency as value into a dictionary
		Count[word] = int(frequency.strip())
		words.append(word)


#check the input text is present in any word of words list.
def searchwords(letter):
	results = []
	for word in words:
		if letter in word:
			results.append(word)
	return results


# sort the words based on constrains( search keyword.
def sortwords(results, incompleteWord):
	wordresults = [(result, result.find(incompleteWord), Count[result], len(result)) for result in results]
	wordresults.sort(key=operator.itemgetter(1))
	wordresults.sort(key=operator.itemgetter(3))
	searchResults = [wordresult[0] for wordresult in wordresults][:25]
	return searchResults