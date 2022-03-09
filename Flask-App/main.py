from flask import Flask
from flask import render_template, request
from random import choice

app = Flask(__name__)

responses = ["It is certain.", "It is decidedly so.","Without a doubt." ,"Yes definitely." 
,"You may rely on it." ,"As I see it, yes." ,"Most likely." ,"Outlook good" ,"Yes." ,"Signs point to yes" 
,"Reply hazy, try again" ,"Ask again later." ,"Better not tell you now." ,"Cannot predict now." 
,"Concentrate and ask again" ,"Don't count on it." ,"My reply is no." ,"My sources say no." ,"Outlook not so good." 
,"Very doubtful."]

@app.route('/',  methods=['GET', 'POST'])
def magic_ball():
    if request.method == 'POST':
        question = request.form.get('question')
        response = choice(responses)
        return render_template('magic.html', question=question, response=response, responding=True)
    return render_template('magic.html', responding=False)
    
if __name__ == "__main__":
    app.run(debug=True)
