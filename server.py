from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "NinjaGoldSecretDemo"
import random
from datetime import datetime

@app.route('/')
def index():
    if "totalGold" not in session:
        session['totalGold'] = 0;
    if "adventures" not in session:
        session['adventures'] = []
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process():
    if request.form['building'] == "farm":
        newgold = random.randrange(10, 21)
        print "Visiting the farm", newgold
    elif request.form['building'] == "house":
        newgold = random.randrange(2,6)
        print "Visiting the house", newgold
    elif request.form['building'] == "cave":
        newgold = random.randrange(5, 11)
        print "Visiting the cave", newgold
    elif request.form['building'] == "casino":
        newgold = random.randrange(-50, 51)
        print "Visiting the casino", newgold
    session['totalGold'] += newgold
    time = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    if newgold >= 0:
        adventure = "Visited the {} and earned {} gold. {}".format(request.form['building'], newgold, time)
    else:
        adventure = "Entered the casino and lost {} gold. {}".format(-1 * newgold, time)
    print "*************** adventure", adventure
    session['adventures'].append(adventure)

















    return redirect('/')

app.run(debug = True)
