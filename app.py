from flask import Flask, render_template, request
import pandas as pd
import pickle
from crawl import resell
import datetime

import os
import psycopg2
import sqlite3

DB_FILENAME = 'datadb.db'
DB_FILEPATH = os.path.join(os.getcwd(), DB_FILENAME)

conn = sqlite3.connect(DB_FILENAME) #없으면 자동생성
cur = conn.cursor()

cur.execute("select * from priceBytime")

data=[]
rows = cur.fetchall()
for row in rows:
    data.append(list(row))

with open("rf_model.pkl","rb") as fr:
   boosting = pickle.load(fr)

app = Flask(__name__)
   
@app.route('/',methods = ['GET','POST'])
def home(): 
   # return render_template('blog.html',data=data)
   if request.method == 'GET':
      return render_template('blog.html')
   
   elif request.method == 'POST':
      value=abc()
      return render_template('blog.html',
                              names=value,
)
  
@app.route('/result',methods = ['GET','POST'])
def result():
   

   if request.method == 'POST':
      result = request.form
      print(request.form)
      result=result.to_dict(flat=False)
      # print(result['발매일'])


      date = result['발매일'][0].split('/')
      dateToday = datetime.date(int(date[2]), int(date[0]), int(date[1]))
      toOrdinal = dateToday.toordinal()  

      date = result['주문일'][0].split('/')
      dateToday = datetime.date(int(date[2]), int(date[0]), int(date[1]))
      toOrdinal2 = dateToday.toordinal()

      time = toOrdinal2 - toOrdinal
      print(toOrdinal2)
      test = pd.DataFrame({'Order_date':toOrdinal2,
                           'Retail_Price':result['소매가'],
                                 'time_gap': time,                                 
                                 'Sneaker_Name_Adidas Yeezy Boost':0.0,
                                 'Sneaker_Name_Air Jordan 1':0.0,
                                 'Sneaker_Name_Nike Air Force':0.0,
                                 'Sneaker_Name_Nike Air Max':0.0,
                                 'Sneaker_Name_Nike Air Presto':0.0,
                                 'Sneaker_Name_Nike Air VaporMax':0.0,
                                 'Sneaker_Name_Nike Blazer Mid':0.0,
                                 'Sneaker_Name_Nike React Hyperdunk':0.0,
                                 'Sneaker_Name_Nike Zoom Fly':0.0,
                                 'Brand_Adidas':0.0,
                                 'Brand_Jordan':0.0,
                                 'Brand_Nike':0.0,                                 
                                 })
      print('여기')
      lists = ['Brand_Adidas','Brand_Jordan'	,'Brand_Nike']                       
      list2 = [ 'Sneaker_Name_Adidias Yeezy Boost', 'Sneaker_Name_Air Jordan 1', 'Sneaker_Name_Nike Air Force', 'Sneaker_Name_Nike Air Max', 'Sneaker_Name_Nike Air Presto', 'Sneaker_Name_Nike Air VaporMax','Sneaker_Name_Nike Blazer Mid', 'Sneaker_Name_Nike React Hyperdunk', 'Sneaker_Name_Nike Zoom Fly']             
      for i in lists:
         if result['브랜드'][0] == i:
            test[result['브랜드']] = 1.0
            print(i)
            break

      for j in list2:
         if result['상품명'][0] == j:
            test[result['상품명']] = 1.0
            print(i)
            break
         
      student_card = pd.DataFrame({'Retail_Price':result['Retail_Price'],
                                 'Shoe_Size':result['Shoe_Size'],
                                 'time_gap':result['time_gap'],
                                 'adidas':result['adidas'],#10개
                                 'boost':result['boost'],
                                 '350':result['350'],
                                 'yeezy':result['yeezy'],
                                 'v2':result['v2'],
                                 'white':result['white'],
                                 'off':result['off'],
                                 'nike':result['nike'],
                                 'air':result['air'],
                                 'blue':result['blue']})
      
      X_tests_encoded = encoder.transform(student_card)  
      
      pd.set_option('display.max_columns', 20)
      print(test)
      result2=int(boosting.predict(test))#-int(result['소매가'][0])
      
      return render_template("cover.html",result = result2)
      
if __name__ == "__main__":
    app.run(debug=True)
    