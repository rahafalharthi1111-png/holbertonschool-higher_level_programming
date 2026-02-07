#!/usr/bin/python3
"""
Task 02: Dynamic template with loops and conditions
"""
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/items")
def items():
    """Render items from JSON file"""
    try:
        with open("items.json", "r") as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run(debug=True)
