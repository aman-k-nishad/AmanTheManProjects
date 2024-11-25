"""
Multi-Language Detection System
Author: Aman K Nishad

This program detects the language of input text among English, German, Swedish, Russian, and Hindi.
It uses dictionary-based matching and calculates the percentage of words matched in each language.

Note: The github repository does not entertain files over 25 mb and thus the "german.txt" file is not uploaded.
"""

# Character sets for different languages
EnglishU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
German = "äöüß"
Swedish = "åäö"
RUSSIAN = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ENGLISH = EnglishU + EnglishU.lower() + ' \t\n'
GERMAN = ENGLISH + German + German.upper() + ' \t\n'
SWEDISH = ENGLISH + Swedish + Swedish.upper() + ' \t\n'
HINDI = "अआइईउऊऋएऐओऔंःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह" + ' \t\n'
UNIFIEDCORPUS = RUSSIAN + ENGLISH + SWEDISH + GERMAN + HINDI

def dictionaries():
   """Initialize all language dictionaries."""
   Eng()
   #Ger()
   Swe()
   Rus()
   Hin()

def Eng():
   """
   Load English dictionary from file.
   Returns:
       list: List of English words
   """
   openEngFile = open('english.txt')
   engWords = []
   for word in openEngFile.read().split('\n'):
       engWords.append(word)
   openEngFile.close()
   return engWords

# def Ger():
#    """
#    Load German dictionary from file.
#    Returns:
#        list: List of German words
#    """
#    openGerFile = open('german.txt')
#    gerWords = []
#    for word in openGerFile.read().split('\n'):
#        gerWords.append(word.upper())
#    openGerFile.close()
#    return gerWords

def Swe():
   """
   Load Swedish dictionary from file.
   Returns:
       list: List of Swedish words
   """
   openSweFile = open('swedish.txt')
   sweWords = []
   for word in openSweFile.read().split('\n'):
       sweWords.append(word.upper())
   openSweFile.close()
   return sweWords

def Rus():
   """
   Load Russian dictionary from file.
   Returns:
       list: List of Russian words
   """
   openRusFile = open('russian.txt')
   rusWords = []
   for word in openRusFile.read().split('\n'):
       rusWords.append(word.upper())
   openRusFile.close()
   return rusWords

def Hin():
   """
   Load Hindi dictionary from file.
   Returns:
       list: List of Hindi words
   """
   openHinFile = open('hindi.txt')
   hinWords = []
   for word in openHinFile.read().split('\n'):
       hinWords.append(word)
   openHinFile.close()
   return hinWords

def LangDetect(text, matchPercentage):
   """
   Detect the language of input text.
   
   Args:
       text (str): Input text to analyze
       matchPercentage (float): Threshold percentage for language detection
       
   Returns:
       str: Detected language or "Unknown language!"
   """
   message = text.upper()
   sentence = removeNonLetters(message)
   theSentence = sentence.split()
   #checkGerman = gerDetect(text)*100
   checkSwedish = sweDetect(text)*100
   checkEnglish = engDetect(text)*100
   checkRussian = rusDetect(text)*100
   checkHindi = hinDetect(text)*100

   if checkEnglish >= matchPercentage:
       return "English"
#    elif checkGerman >= matchPercentage:
#        return "German"
   elif checkSwedish >= matchPercentage:
       return "Swedish"
   elif checkHindi >= matchPercentage:
       return "Hindi"
   elif checkRussian >= matchPercentage:
       return "Russian"
   else:
       return "Unknown language!"

def dataset_for_lang_detect(text):
   """
   Prepare text for language detection by converting to uppercase and splitting into words.
   
   Args:
       text (str): Input text
   
   Returns:
       list: List of words from the input text
   """
   message = text.upper()
   sentence = removeNonLetters(message)
   theSentence = sentence.split()
   return theSentence

def removeNonLetters(text):
   """
   Remove all characters that aren't in the unified corpus.
   
   Args:
       text (str): Input text
       
   Returns:
       str: Cleaned text containing only valid characters
   """
   lettersOnly = []
   unidentified = []
   for charecter in text:
       if charecter in UNIFIEDCORPUS:
           lettersOnly.append(charecter)
       else:
           unidentified.append(charecter)
   return ''.join(lettersOnly)

# def gerDetect(sentence):
#    """
#    Calculate the percentage of German words in the text.
   
#    Args:
#        sentence (str): Input text
       
#    Returns:
#        float: Percentage of German words matched
#    """
#    matches = 0
#    for word in sentence:
#        if word in Ger():
#            print('Word matched in German: ', word)
#            matches += 1
#    stats = matches/len(sentence)
#    return stats*100

def sweDetect(sentence):
   """
   Calculate the percentage of Swedish words in the text.
   
   Args:
       sentence (str): Input text
       
   Returns:
       float: Percentage of Swedish words matched
   """
   matches = 0
   for word in sentence:
       if word in Swe():
           print('Word matched in Swedish: ', word)
           matches += 1
   stats = matches/len(sentence)
   return stats*100

def rusDetect(sentence):
   """
   Calculate the percentage of Russian words in the text.
   
   Args:
       sentence (str): Input text
       
   Returns:
       float: Percentage of Russian words matched
   """
   matches = 0
   for word in sentence:
       if word in Rus():
           print('Word matched in Russian: ', word)
           matches += 1
   stats = matches/len(sentence)
   return stats*100

def engDetect(sentence):
   """
   Calculate the percentage of English words in the text.
   
   Args:
       sentence (str): Input text
       
   Returns:
       float: Percentage of English words matched
   """
   matches = 0
   for word in sentence:
       if word in Eng():
           print('Word matched in English: ', word)
           matches += 1      
   stats = matches/len(sentence)
   return stats*100

def hinDetect(sentence):
   """
   Calculate the percentage of Hindi words in the text.
   
   Args:
       sentence (str): Input text
       
   Returns:
       float: Percentage of Hindi words matched
   """
   matches = 0
   for word in sentence:
       if word in Hin():
           print('Word matched in Hindi: ', word)
           matches += 1
   stats = matches/len(sentence)
   return stats*100

def main():
   """
   Main function to run the language detection program.
   Prompts user for input text and detection threshold.
   """
   print("Welcome to Multi-Language Detection System")
   print("Supported languages: English, German, Swedish, Russian, Hindi")
   print("-" * 50)
   
   while True:
       # Get input text from user
       text = input("\nEnter the text to analyze (or 'quit' to exit): ")
       if text.lower() == 'quit':
           break
           
       # Get threshold percentage from user
       while True:
           try:
               threshold = float(input("Enter the detection threshold percentage (1-100): "))
               if 1 <= threshold <= 100:
                   break
               print("Please enter a number between 1 and 100")
           except ValueError:
               print("Please enter a valid number")
       
       # Process the text
       try:
           detected_language = LangDetect(text, threshold)
           print(f"\nDetected Language: {detected_language}")
           
           # Print match percentages for each language
           print("\nMatch percentages:")
           print(f"English: {engDetect(text):.2f}%")
           #print(f"German: {gerDetect(text):.2f}%")
           print(f"Swedish: {sweDetect(text):.2f}%")
           print(f"Russian: {rusDetect(text):.2f}%")
           print(f"Hindi: {hinDetect(text):.2f}%")
           
       except Exception as e:
           print(f"An error occurred: {str(e)}")
           print("Please make sure all language dictionary files are present.")

if __name__ == "__main__":
   main()