from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
import asyncio
from threading import Thread
import json
import discord
from discord.ext import commands
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'
users = []
app = Flask('')
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.errorhandler(404)
def page_not_found(e):
  return render_template('erro404.html'), 404

        

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()
