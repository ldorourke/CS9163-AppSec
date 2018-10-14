There is a shell file in this directory to run the commands. Simply run: 

	./RunSpellChecker

This will run the following commands 
	
	javac SpellChecker.java
	java SpellChecker

The spell checker first goes through a file with several spelling mistakes and outputs the original file as well as the misspelled words. It then goes through the Declaration of Independence, which has no spelling mistakes. The files can be found in the data folder.

	declarationofindependence.txt
	spellingmistakes.txt
	words.txt

The words.txt file is a dictionary with (mostly) all the words in the English dictionary. It was found here: https://github.com/dwyl/english-words/blob/master/words.txt