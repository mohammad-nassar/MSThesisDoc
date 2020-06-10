from string import punctuation
import re
import pathlib


"""
Execution sequence: 1

This is the first python file to be executed.
-Get separated words from all corpus list and insert them in one file "Tokenized_all_v5.txt"
-generate all statistical file to hold word counts per corpus and acumalative total words "WordStatisticeFile"
"""

class DSPrepare:

    arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''

    ar = ['د', 'ج', 'ح', 'خ', 'ه', 'ع', 'غ', 'ف', 'ق', 'ث', 'ص', 'ض',
          'ذ', 'ش', 'س', 'ي', 'ب', 'ل', 'ا', 'أ', 'إ', 'ت', 'ن','م',
          'ك', 'ط', 'ظ', 'ز', 'و', 'ة', 'ى', 'آ', 'لا', 'ر', 'ؤ','ء'
          ]

    ar_tashkeel = ['ِ', 'ُ', 'ٓ', 'ٰ', 'ْ', 'ٌ', 'ٍ', 'ً', 'ّ', 'َ']
    """
    corpusList = ['1_corpus.txt',
                      '2_Watan.txt',
                      '3_Khaleej.txt',
                      '4_KACST.txt',
                      '5_aljazeera.txt',
                      '6_Tweets-ann.txt',
                      '7_Tweets-sharp.txt',
                      '8_Khaleej100.txt',
                      '9_KACST100.txt',
                      '10_Watan100.txt',
                      '11_aljazeera100.txt',
                      '12_rdi.txt',
                      '13_Books.txt',
                      '14_quran.txt',
                      '15_WikiNewsTruth.txt'
                      ]
    """
    """
    Psedocode
    
    readCorpusFiles(filePath)
        for fileName in filePath
            getLines(fileName)
    getLines(fileName)
        for line in fileName
            splitLineIntoWords(line)
    splitLineIntoWords(line)
        for word in line.split(whiteSpace)
        filterWord(word)
    filterword(word)
        if word not contains (char in arabic_punctuations)
            storeRealWordsInOneFile(word)
    storeRealWordsInOneFile(word)
        insertIntoMainCorpus(word)
    """
    def readFile(self):
        corpusPath="C:\\Users\\mohammad.nassar\\PycharmProjects\\MSProject\\MSThesis\\CorporaDS"
        ProcessedDSPath="C:\\Users\\mohammad.nassar\\PycharmProjects\\MSProject\\MSThesis\\ProcessedDS"
        WordStatisticeFile = open(ProcessedDSPath + "\\" + "WordStatisticeFile.txt" , 'a', encoding='utf-8')
        FileAppender_All_Tokenized = open(ProcessedDSPath + "\\" + "Tokenized_All_v5.txt", 'a', encoding='utf-8')
        TotalWordsCounter = 0

        for corpus_file in pathlib.Path(corpusPath).iterdir():
            fileWordsCounter = 0
            if corpus_file.is_file():
                if corpus_file.name.strip().endswith(".txt"):
                    FileAppender1 = open(ProcessedDSPath+"\\"+ "Tokenized_v5_"+corpus_file.name, "a")
                    with open(corpus_file, 'r+',newline='',  encoding='utf-8' ) as f1:
                        data = f1.readlines()
                        for line in data:
                            words = line.split()
                            for word in words:
                              if (word not in punctuation) and (word != '،') and (not word.isnumeric()) and not bool(
                                re.search(r'\d', word)) and len(word) > 2:
                                    print(word)
                                    FileAppender1.write(word.strip() + "\n")
                                    FileAppender_All_Tokenized.write(word.strip() + "\n")
                                    fileWordsCounter = fileWordsCounter + 1
                WordStatisticeFile.write("Total Words in file "+ "Tokenized_v5_"+ corpus_file.name + " = ")
                WordStatisticeFile.write(str(fileWordsCounter))
                WordStatisticeFile.write("\n")
                TotalWordsCounter=TotalWordsCounter+fileWordsCounter
            f1.close()
            FileAppender1.close()

        WordStatisticeFile.write("\n\n")
        WordStatisticeFile.write("Total Words in all file  = ")
        WordStatisticeFile.write(str(TotalWordsCounter))
        WordStatisticeFile.close()
        FileAppender_All_Tokenized.close()
r1 = DSPrepare()
r1.readFile()