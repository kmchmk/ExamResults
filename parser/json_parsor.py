from asyncio.windows_events import NULL
import sqlite3
import json

full_list = []
file = open("../results/2022/results_2022.txt", "r")

line_count = 0
for line in file.readlines():
    full_list.append(json.loads(line))
    line_count += 1

print("lines in txt - " + str(line_count))

# Join/Create DB
conn = sqlite3.connect('result_db.db')

# Delete RESULT table
conn.execute('''DROP TABLE RESULT;''')

# Create RESULT table
conn.execute('''CREATE TABLE RESULT
         (
         INDEX_NO       INT(6)  PRIMARY KEY,
         NIC            INT(12),
         NAME           VARCHAR(100),
         SUB1_NAME      VARCHAR(50),
         SUB1_RESULT    VARCHAR(1),
         SUB2_NAME      VARCHAR(50),
         SUB2_RESULT    VARCHAR(1),
         SUB3_NAME      VARCHAR(50),
         SUB3_RESULT    VARCHAR(1),
         SUB4_NAME      VARCHAR(50),
         SUB4_RESULT    VARCHAR(1),
         SUB5_NAME      VARCHAR(50),
         SUB5_RESULT    VARCHAR(1),
         ZSCORE         DECIMAL(7,4),
         DISTRCT_RANK   INT(6),
         ISLAND_RANK    INT(6)
         );''')


# count = 1
for result in full_list:
    # if count > 10000:
    #     break

    try:
        student_nic = result["nic"]
        student_index_no = result["indexNo"]
        if(student_index_no == None):
            # print(result)
            break
        student_name = result["name"]
        student_zScore = result["zScore"]
        student_districtRank = result["districtRank"]
        student_islandRank = result["islandRank"]
        
        subject_names = []
        subject_results = []
        for i in range(5):
            try:
                subject_names.append(result["subjectResults"][i]["subjectName"])
                subject_results.append(result["subjectResults"][i]["subjectResult"])
            except:
                subject_names.append("NULL")
                subject_results.append("NULL")

        sql_insert = "INSERT INTO RESULT (NIC, INDEX_NO, NAME, SUB1_NAME, SUB1_RESULT, SUB2_NAME, SUB2_RESULT, SUB3_NAME, SUB3_RESULT, SUB4_NAME, SUB4_RESULT, SUB5_NAME, SUB5_RESULT, ZSCORE, DISTRCT_RANK, ISLAND_RANK) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(student_nic, student_index_no, student_name, subject_names[0], subject_results[0], subject_names[1], subject_results[1], subject_names[2], subject_results[2], subject_names[3], subject_results[3], subject_names[4], subject_results[4], student_zScore, student_districtRank, student_islandRank)

        conn.execute(sql_insert)
    except:
        print(result)
        pass
    # count += 1

conn.commit()

results = conn.execute('SELECT COUNT(*) FROM RESULT')
# results = conn.execute('SELECT * FROM RESULT')

for result in results:
    print("lines in db - " + str((result)))
conn.close()

