import os
import random
import time


def word_loader(filename):
	lst = []
	with open(filename, 'r') as words:
		for word in words:
			lst.append(word.strip())
	return lst

def word_picker(word_lst):
	word = random.choice(word_lst)
	return word

def game(word_lst, max_time=5.0):
	score = 0

	while True:
		clear()

		before_time = time_check()
		word = word_picker(word_lst)

		ingame_display(word, score, max_time)
		user_word = input('--> ')
		
		after_time = time_check()
		total_time = after_time - before_time
		
		if total_time > max_time:
			print('\nToo late!')
			break
		if not checker(user_word, word):
			print('\nYou typed it wrong!')
			break
		
		score += points(total_time)
	
	return score

def clear():
	os.system('clear')

def ingame_display(word, score, max_time):
	print(f'Your score is: {score}')
	print(f'You have {max_time} seconds to type the word:\n\n{word}\n')
	pass

def time_check():
	time_now = round(time.time(), 3)
	return time_now

def checker(user_input, word):
	correct = False
	if user_input == word.lower():
		correct = True
	return correct

def points(total_time, multiplier=1000):
	points = round(total_time * multiplier)
	return points

def high_scores_loader(filename):
	high_scores = {}
	with open(filename, 'r') as f:
		for line in f:
			high_score = line.split()
			high_scores[high_score[0]] = high_score[1]
	return high_scores

def end_display(high_scores, player_score, new_hs=False):
	if new_hs == True:
		print('New high score!')
	print(f'Your score was {player_score}.\n')
	print('The high scores are:')
	for i, (initials, score) in enumerate(high_scores.items()):
		print(f'{i}. {initials} {score}')
		if i+1 == len(high_scores):
			print('')

def score_saver(filename, high_scores):
	with open(filename, 'w') as f:
		for i, (key, value) in enumerate(high_scores.items()):
			if i:
				f.write(f'\n{key} {value}')
			else:
				f.write(f'{key} {value}')


if __name__ == '__main__':
	words_file = '/usr/share/dict/web2'
	word_lst = word_loader(words_file)

	high_scores_file = 'high_scores.txt'
	hs_dict = high_scores_loader(high_scores_file)

	score = game(word_lst)
	end_display(hs_dict, score)