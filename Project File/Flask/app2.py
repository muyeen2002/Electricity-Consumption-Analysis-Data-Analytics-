# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 09:31:25 2023

@author: ramya
"""

from flask import Flask, render_template, request                     
app = Flask(__name__,template_folder="templates")          
                                                          
@app.route("/")
def hello():
    user='chandu'
    return render_template('home.html',user=user) 

if __name__ == "__main__":
     app.run(debug=True ,port=8080,use_reloader=False) 