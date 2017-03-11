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
		if country_info == 'Portugal' and drug_info == 'Heroin':
			return render_template("portugal_heroin.html")
		if country_info == 'Portugal' and drug_info == 'Morphine':
			return render_template("portugal_morphine.html")
		if country_info == 'Portugal' and drug_info == 'Opium':
			return render_template("portugal_opium.html")
		if country_info == 'Portugal' and drug_info == 'Crack Cocaine':
			return render_template("portugal_crackcocaine.html")
		if country_info == 'Portugal' and drug_info == 'Cocaine':
			return render_template("portugal_cocaine.html")
		if country_info == 'Portugal' and drug_info == 'Lsd':
			return render_template("portugal_lsd.html")
		if country_info == 'Portugal' and drug_info == 'Mdma':
			return render_template("portugal_mdma.html")
		if country_info == 'Portugal' and drug_info == 'Ecstasy':
			return render_template("portugal_ecstasy.html")
		if country_info == 'Portugal' and drug_info == 'Psilocybin':
			return render_template("portugal_psilocybin.html")
		if country_info == 'Portugal' and drug_info == 'Magic Mushrooms':
			return render_template("portugal_magicmushrooms.html")
		if country_info == 'Portugal' and drug_info == 'Methamphetamine':
			return render_template("portugal_methamphetamine.html")
		if country_info == 'Portugal' and drug_info == 'Crystal Meth':
			return render_template("uk_crystalmeth.html")
		if country_info == 'Uk' and drug_info == 'Cannabis':
			return render_template("uk_cannabis.html")
		if country_info == 'Uk' and drug_info == 'Heroin':
			return render_template("uk_heroin.html")
		if country_info == 'Uk' and drug_info == 'Morphine':
			return render_template("uk_morphine.html")
		if country_info == 'Uk' and drug_info == 'Opium':
			return render_template("uk_opium.html")
		if country_info == 'Uk' and drug_info == 'Crack Cocaine':
			return render_template("uk_crackcocaine.html")
		if country_info == 'Uk' and drug_info == 'Cocaine':
			return render_template("uk_cocaine.html")
		if country_info == 'Uk' and drug_info == 'Lsd':
			return render_template("uk_lsd.html")
		if country_info == 'Uk' and drug_info == 'Mdma':
			return render_template("uk_mdma.html")
		if country_info == 'Uk' and drug_info == 'Ecstasy':
			return render_template("uk_ecstasy.html")
		if country_info == 'Uk' and drug_info == 'Psilocybin':
			return render_template("uk_psilocybin.html")
		if country_info == 'Uk' and drug_info == 'Magic Mushrooms':
			return render_template("uk_magicmushrooms.html")
		if country_info == 'Uk' and drug_info == 'Methamphetamine':
			return render_template("uk_methamphetamine.html")
		if country_info == 'Uk' and drug_info == 'Crystal Meth':
			return render_template("uk_crystalmeth.html")
		else: 
			return render_template("druginfo.html")




app.run()
