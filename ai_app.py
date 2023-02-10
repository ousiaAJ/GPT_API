import os
import openai
import json
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
  auftrag = request.form["textinput"]
  if auftrag:
      result = gpt(auftrag)
      return render_template("result.html", result=result)
  else:
      return render_template("index.html")





def gpt(auftrag):
  print("API started")
  openai.api_key = "<key>"

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=auftrag,
    temperature=0.6,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
  )
  json_object = json.loads(str(response))
  answer = json_object['choices'][0]['text']
  return answer

if __name__ == '__main__':
    app.run(debug=True)
