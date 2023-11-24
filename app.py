from flask import Flask, render_template, request, make_response, jsonify
import os
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
	
@app.route('/webhook', methods = ['POST'])
def render_image_file():
   return make_response(jsonify({'fulfillmentText': "DEZED RENOS - Thank You For contacting us."}))

if __name__ == '__main__':
   app.run(debug = True)