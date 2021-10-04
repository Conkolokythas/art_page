from flask import Flask, render_template, session, jsonify

app = Flask(__name__)
app.secret_key = "portfolio_page"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/bio')
def bio():
    return render_template("bio.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/change_lang')
def en():
    if session["lang"] == "gr":
        session["lang"] = "en"
        return jsonify("gr")
    elif session["lang"] == "en":
        session["lang"] = "gr"
        return jsonify("en")


@app.route('/check_lang', methods=["GET", "POST"])
def check_lang():
    if not session:
        session["lang"] = "gr"
        return jsonify(session["lang"])
    elif session:
        return jsonify(session["lang"])


if __name__ == "__main__":
    app.run(debug=True)