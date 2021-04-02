from flask import Flask, request, render_template, url_for, redirect
from forms import SpendingsForm
from models import spendings

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route('/spendings/', methods=["GET", "POST"])
def spendings_list():
    form = SpendingsForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            spendings.create(form.data)
            spendings.save_all()
        return redirect(url_for("spendings_list"))

    return render_template("spendings.html", form=form, spendings=spendings.all(), error=error)

if __name__ == "__main__":
    app.run(debug=True)

