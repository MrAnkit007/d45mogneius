import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'MrAnkit007'

os.system("git clone https://MrAnkit007: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@github.com/MrAnkit007/BBBot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")
