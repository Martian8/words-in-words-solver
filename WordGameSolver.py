success = False
while success != True:
    Word = input("Type your word here (max 15 letters)  ").lower()
    # Ends program if no word has been selected or it's too long
    if Word.isalpha() and len(Word) < 16:
        success = True
    else:
        print("Please insert a word up to 15 letters long")

# Variables
Word = [char for char in Word]
File = open("Words.txt", "r")
WordList = File.read()
File.close()
WordList = WordList.split(" ")
loop = 0
while loop < len(WordList):
    WordList[loop] = WordList[loop].split(",")
    loop += 1
Results = []
for wordlength in WordList:
    if len(wordlength[0]) <= len(Word):
        for word in wordlength:
            fits = True
            for char in word:
                try:
                    Word.index(char)
                except:
                    fits = False
            if fits == True:
                Results.append(word)
# Double Up word remover
Results = list(set(Results))

# self remover
try:
    Results.remove(''.join(Word))
except:
    0
# Double Up letter remover
LetterNumbers = ['' for char in Word]
loop = 0
while loop < len(LetterNumbers):
    LetterNumbers[loop] = Word.count(Word[loop])
    loop += 1
loop = 0
while loop < len(Results):
    numberInResult = 0
    try:
        for char in Results[loop]:
            numberInResult = Results[loop].count(char)
            if numberInResult > LetterNumbers[Word.index(char)]:
                Results.remove(Results[loop])
                loop -= 1
    except:
        0
    loop += 1


Mode = input("If you would like to sort by length type Y  ").lower()
if Mode == "y":
    Results.sort(key=len)
else:
    Results.sort()
for result in Results:
    print(result)
print(len(Results))
