import psycopg2
import pandas as pd
import datetime
connection= psycopg2.connect(user="postgres",password="postgres",host='127.0.0.1', port='5432', database="imdb_data")
cursor=connection.cursor()
cursor.execute("select * from label_types")
cursor.execute("INSERT INTO label_types(lable_id,Lable_name,comments) values (%s, %s, %s)",('0', 'positive', 'positive feeling'))
cursor.execute("INSERT INTO label_types(lable_id,Lable_name,comments) values (%s, %s, %s)",('1', 'negative', 'negative feeling'))
cursor.execute("INSERT INTO label_types(lable_id,Lable_name,comments) values (%s, %s, %s)",('2', 'neutral', 'neutral feeling'))
data=pd.read_csv('IMDB Datast.csv')
data['sentiment'].mask(data['sentiment']== 'positive' , '1' , inplace=True)
data['sentiment'].mask(data['sentiment']== 'negative' , '0' , inplace=True)
for row in data.itertuples():
    ID= row.Index
    Text= row.review
    text_date= datetime.datetime.now()
    Text_id=row.Index
    label_id=row.sentiment
    label_date= datetime.datetime.now()
    cursor.execute("INSERT INTO data_input(id,TEXT,date_input) values (%s, %s, %s)",(ID, Text, text_date))
    cursor.execute("INSERT INTO data_labeling(text_id,lable_number,lable_date) values (%s, %s, %s)",(Text_id, label_id, label_date))
    
connection.commit()
cursor.close()