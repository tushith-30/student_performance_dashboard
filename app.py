from flask import Flask, render_template, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    return df

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analytics")
def analytics():
    df = get_data()

    average = df["marks"].mean()
    topper = df.loc[df["marks"].idxmax()]["name"]
    pass_percentage = (df[df["marks"] >= 40].shape[0] / df.shape[0]) * 100
    subject_avg = df.groupby("subject")["marks"].mean().to_dict()

    return jsonify({
        "average": round(average, 2),
        "topper": topper,
        "pass_percentage": round(pass_percentage, 2),
        "subject_avg": subject_avg
    })

if __name__ == "__main__":
    app.run(debug=True)