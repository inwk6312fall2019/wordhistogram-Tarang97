fin = open('2600-0.txt')
for line in fin:
	word = line.strip()

def rotate_letters(letter, n):
	if letter.isupper():
		start = ord('A')
	elif letter.islower():
		start = ord('a')
	else:
		start = ord(letter)
	letter_char = ord(letter)
	letter_diff = start + ((letter_char - start) % 26)
	return chr(letter_diff)

def rotate_pairs(word, n):
	new_words = ''
	for lett in word:
		new_lett = rotate_letters(word,n)
		new_words += new_lett
	return new_words

print(rotate_pairs(word, 3))

