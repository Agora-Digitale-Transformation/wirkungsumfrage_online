from flask import Flask, render_template, url_for, flash, redirect
from modules.net import plot_spinne_ex

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/example", methods=['GET'])
def example():
    # Run script and pass inputs
    # param = request.args.get("param", default=1, type=int) would get this and pass this to plot_spinne()
    plot = plot_spinne_ex()

    return render_template("example.html", plot=plot)

if __name__ == '__main__':
    app.run(debug=True)