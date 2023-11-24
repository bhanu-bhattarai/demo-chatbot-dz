from flask import Flask, render_template, request
import os
import model
import json
app = Flask(__name__)

@app.route('/')
def information():
   data = {
   "Name":"Bhanu Bhakta Bhattarai",
   "Student Id":"200566953",
   "class":"Conversational AI"
      }
   return render_template('home.html', data=json.dumps(data, indent=4))
	
@app.route('/webhook', methods = ['GET', 'POST'])
def render_image_file():
   if request.method == 'GET':
      return render_template('display.html', img_name="home-renovation.jpg")

@app.route('/back', methods=['POST'])
def go_back():
    return upload_file()

if __name__ == '__main__':
   app.run(debug = True)