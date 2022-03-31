from flask import Flask, redirect
from flask import render_template, request, redirect, url_for
from random import choice
import time

app = Flask(__name__)

responses = ["It is certain", "It is decidedly so","Without a doubt" ,"Yes definitely" 
,"Don't rely on it its Matt B's Monday" ,"Please update the standup board" ,"Most likely" ,"Outlook good" ,"Signs point to yes" 
,"Reply hazy, try again" ,"Ask again later" ,"Better not tell you now" ,"Cannot predict now" 
,"Concentrate and ask again" ,"Don't count on it" ,"My reply is no" ,"My sources say no" ,"Outlook not so good" 
,"Very doubtful", "Stick it in the Bling Chat", "Ask Lindsey!", "Tell them raise a CloudOps Request", "Important! Tickets Assigned!!", "Is it Fridaaay yet?"]

@app.route('/',  methods=['GET', 'POST'])
def magic_ball():
    if request.method == 'POST':
        question = request.form.get('question')
        response = choice(responses)
        time.sleep(4)
        return render_template('magic.html', question=question, response=response, responding=True)
    return render_template('magic.html', responding=False)

if __name__ == "__main__":
    app.run(debug=True)
