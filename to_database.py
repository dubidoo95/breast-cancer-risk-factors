import os
import sqlite3
import pandas as pd

# data 불러오기
dir = "./dataset/"
train = pd.read_csv(dir+"train.csv")
val = pd.read_csv(dir+"validation.csv")
test = pd.read_csv(dir+"test.csv")

# sqlite3 열기

DB_FILENAME = 'data.db'
DB_FILEPATH = os.path.join(dir, DB_FILENAME)

conn = sqlite3.connect(DB_FILEPATH)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS train;")  
cur.execute("DROP TABLE IF EXISTS validation;")  
cur.execute("DROP TABLE IF EXISTS test;")  

# table 생성
create_train = """
                CREATE TABLE train(
                    age_group_5_years VARCHAR(32),
                    race_eth VARCHAR(32),
                    first_degree_hx VARCHAR(32),
                    age_menarche VARCHAR(32),
                    age_first_birth VARCHAR(32),
                    BIRADS_breast_density VARCHAR(32),
                    current_hrt	VARCHAR(32),
                    menopaus VARCHAR(32),
                    bmi_group VARCHAR(32),
                    biophx VARCHAR(32),
                    breast_cancer_history VARCHAR(32),
                    count INTEGER);"""
create_val = """
                CREATE TABLE validation(
                    age_group_5_years VARCHAR(32),
                    race_eth VARCHAR(32),
                    first_degree_hx VARCHAR(32),
                    age_menarche VARCHAR(32),
                    age_first_birth VARCHAR(32),
                    BIRADS_breast_density VARCHAR(32),
                    current_hrt	VARCHAR(32),
                    menopaus VARCHAR(32),
                    bmi_group VARCHAR(32),
                    biophx VARCHAR(32),
                    breast_cancer_history VARCHAR(32),
                    count INTEGER);"""   
create_test = """
                CREATE TABLE test(
                    age_group_5_years VARCHAR(32),
                    race_eth VARCHAR(32),
                    first_degree_hx VARCHAR(32),
                    age_menarche VARCHAR(32),
                    age_first_birth VARCHAR(32),
                    BIRADS_breast_density VARCHAR(32),
                    current_hrt	VARCHAR(32),
                    menopaus VARCHAR(32),
                    bmi_group VARCHAR(32),
                    biophx VARCHAR(32),
                    breast_cancer_history VARCHAR(32),
                    count INTEGER);"""                                  

cur.execute(create_train)
cur.execute(create_val)
cur.execute(create_test)

# database에 data 입력
for i in range(len(train)):
    cur.execute(f"""INSERT INTO train(
                    age_group_5_years, race_eth, first_degree_hx, age_menarche,
                    age_first_birth, BIRADS_breast_density, current_hrt,
                    menopaus, bmi_group, biophx, breast_cancer_history, count)
                    VALUES('{train.iloc[i][0]}', '{train.iloc[i][1]}','{train.iloc[i][2]}', '{train.iloc[i][3]}',
                    '{train.iloc[i][4]}', '{train.iloc[i][5]}', '{train.iloc[i][6]}', '{train.iloc[i][7]}',
                    '{train.iloc[i][8]}', '{train.iloc[i][9]}',' {train.iloc[i][10]}','{train.iloc[i][11]}');""")
for i in range(len(val)):
    cur.execute(f"""INSERT INTO validation(
                    age_group_5_years, race_eth, first_degree_hx, age_menarche,
                    age_first_birth, BIRADS_breast_density, current_hrt,
                    menopaus, bmi_group, biophx, breast_cancer_history, count)
                    VALUES('{val.iloc[i][0]}', '{val.iloc[i][1]}','{val.iloc[i][2]}', '{val.iloc[i][3]}',
                    '{val.iloc[i][4]}', '{val.iloc[i][5]}', '{val.iloc[i][6]}', '{val.iloc[i][7]}',
                    '{val.iloc[i][8]}', '{val.iloc[i][9]}',' {val.iloc[i][10]}','{val.iloc[i][11]}');""")
for i in range(len(test)):
    cur.execute(f"""INSERT INTO test(
                    age_group_5_years, race_eth, first_degree_hx, age_menarche,
                    age_first_birth, BIRADS_breast_density, current_hrt,
                    menopaus, bmi_group, biophx, breast_cancer_history, count)
                    VALUES('{test.iloc[i][0]}', '{test.iloc[i][1]}','{test.iloc[i][2]}', '{test.iloc[i][3]}',
                    '{test.iloc[i][4]}', '{test.iloc[i][5]}', '{test.iloc[i][6]}', '{test.iloc[i][7]}',
                    '{test.iloc[i][8]}', '{test.iloc[i][9]}',' {test.iloc[i][10]}','{test.iloc[i][11]}');""")                    
conn.commit()
conn.close()