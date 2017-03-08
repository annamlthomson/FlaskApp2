# -*- coding: utf-8 -*-
from flask import Flask 
from flask import render_template 
from flask import request
import requests


app = Flask("MyApp")

@app.route("/")
def landing():
	return render_template("landing.html")


@app.route("/druginfo", methods=['POST', 'GET'])
def druginfo():
	error = None
	form_data = request.form
	drug_info = form_data['drug']
	drug_info = drug_info.title()
	country_info = form_data['country']
	country_info = country_info.title()
	if request.method == 'POST':
		if country_info == 'Portugal' and drug_info == 'Cannabis':
			return render_template("portugal_cannabis.html")
		else: 
			return render_template("druginfo.html")




app.run()
