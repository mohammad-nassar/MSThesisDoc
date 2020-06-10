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

conn=connectToDB(connectionString)
openMainCorpusFile(filePath)
for word in filePath
    insert word in tableName
close file
close connection

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
        with open(ProcessedDSPath + "Tokenized_All_v5.txt", encoding='utf-8') as Tokenized_File:
            data_lines = Tokenized_File.readlines()
            for line in data_lines:
                words = line.split()
                for word in words:
                    try:
                        cur.execute(u"INSERT INTO lrt_corpus(word) VALUES('" + word + "')")
                        conn.commit()
                    except Exception as e:
                        content = 'not connected'
                        print(e)

        Tokenized_File.close()

        cur.close()
        conn.close()


ins = DB_CONTROL()
ins.INSERT_WORDS()
