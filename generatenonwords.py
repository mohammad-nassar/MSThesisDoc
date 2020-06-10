# Importing defaultdict
from collections import defaultdict
import cx_Oracle
import logging
from os import walk
import pathlib
import random
"""
Psedocode

orthographic_dict   =    {  "ortho1" :  ['ح', 'ج', 'خ'],
                            "ortho2" :  ['ب',  'ت', 'ث'],
                            "ortho3" :  ['س',  'ص', 'ش'],
                            "ortho4" :  ['ذ',  'د'],
                            "ortho5" :  ['ض','ذ','ظ'],
                            "ortho6" :  ['ق','ك','ف'],
                            "ortho7" :  ['ع','غ']
                         }

phonological_dict   =    {  "phono1" :  ['ء','ه','خ','ح','ع','غ'],
                            "phono2" :  ['ت','ث','ج','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ق','ك','ل','ث','ي'],
                            "phono3" :  ['ب','ف','م','و'],
                            "phono4" :  ['أ','و','ي','ا'],

                        }

define Arabic orthographic characters list
define Arabic phonological characters list

conn=connectToWordsDB(conn)
GenerateNonWords(conn, tableName)
    WordsDataset=select words from tableName
    for word in WordsDataset
        generateOrthoNonWords(word)
        generatePhonoNonWords(word)
    endloop
endGenerateNonWords

generateOrthoNonWords(word)
    repalcePosition=generarteRandomNumber(minLimit=2, maxLimit=length(word))
    repalceChar=word(replacePosition)
    replaceOrthoList=orthoCharList(repalceChar)
    for char in orthographic_dict
        newNonWord=word.repalce(repalcePosition, char)
        insert into nonWordTable(newNonWord, repalcePosition, repalceChar, word)
    end loop
end generateOrthoNonWords
        

generatePhonoNonWords(word)
    epalcePosition=generarteRandomNumber(minLimit=2, maxLimit=length(word))
    repalceChar=word(replacePosition)
    replacePhonoList=phonoCharList(repalceChar)
    for char in phonological_dict
        newNonWord=word.repalce(repalcePosition, char)
        insert into nonWordTable(newNonWord, repalcePosition, repalceChar, word)
    end loop
end generatePhonoNonWords

"""

