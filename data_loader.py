import csv
import configparser
import pymysql as sql
import time
import shutil
#from data_gen import dt_string
import pandas as pd
import threading
import os
import datetime
import glob

print("Data loader")
#print(dt_string)
config = configparser.ConfigParser()
config.read('db.ini')
host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']
conn=sql.connect(host=host,port=3306,user=user,password=passwd, db=db)
cursor=conn.cursor()
folder_name = 'gen_process'
file_type = 'csv'
seperator =','
new_path='C:/Users/srika/PycharmProjects/gen_process/processed/success'
fail_path='C:/Users/srika/PycharmProjects/gen_process/processed/failed'
count=0
while True:
    for files in glob.glob("*.csv"):
        print(files)
        sql_script = "INSERT INTO gen_table( random_int, random_str, random_date, name_of_file) VALUES(%s, %s, %s, %s)"
        current_path=files
        # Insert into the fileTable
        filename=files
        count+=1
        process_name=count
        process_date=datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        message='In-Progress'
        insert="INSERT INTO log_table( process_name, file_name, message, process_date) VALUES (%s, %s, %s, %s)"
        insert_values=(str(process_name),str(filename),str(message),str(process_date))
        cursor.execute(insert,insert_values)
        conn.commit()

        with open(files) as csv_file:
            # l_num_rows = csv_file%rowcount

            # insert into fileTable -> l_fileid,csv_file,'in-progress',l_num_rows

            csv_reader = csv.reader(csv_file, delimiter=',')
            pdd=pd.read_csv(files)
            l_num_rows=len(pdd.axes[0])+1
            print("l_num_rows")
            print(l_num_rows)


            for row in csv_reader:
                print(row)
                sql_insert_script=sql_script + '(' + row[0] + ',' + row[1] + ',' + row[2]+ ');'
                values=(int(row[0]),str(row[1]),str(row[2]),str(files))

                try:
                    cursor.execute(sql_script,values)
                except:
                    pass
                    # log error in log file
            conn.commit()
            count_query="select count(*) from gen_table where name_of_file = %s"
            count_val=(str(files))
            cursor.execute(count_query,count_val)
            l_tab=cursor.fetchone()
            l_tab_rows=l_tab[0]
            print("l_tab_rows")
            print(l_tab_rows)
            print(type(l_tab_rows))

            #conn.commit()

        # validation

        if l_tab_rows == l_num_rows:
            #SQL -> update fileTable set status = 'success' where      where file_id = "+ l_fileid)
            update_query = """update log_table set message = %s where process_name = %s"""
            val=('success',str(process_name))
            cursor.execute(update_query,val)
            conn.commit()
            shutil.move(files, new_path)
            print("success")
        elif l_num_rows != 10 or l_tab_rows != l_num_rows:
            #SQL -> update fileTable set status = 'failed' where      where file_id = "+ l_fileid)
            update_query = """update log_table set message = %s where process_name = %s"""
            val1=('failed',str(process_name))
            cursor.execute(update_query,val1)
            conn.commit()

            shutil.move(files, fail_path)
            print("failed")


        # Move File to /processed/success or /processed/failed
        #shutil.move(files, new_path)



    time.sleep(15)
cursor.close()
