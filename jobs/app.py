from flask import Flask, render_template


app = Flask(__name__)

@route(URL='/')
def jobs():
    return render_template('index.html')