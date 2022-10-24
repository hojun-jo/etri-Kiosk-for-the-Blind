from flask import Flask, render_template
import db

app = Flask(__name__)
menu_info = db.menu_info()

@app.route('/')
@app.route('/home')
def home():
    # return 'home'
    return render_template("index.html")

@app.route('/schoolfood')
def set():
    return 'set'
    # return render_template("index.html")

@app.route('/bibimbap')
def burger():
    return 'burger'
    # return render_template("index.html")

@app.route('/porkcutlet')
def side():
    return 'side'
    # return render_template("index.html")

# 인터프리터에서 직접 실행된 경우에만 실행
if __name__ == '__main__':
    app.run(debug=True)