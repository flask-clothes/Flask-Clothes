from flask import Flask, render_template, url_for, request, make_response, redirect


app = Flask(__name__)


@app.route("/")
def home: