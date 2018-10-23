import random
from werkzeug.routing import BaseConverter
from flask import Flask, jsonify, request, json, session, render_template, redirect, url_for, Response
import final_model

app = Flask(__name__)

@app.route('/upload')
def upload_temp():
   return render_template('upload.html')

import time
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   print("Work")
   if request.method == 'POST':
      print("POST")
      f = request.files['file']
      f.save(f.filename)
      # message = final_model.get_result(f.filename)
      # print(message)
      return render_template('check.html')
   else:
       print("GET")

@app.route('/checker', methods = ['GET', 'POST'])
def check_file():
   if request.method == 'POST':
      print("POST")
      print(request.form['input'])
      message = final_model.get_result(request.form['input'])
      print(message)
      if(message=="0"):
          return "Cooking"
      elif(message=="1"):
          return "Dance"
      else:
        return "Sports"

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host="192.168.43.171",port=8000,debug=False, threaded=False)
