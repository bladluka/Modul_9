from flask import Flask, render_template, request
import requests, csv

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0]['rates']
with open('currency.csv', 'w') as csvfile:
    currencywriter = csv.writer(csvfile, delimiter=';')
    currencywriter.writerows(rate.values() for rate in rates)
    csvfile.close()

def calculation(currency, amount):
    amounts = int(amount)
    for rate in rates:
        values = [rate["currency"], rate["code"], rate["bid"], rate["ask"]]
        if values[1] == currency:
            return round((amounts * rate["ask"]), 2)

@app.route("/", methods=["GET", "POST"])
def currency():
    if request.method == "POST":
        source = request.form
        currency = source.get("currency")
        amount = source.get("amount")
        ask = calculation(currency, amount)
        return render_template("currency.html", ask=ask)

    return render_template("currency.html")

if __name__ == "__main__":
    app.run(debug=True)






