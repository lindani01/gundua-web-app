"""
The flask application package.
"""

from flask import Flask,render_template
app = Flask(__name__)

#import FlaskWebProject1.views

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