en=['a','b','c','d','e','f','g','h','i','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

orthographic_dict   =    {  "ortho1" :  ['ح', 'ج', 'خ'],
                            "ortho2" :  ['ب',  'ت', 'ث'],
                            "ortho3" :  ['س',  'ص', 'ش'],
                            "ortho4" :  ['ذ',  'د'],
                            "ortho5" :  ['ض','ذ','ظ'],
                            "ortho6" :  ['ق','ك','ف'],
                            "ortho7" :  ['ع','غ']
                         }

phonological_dict   =    {  "phono1" :  ['ء','ه','خ','ح','ع','غ'],
                            "phono2" :  ['ت','ث','ج','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ق','ك','ل','ث','ي'],
                            "phono3" :  ['ب','ف','م','و'],
                            "phono4" :  ['أ','و','ي','ا'],

                        }

def main():
    #getNonWords();
    getNonWords_db();

def getNonWords_db():
    ipaddress = 'localhost'
    username = 'LRT'
    password = 'Dec$$2020'
    port = '1521'
    tnsname = 'ORCLM'

    try:
        conn = cx_Oracle.connect(username + '/' + password + '@' + ipaddress + ':' + port + '/' + tnsname,
                                 encoding='UTF-8', nencoding='UTF-8')
        cur = conn.cursor()
        mylist=[]
        for i in range(10):
            records=cur.execute('SELECT id, WORD    FROM lrt_word_frequency ')
            reconn = 0
            for result in records:
                reconn +=1
                id=result[0]
                word=result[1]
                if len(word) < 3:
                    continue
                print("result",result[0])
                print(id)
                print(word)
                print("result", result[1])
                print("id=",id, "word=",word)
                word=str(word).replace(")","").replace("(","").replace("'","").replace(",","")
                print(str(result).replace(")","").replace("(","").replace("'","").replace(",",""))
                print("before calling", word)
                #generate_nonwords_ortho(id, word, conn)
                generate_nonwords_phono(id, word, conn)

    except Exception:
        logging.error("Database Connection Error")
        raise

def getNonWords():
    ProcessedDSPath = "C:\\Users\\mohammad.nassar\\PycharmProjects\\storeData\\ProcessedDS"
    print(ProcessedDSPath)
    for p in pathlib.Path(ProcessedDSPath).iterdir():
        if p.is_file():
            if p.name.strip().endswith(".txt") and p.name.strip() == "Tokenized_All_v5.txt":
                with open(p, encoding='utf-8') as f1:
                    data = f1.readlines()
                    for line in data:
                        words = line.split()
                        if words[0].isalpha():
                            for i in words[0]:
                                if i in en:
                                    break
                            print(words[0])
                            #generate_nonwords_ortho(words[0])
                            #break
                            #generate_nonwords_phono(words[0])
                f1.close()

    f1.close()

def getOrthoList(orthochar):
    for ortho in orthographic_dict.values():
        if orthochar in ortho:
                return ortho;

def getPhonoList(phonochar):
    for phono in phonological_dict.values():
        if phonochar in phono:
            return phono;

def generate_nonwords_ortho(id, ortho_word, db_conn):
    print("*******************    Orthoo   ****************")
    print("word", ortho_word)
    word_id=id
    print("length",ortho_word, len(ortho_word)-1)
    conn=db_conn
    print(conn)
    replace_index = random.randint(2, len(ortho_word)-1)
    print("replace_index",replace_index)
    word_list=[]
    word_list=ortho_word
    prefix = word_list[0:replace_index]
    postfix= word_list[replace_index+1 :: ]

    print("prefix", prefix)
    print("postfix", postfix)

    replace_char= word_list[replace_index]

    print("replace_char=" + replace_char)
    ortho_list=[]
    ortho_list  = getOrthoList(replace_char)
    print("ortho_list",ortho_list)
    print(type(ortho_list))

    if not ortho_list:
        print("list is empty")
    else:
        for ortho_char in ortho_list:
            if ortho_char != replace_char:
                 new_word_list=[]
                 new_word= prefix + ortho_char + postfix
                 new_word_list.append(new_word)
                 print("new_word_list", new_word_list)
                 print("new_word", ortho_word)
                 query = f"INSERT INTO lrt_nonwords (word_id, non_word, type, replace_char_index, replaced_char, prefix,ORIGINAL_CHAR, postfix) VALUES('{word_id}','{new_word}', 1,{replace_index},'{ortho_char}','{prefix}','{replace_char}','{postfix}')"
                 conn.cursor().execute(query)
                 conn.commit()
                 print(query)




def generate_nonwords_phono( id, phono_word, db_conn):
    print("*******************    Phonooooo   ****************")

    print("word", phono_word)
    word_id = id
    print("length", phono_word, len(phono_word) - 1)
    conn = db_conn
    replace_index = random.randint(2, len(phono_word) - 1)
    word_list = []
    word_list = phono_word
    prefix = word_list[0:replace_index]
    postfix = word_list[replace_index + 1::]
    replace_char = word_list[replace_index]

    phono_list = []
    phono_list = getPhonoList(replace_char)
    phono_list = getPhonoList(replace_char)

    if not phono_list:
        print("list is empty")
    else:
        for phone_char in phono_list:
            if phone_char != replace_char:
                new_word_list = []
                new_word = prefix + phone_char + postfix
                query = f"INSERT INTO lrt_nonwords (word_id, non_word, type, replace_char_index, replaced_char, prefix,ORIGINAL_CHAR, postfix) VALUES('{word_id}','{new_word}', 2,{replace_index},'{phone_char}','{prefix}','{replace_char}','{postfix}')"
                conn.cursor().execute(query)
                conn.commit()
                print(query)

if __name__ == "__main__":
    main()