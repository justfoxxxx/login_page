from flask import Flask, render_template, url_for, session, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['secret_key'] = 'A_D(AS)+_(DAS_+)DA_+D'




@app.route('/', methods=['GET', 'POST'])
def IndexView():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080') 