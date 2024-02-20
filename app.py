from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_colab', methods=['POST'])
def run_colab():
    os.system('edi1.py')
    return '<script>window.location.href = "https://app.alpaca.markets/account/login";</script>'




if __name__ == '__main__':
    app.run(debug=True)
