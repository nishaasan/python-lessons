from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store votes
votes = {'coffee': 0, 'tea': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    # Update vote count based on the form submission
    selected_option = request.form.get('vote')
    print(selected_option,votes)
    if selected_option in votes:
        votes[selected_option] += 1
    return redirect(url_for('index'))

@app.route('/result')
def result():
    return render_template('results.html', votes=votes)

if __name__ == '__main__':
    app.run(debug=True,port=2000)
