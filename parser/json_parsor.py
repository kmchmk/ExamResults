import sqlite3
import json

full_list = []
file = open("../results/2022/results_2022.txt", "r")

for line in file.readlines():
    full_list.append(json.loads(line))

# Join/Create DB
conn = sqlite3.connect('result_db.db')

# Delete RESULT table
conn.execute('''DROP TABLE RESULT;''')

# Create RESULT table
conn.execute('''CREATE TABLE RESULT
         (
         NIC            INT(12)         PRIMARY KEY,
         INDEX_NO       INT(6)          NOT NULL,
         NAME           VARCHAR(100)    NOT NULL,
         SUB1_NAME      VARCHAR(50),
         SUB1_RESULT    VARCHAR(1),
         SUB2_NAME      VARCHAR(50),
         SUB2_RESULT    VARCHAR(1),
         SUB3_NAME      VARCHAR(50),
         SUB3_RESULT    VARCHAR(1),
         ZSCORE         DECIMAL(5,4),
         DISTRCT_RANK   INT(6),
         ISLAND_RANK    INT(6)
         );''')


count = 0
for result in full_list:
    if count > 30:
        break
    try:
        sql_insert = "INSERT INTO RESULT (NIC, INDEX_NO, NAME, SUB1_NAME, SUB1_RESULT, SUB2_NAME, SUB2_RESULT, SUB3_NAME, SUB3_RESULT, ZSCORE, DISTRCT_RANK, ISLAND_RANK) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(result["nic"], result["indexNo"], result["name"], result["subjectResults"][
            0]["subjectName"], result["subjectResults"][0]["subjectResult"], result["subjectResults"][1]["subjectName"], result["subjectResults"][1]["subjectResult"], result["subjectResults"][2]["subjectName"], result["subjectResults"][2]["subjectResult"], result["zScore"], result["districtRank"], result["islandRank"])

        conn.execute(sql_insert)
    except:
        print(result)
    count += 1

# conn.commit()

results = conn.execute('SELECT COUNT(*) FROM RESULT')

for result in results:
    print(result)
conn.close()

print("Edited for testing")
