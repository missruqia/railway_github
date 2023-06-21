from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')
    return render_template('greet.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')