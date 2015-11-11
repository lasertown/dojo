from flask import Flask, render_template, request, redirect, session
import random
import time
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
messages = []


@app.route('/')
def index():
	if session.get('gold'):
		pass
	else:
		session['gold'] = 0
	return render_template("ninjagold.html", messages=messages, gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def function():
	if request.form['building'] == 'farm':
		roll = random.randrange(10, 21)
		session['gold'] += roll
		messages.insert(0,("Earned " + str(roll) + " golds from the farm! " + str(time.strftime("%d/%m/%Y %I:%M %p"))))
	if request.form['building'] == 'cave':
		roll = random.randrange(5, 11)
		session['gold'] += roll
		messages.insert(0,("Earned " + str(roll) + " golds from the cave! " + str(time.strftime("%d/%m/%Y %I:%M %p"))))
	if request.form['building'] == 'house':
		roll = random.randrange(2, 6)
		session['gold'] += roll
		messages.insert(0,("Earned " + str(roll) + " golds from the house!" + str(time.strftime("%d/%m/%Y %I:%M %p"))))
	if request.form['building'] == 'casino':
		roll = random.randrange(-50, 51)
		session['gold'] += roll
		if roll < 0: 
			messages.insert(0,("Entered a casino and lost " + str(roll) + " golds... Ouch.." + str(time.strftime("%d/%m/%Y %I:%M %p"))))
		else:
			messages.insert(0,("Earned " + str(roll) + " golds from the casino!" + str(time.strftime("%d/%m/%Y %I:%M %p"))))
	return redirect('/')
	

app.run(debug=True)
