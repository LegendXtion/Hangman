WORDS = '''

MASTER
WORK
HARD
REAL
GREAT
RAINBOW
EAT
GAMER
HANGMAN
WORDS
DATE
MONDAY
TUESDAY
SUNDAY
QUEST
ACTION
SMARTPHONE
LATER
BOY
GIRL
MAN
WOMAN



'''



SplitWords = []

for word in WORDS.split('\n'):
	if word:
		for letter in word:
			if word.count(letter)>1:
				break
		else:
			SplitWords.append(word)
