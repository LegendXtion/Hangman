from tkinter import *
import random
from string import ascii_uppercase
from words import SplitWords
from tkinter.messagebox import showinfo
import sys
from animations import ANIMS

class ButtonWidget():
	def __init__(self, Letter, Row, Column, Master):
		self.x = Button(master=Master, text=Letter, font=('Arial', 16), width=5, command=self.letter_button, bg='black', fg='green')
		self.x.grid(row=Row, column=Column)
		self.Letter = Letter
		self.PRESSED_KEY = ''

	def letter_button(self):
		self.PRESSED_KEY+=self.Letter
				
		global ListWord, NonListWord, wrong_entry_var, guess_entry_var, livesRemaining, displaySelected, ANIMS, draw_text, AnimationNum
		ListWord2 = ListWord[::]
		if self.Letter in ListWord2:
			Index = ListWord.index(self.Letter)
			del ListWord2[Index]
			displaySelected[Index] = self.Letter
			word_label_var.set(' '.join(displaySelected))
			
		else:
			livesRemaining-=1
			draw_text.delete('1.0', 'end')
			draw_text.insert(END, ANIMS[AnimationNum])
			AnimationNum -= 1
			NonListWord.append(self.Letter)
			wrong_entry_var.set(' '.join(NonListWord))
			guess_entry_var.set(livesRemaining)

		if '_' not in displaySelected:
			showinfo('Game Completed', 'You SAVED Me!!')
			sys.exit()


		if livesRemaining == 0:
			showinfo('Game Over', 'You KILLED Me!!')
			sys.exit()


SelectedWord = random.choice(SplitWords)
lengthWord = len(SelectedWord)
displaySelected = ['_']*lengthWord
livesRemaining = 10
wrongGuess = ''
ListWord = list(SelectedWord)
NonListWord = []
AnimationNum = -1

root = Tk()
root.title('Hangman Gamme')
root.config(bg='purple')


# FRAME 1

word_frame = Frame(master=root)

word_label_var = StringVar()
word_label = Label(master=word_frame, font=("Arial", 25), width=30, fg='yellow', bg='purple', textvariable=word_label_var)
word_label_var.set(' '.join(displaySelected))
word_label.grid(row=0, column=0, columnspan=10)

word_frame.grid(row=0, column=0, columnspan=10)


# FRAME 2


middle_frame = Frame(master=root, bg='purple')

length_label = Label(master=middle_frame, text='Length', font=("Arial", 16), width=5, fg='black', bg='green')
length_label.grid(row=1, column=1)

length_entry_var = IntVar()
length_entry = Entry(master=middle_frame, width=5, textvariable= length_entry_var, font=('Arial', 16), bg='black', fg='red', justify='center')
length_entry_var.set(lengthWord)
length_entry.grid(row=1, column=2)

guess_label = Label(master=middle_frame, text='Guess Left', font=("Arial", 16), width=9, fg='black', bg='green')
guess_label.grid(row=1, column=3)

guess_entry_var = IntVar()
guess_entry = Entry(master=middle_frame, width=5, textvariable=guess_entry_var, font=('Arial', 16), bg='black', fg='red', justify='center')
guess_entry_var.set(livesRemaining)
guess_entry.grid(row=1, column=4)

wrong_label = Label(master=middle_frame, text='Wrong Guess', font=("Arial", 16), width=15, fg='black', bg='green')
wrong_label.grid(row=1, column=5)

wrong_entry_var = StringVar()
wrong_entry = Entry(master=middle_frame, width=18, textvariable=wrong_entry_var, font=('Arial', 16), bg='black', fg='red', justify='center')
wrong_entry_var.set(wrongGuess)
wrong_entry.grid(row=1, column=6)

middle_frame.grid(row=1, column=0, columnspan=10)


# FRAME 3


first_column = ascii_uppercase[:10]
second_column = ascii_uppercase[10:20]
third_column = ascii_uppercase[20:]

letter_frame = Frame(master=root, bg='purple')

for count, letter in enumerate(first_column):
	ButtonWidget(Letter=letter, Row=0, Column=count, Master=letter_frame)

for count, letter in enumerate(second_column):
	ButtonWidget(Letter=letter, Row=1, Column=count, Master=letter_frame)

for count, letter in enumerate(third_column):
	ButtonWidget(Letter=letter, Row=2, Column=count+2, Master=letter_frame)


letter_frame.grid(row=3, column=0, columnspan=10, rowspan=3)


# FRAME 4


draw_frame = Frame(master=root)

draw_text = Text(master=draw_frame, width=25, height=15, fg='red', bg='black', font=("Consolas", 15, "bold"))
draw_text.insert(END, '')
draw_text.grid(row=1, column=1)

draw_frame.grid(row=0, column=11, rowspan=6)


root.mainloop()
