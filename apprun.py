# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:32:44 2019

@author: armazumd
"""

from flask import Flask
from linkedin_api import Linkedin
from flask import jsonify
app = Flask(__name__)

from flask import Flask
from flask import request
import json
app = Flask(__name__)
  
@app.route('/connections', methods = ['POST'])
def postJsonHandler():
  content = request.get_json()
  api = Linkedin(content['email'],content['password'])
  connections=api.search_people(network_depth ='F',limit=5)
  querry=[]
  for item in connections:
    data = {}
    value = item['urn_id']
    retrieve=api.get_profile(value)
    name=retrieve['firstName']+' '+retrieve['lastName']
    link='https://www.linkedin.com/in/'+item['public_id']+'/'
    data['name'] = name
    data['link']=link
    querry.append(data)
    
  return jsonify(querry)

if __name__ == '__main__':
    app.run(debug=True)
