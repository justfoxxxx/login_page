from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def IndexView():
    render_template 

if __name__ == '__main__':
    app.run(debug=True, host='0. 0. 0. 0', port='0808') 