#2023
from flask import Flask
from flask import request, render_template
import textblob
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    return(render_template('index.html'))

@app.route("/main", methods = ["GET", "POST"])
def main():
    name = request.form.get("q")
    return(render_template('main.html'))

@app.route("/SA", methods = ["GET", "POST"])
def SA():
    return(render_template('SA.html'))

@app.route("/SA_result", methods = ["GET", "POST"])
def SA_result():
    q = request.form.get('q')
    r = textblob.TextBlob(q).sentiment
    return(render_template('SA_result.html',r=r))


@app.route("/AI", methods = ["GET", "POST"])
def AI():
    return(render_template('GenAI.html'))

@app.route("/AI_result", methods = ["GET", "POST"])
def AI_result():
    
    api = os.getenv("makersuite")
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")

    q = request.form.get('q')
    r = model.generate_content(q)
    return(render_template('GenAI_result.html',r=r))


if __name__=="__main__":
    app.run()
