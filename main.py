from flask import Flask, render_template
import pandas as pd

# Create a website object
app = Flask(__name__)


# Connect html pages with website object
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

# Give a specific port name to be able to run multiple Flask apps
# E.g. port 5001
# Avoids clashes between app running at the same time
if __name__ == "__main__":
    app.run(debug=True)