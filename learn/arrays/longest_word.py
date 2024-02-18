def longestWord(sen: str) -> str:
	"""
	iterate through the loop, check if each char is 
	a alphabet and not a space, 

	create a key of the word by appending one letter ata time
	and the length as the value in a dict

	find the longest value and get the key

	"""
	len_of_word = {}
	temp = ""
	for i in sen:
		if i.isalpha():
			temp = temp+i
		if i == " ":
			len_of_word[temp] = len(temp)
			temp = ""
	len_of_word[temp] = len(temp)
	temp = ""

	return max(len_of_word.keys())

			
   
    
def LongestWord2(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha() or letter.isnumeric():
        nw += letter
      else :
        nw += " "
    return max(nw.split(),key=len)

print(LongestWord2("i am a genius sayaji"))



