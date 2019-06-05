from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("hello.html", message="天才")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        comment = request.form['comment']
        comment2 = request.form['comment2']
        data = comment + comment2



    return render_template("result.html", prediction = data)



if __name__ == '__main__':
    app.run()
