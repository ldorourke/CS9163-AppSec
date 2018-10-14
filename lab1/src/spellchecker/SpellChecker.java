
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;
import java.lang.RuntimeException;
import java.lang.StringBuilder;
import java.io.FileReader;
import java.io.BufferedReader;


/**
* A Simple Spell Checker class.
*/
public class SpellChecker {

    private static final String SPACE = " ";
    private static final String HYPHEN = "-";
    private static final String EMPTY_STRING = "";
    private static final String DICTIONARY_FILE = "../data/words.txt"; 
	private static final String MISTAKE_FILE_NAME = "../data/spellingmistakes.txt";
    private static final String NO_MISTAKE_FILE_NAME = "../data/declarationofindependence.txt";
    private static final String REGEX_FOR_REPLACEMENT = "[^a-z\\sA-Z]";
    
    private static Set<String> dictionary;

	
    /**
    * Main function. Entry point to the class.
    * @param args Command Line input
    */
	public static void main(String[] args) {
        createDictionary();
		List<String> mistakeFileLines = getStringOfFile(MISTAKE_FILE_NAME);
        List<String> spellingMistakes = spellCheck(mistakeFileLines);
        formatOutput(spellingMistakes);

        List<String> noMistakeFileLines = getStringOfFile(NO_MISTAKE_FILE_NAME);
        List<String> noSpellingMistakes = spellCheck(noMistakeFileLines);
        formatOutput(noSpellingMistakes);

	}


    /**
    * Creates a dictionary. words.txt found on this Github:
    * https://github.com/dwyl/english-words/blob/master/words.txt
    */
    private static void createDictionary() {
        dictionary = new HashSet<>();
        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(DICTIONARY_FILE))) { 
            String word; 
            while ((word = bufferedReader.readLine()) != null) {
                dictionary.add(word.toLowerCase());
            }
        }
        catch (Exception e) {
            throw new RuntimeException(e);
        }

    }


    /**
    * Returns the lines of each file as a List of Strings.
    * @param fileName The name of the file 
    * @return A List of Strings
    */
    private static List<String> getStringOfFile(String fileName) {
    	try (BufferedReader bufferedReader = new BufferedReader(new FileReader(fileName))) { 
    		String fileLine;
            System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~ORIGINAL FILE~~~~~~~~~~~~~~~~~~~~~~~~~~");
            List<String> allLines = new ArrayList<>();
    		while ((fileLine = bufferedReader.readLine()) != null) {
                System.out.println(fileLine);
                fileLine = fileLine.replace(HYPHEN, SPACE);
    			allLines.add(fileLine);
    		}
            return allLines;     		
    	}
    	catch (Exception e) {
    		throw new RuntimeException(e);
    	}

    }


    /**
    * Splits each line by the space.
    * @param fileLines List of lines in the file
    * @return the incorrectly spelt words
    */
    private static List<String> spellCheck(List<String> fileLines) {
    	
        List<String> spellingMistakes = new ArrayList<>();
        for (String line : fileLines) {
            String[] splitLine = line.split(SPACE);
            for (String word : splitLine) {
                word = word.replaceAll(REGEX_FOR_REPLACEMENT, EMPTY_STRING);
                if (!checkWord(word)) {
                    spellingMistakes.add(word);
                }
            }
        }
        return spellingMistakes;
    }


    /**
    * Checks if the current word is in the dictionary.
    * @param word the word we are interested in
    * @return true or false
    */
    private static boolean checkWord(String word) {
        return (dictionary.contains(word.toLowerCase()) ?  true :  false);
    }


    /**
    * Format the output with the mistakes made.
    * @param spellingMistakes the mistakes in the file
    */
    private static void formatOutput(List<String> spellingMistakes) {
        System.out.println("\n~~~~~~~~~~~~~~~~~~~~~~~~~~MISTAKES~~~~~~~~~~~~~~~~~~~~~~~~~~");
        System.out.println(spellingMistakes.size()+ " mistakes in the file:");
        System.out.println(spellingMistakes);
    }

}
