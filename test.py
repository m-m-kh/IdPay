from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/callback/',methods=['get'])
def callback():
    print(request.args)
    return 'wda'
    
app.run()