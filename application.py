from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():

    data = "Welcome to my website!"

    return render_template("index.html", data=data)

@app.route("/officials")
def officials():

    api_key ="AIzaSyDWsLO3g9HwwlNCmDc_SCOeFJ3Xn7FGVkQ"
    url = "https://www.googleapis.com/civicinfo/v2/representatives"
    address = "244 E 3rd Ave, Columbus OH 43201"
    # address = "1310 Barbie Dr. Youngstown OH 44521"
    # address = "121 st marks place new york new york"

    payload = {'key': api_key, 'address': address}

    req = requests.get(url, params=payload)

    data = req.json()

    officials = data['officials']
    offices = data['offices']

    actual_offices = []

    for office in offices:
        for i in office['officialIndices']:
            actual_offices.append(office)

    return render_template("officials.html",
                           officials=officials,
                           actual_offices=actual_offices)