import os
import openai
from flask import Flask, request, render_template
from config import OPENAI_API_KEY

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
            messages=[ {"role": "system", "content": "You are Habibi Bot, a muslim sharing helpful tips from the Quran and Sunnah"},
           {"role": "user", "content": message}], 
           temperature=0, max_tokens=500)
        return render_template("index.html", response=response.choices[0].message.content)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
