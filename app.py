from flask import Flask, render_template, request
from openpyxl import load_workbook
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():

        return "Tchau"


if __name__ == "__main__":
    app.run()
