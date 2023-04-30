from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
application = Flask(__name__, static_folder='static')
app = application

@application.route('/',methods=['GET','POST'])
@cross_origin() # its purpose is to be available to different countries
def index():
    return render_template("landing.html")
@application.route('/gpt',methods=['GET','POST'])
@cross_origin() # its purpose is to be available to different countries
def index1():
    import os
    import openai
    openai.api_key ="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"
    input_text = request.form['input-field']
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": input_text}
      ]
    )

    output_text=completion.choices[0].message['content']
    return render_template('landing.html',output=output_text)



if __name__ == '__main__':
    application.run(debug=True)