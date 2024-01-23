from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    quote = "ALL IS WELL"
    return render_template('index.html', quote=quote)

@app.route('/greet/<name>')
def greet(name):
    quote = "ALL IS WELL"
    return render_template('greeting.html', greeting=f"Hello, {name}!", quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
