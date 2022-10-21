from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'home'
    # return render_template("index.html")

@app.route('/set')
def set():
    return 'set'
    # return render_template("index.html")

@app.route('/burger')
def burger():
    return 'burger'
    # return render_template("index.html")

@app.route('/side')
def side():
    return 'side'
    # return render_template("index.html")

@app.route('/drink')
def drink():
    return 'drink'
    # return render_template("index.html")

# 인터프리터에서 직접 실행된 경우에만 실행
if __name__ == '__main__':
    app.run(debug=True)