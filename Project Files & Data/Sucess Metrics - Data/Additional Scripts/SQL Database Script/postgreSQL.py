# Pushes project data to an sql database - Big Data Challenge 2021 

import psycopg2
import pickle
import uuid
import csv
from csv import reader


def load_table(file_path, table_name, t_host, t_port, t_dbname, t_user, t_pw):

    conn = psycopg2.connect(host=t_host, port=t_port,
                            dbname=t_dbname, user=t_user, password=t_pw)
    cursor = conn.cursor()
    data = open(file_path, "r")

    for row in reader(data):

        id = str(uuid.uuid1())
        full_name = row[0]
        alias = row[1]
        external_alias = alias
        type = row[2]
        unit = row[3]
        period = "na"
        description = row[4]

        query = "INSERT INTO TABLENAME (CATAGORIES GO HERE) VALUES (%s);"
        data = (id, full_name, alias, external_alias,
                type, unit, period, description)

        cursor.execute(query, data)
        conn.commit()


file_path = "data_final.csv"
table_name = "NAME"
t_host = "ec2-2254-162-218-31.compute-1.amazonaws.com"
t_port = "54422"
t_dbname = "d7v02asa19o3bqsaeqm"
t_user = "vayxi1dedassxkoasafyy"
t_pw = "98709a53af66ds2118fa05e7cba40416221b7d6b1f44186c36ee31236b720c0b11bbc2911c4"

load_table(file_path, table_name, t_host, t_port, t_dbname, t_user, t_pw)
