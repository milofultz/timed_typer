Timed Type Overview
---

The program will ask you to type a word in a specific amount of time over and over until you mess up, calculating a score for you based on your speed.

Program will start by grabbing the dictionary of words
Program will pick a word at random and display it on the screen with the total time you have as it asks you to type it.
Once you hit return, program will tell you if you did it fast enough or not.
If you did, program will calculate a score based on how quickly you typed it.
If you didn't, program will take away one of your lives and player will get no score.
This will continue until all lives are lost. 
Program will display score at the end.
Program will save high scores so you can see who before you won.

Word Loader - Find and load the words so they can be used
	IN: words file
	OUT: list of strings
Picker - picks random word from words
	IN: list of strings
	OUT: string
In Game Display - display all elements on screen before turn begins
	IN: string (picker), int (score), string (time)
	OUT: none
Time Check - will check how long it took for user to type in word
	IN: none
	OUT: float of time
Checker - will check if the word was typed correctly
	IN: string, user input, string word
	OUT: Boolean
Points - Will determine how many points user gets
	IN: float of time
	OUT: int, score
Score Loader - Find and load high scores for display
	IN: file, scores
	OUT: dict, scores (name, score)
End Display - Display all elements on screen at the end
	IN: dict (score loader), int (score)
	OUT: none
Score Saver - Receive and save new high scores
	IN: int (score), string (name)
	OUT: file, scores

---

Word Loader:
	The program gets the filepath. The program finds the file at the filepath and opens it. The program copies all the words one by one from the file and adds them to a list. The list is then returned.

Picker - picks random word from words
	The program receives a list of N words. The program rolls a dice that is N sides and chooses the word found in that index of the list. The program returns that word.

In Game Display - display all elements on screen before turn begins
	The program receives the word to be typed, the user's score, and how long the user has to type the word. The program that displays those elements on the screen. 

Time Check - will check how long it took for user to type in word
	The program returns the exact time up to the thousandth of a second.

Checker - will check if the word was typed correctly
	The program receives the word that was typed and the word that was asked to be typed. The program compares the two and sees if they are an exact match or not. The program tells you if they are the same.

Points - Will determine how many points user gets
	The program receives a number and a multiplier. The program multiplies them together and returns a rounded number.

Score Loader - Find and load high scores for display
	The program receives a filepath. The program looks for the file at that filepath and opens the file. The program copies the file contents into a dictionary. The program returns a dictionary.

End Display - Display all elements on screen at the end
	The program receives the high scores and the last player's score. The program displays these on screen.

Score Saver - Receive and save new high scores
	IN: dict, high scores; string, filename
	OUT: file, scores
	The program receives a dictionary of high scores and a filepath. The program creates a new file or erases the content of whatever was previously at that filepath. The program copies these dictionary contents into the file.