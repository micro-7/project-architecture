from flask import Flask, render_template #use fapp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) # use froute
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST']) # use froute
def register():
    return render_template('register.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 