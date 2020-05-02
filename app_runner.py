# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:27:55 2020

@author: dm226t
"""
from flask import Flask, render_template, request, jsonify
import json

app=Flask(__name__)

@app.route('/')
def get_ui():
    return render_template('amazon_phones.html')

@app.route("/post/<int:post_id>")
def post(post_id):
  return "<h2> Post ID is, %s </h2>" %post_id


@app.route('/process', methods=['POST'])
def process():
    
    name = request.form['name']
    if name:
        app.


if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000)
    
    