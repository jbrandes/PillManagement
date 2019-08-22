from flask import Flask, request
from flask import Flask, Response
from flask import send_file, send_from_directory, safe_join, abort
import requests

def prompt():
    


def medRequest():
    

URL = 'https://api.fda.gov/drug/event.json?search=receivedate:[20040101+TO+20160601]&count=receivedate'

data = requests.get(URL).json()

for result in data.get('results', []):
  print(result)


@app.route('/')
def home():
    render_template('index.html', name=name)
  
@app.route('/Monday', methods=['POST', 'GET'])
def Monday():
   
        
@app.route('/Tuesday', methods=['POST', 'GET'])
def Tuesday():
   
@app.route('/Wednesday', methods=['POST', 'GET'])
def Wednesday():
    
@app.route('/Thursday', methods=['POST', 'GET'])
def Thursday():
    
@app.route('/Friday', methods=['POST', 'GET'])
def Friday():
   
@app.route('/Saturday', methods=['POST', 'GET'])
def Saturday():
   
@app.route('/Sunday', methods=['POST', 'GET'])
def Sunday():
   
   
   

if __name__ == '__main__':
    app.run(port=5000,debug=True) 

