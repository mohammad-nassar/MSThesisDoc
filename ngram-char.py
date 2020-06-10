"""
Execution sequence: 3
Word character n-gram generation is runnning here.
all character n-grams of each single word is stored in a list in a file named "ngram1.txt"
"""

import pathlib

"""
Pesedocode
readCorpusData(filePath)
for line in filePath
    ngramToken(line)
closeFile

ngramToken(word)
    TokenList.append(getTokensInWord)
    insertIntoNGramFile(TokenList)
    closeTokenListFile
        
"""
def ngram_token(word="فلسطين"):
    grams_list = []
    gram_rank = 2
    while gram_rank < len(word):
        for i in range(len(word) - 1):
            if len(word[i:i + gram_rank]) == gram_rank:
                grams_list.append(word[i:i + gram_rank])
        gram_rank = gram_rank + 1
    grams_list.append(word)
    FileAppender1 = open("C:\\Users\\mohammad.nassar\\PycharmProjects\\storeData\\ProcessedDS\\" + "ngram_file.txt",
                         "a", encoding='utf-8')
    FileAppender1.write(str(grams_list))
    FileAppender1.write("\n")
    FileAppender1.close()


def readFile():
    ProcessedDSPath = "C:\\Users\\mohammad.nassar\\PycharmProjects\\storeData\\ProcessedDS\\"
    print(ProcessedDSPath)
    for p in pathlib.Path(ProcessedDSPath).iterdir():
        if p.is_file():
            if p.name.strip().endswith(".txt") and p.name.strip() == "Tokenized_All_v5.txt":
                with open(p, encoding='utf-8') as f1:
                    data = f1.readlines()
                    for line in data:
                        words = line.split()
                        for word in words:
                            ngram_token(word)
    f1.close()


if __name__ == "__main__":
    readFile()
