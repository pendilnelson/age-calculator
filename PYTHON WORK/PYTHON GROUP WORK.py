from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

# Simple HTML form inside a template string
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Age Calculator</title>
</head>
<body style="font-family: Arial; margin: 50px;">
    <h2>Age Calculator</h2>
    <form method="post">
        <label for="dob">Enter your Date of Birth:</label><br><br>
        <input type="date" name="dob" required>
        <button type="submit">Calculate Age</button>
    </form>
    {% if age is not none %}
        <h3>Your Age: {{ age }} years</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        dob_str = request.form["dob"]
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        # Calculate age in years
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return render_template_string(HTML_TEMPLATE, age=age)

if __name__ == "__main__":
    app.run(debug=True)
