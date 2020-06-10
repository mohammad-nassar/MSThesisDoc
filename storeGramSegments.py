import cx_Oracle
import logging

"""
Execution sequence: 2

This is the second python file to be executed.
-Read the file which contains all words from all corpora: "Tokenized_all_v5.txt"
-Store each word in the file in the database table LRT_CORPUS@LRT schema
"""

"""
Psedocode

conn=getDBConnection(connectionString)
readNGramSegmentFile(filePath)
    insert segement into DB (conn, filePath)
close file
close DB connection

"""

class DB_CONTROL:
    def __init__(self):
        print("created")

    def INSERT_WORDS(this):
        ipaddress = 'localhost'
        username = 'LRT'
        password = 'Dec$$2020'
        port = '1521'
        tnsname = 'ORCLM'

        try:
            conn = cx_Oracle.connect(username + '/' + password + '@' + ipaddress + ':' + port + '/' + tnsname,
                                     encoding='UTF-8', nencoding='UTF-8')
        except Exception:
            logging.error("Database Connection Error")
            raise

        cur = conn.cursor()
        ProcessedDSPath = "C:\\Users\\mohammad.nassar\\PycharmProjects\\storeData\\ProcessedDS\\"
        with open(ProcessedDSPath + "ngram_file.txt", encoding='utf-8') as NGram_File:
            data_lines = NGram_File.readlines()
            for line in data_lines:
                words = line.split()
                for word in words:
                    word = word.replace("]", "").replace(";", "").replace("[", "").replace("،", "").replace(",",
                                                                                                            "").replace(
                        "'", "").replace(":", "").replace(".", "").replace("?", "").replace(")", "").replace("(", "")
                    try:
                        query = ""
                        """
                        if len(word) == 6:
                            print(word)
                            print(len(word))
                            query = u"INSERT INTO lrt_6_gram(gram) VALUES('" + word + "')"
                            cur.execute(query)
                            conn.commit()
                       
                        if len(word) == 8:
                            print(word)
                            print(len(word))
                            query = u"INSERT INTO lrt_8_gram(gram) VALUES('" + word + "')"
                            cur.execute(query)
                            conn.commit()
                         
                        if len(word) == 9:
                            print(word)
                            print(len(word))
                            query = u"INSERT INTO lrt_9_gram(gram) VALUES('" + word + "')"
                            cur.execute(query)
                            conn.commit()
                        """
                        if len(word) == 3:
                            print(word)
                            print(len(word))
                            query = u"INSERT INTO lrt_3_gram(gram) VALUES('" + word + "')"
                            cur.execute(query)
                            conn.commit()
                    except Exception as e:
                        content = 'not connected'
                        print(e)

        NGram_File.close()

        cur.close()
        conn.close()


ins = DB_CONTROL()
ins.INSERT_WORDS()
