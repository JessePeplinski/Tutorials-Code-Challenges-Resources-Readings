from flask import Flask

app = Flask(__name__) # Gives each file a unique name

@app.route('/') # 'http://www.google.com/ - homepage
def home():
    return "Hello world!"

app.run(port=5000)
