from flask import Flask, render_template_string, request
from datetime import datetime

app = Flask(__name__)

# Updated colorful HTML template
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Age Calculator</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
            text-align: center;
            width: 420px;
        }
        h2 {
            font-size: 32px;
            margin-bottom: 20px;
            color: #ffdd57;
        }
        label {
            font-size: 18px;
        }
        input[type="date"] {
            margin: 15px 0;
            padding: 12px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            background: #ffdd57;
            color: #333;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s ease;
        }
        button:hover {
            background: #ffb400;
            transform: scale(1.05);
        }
        h3 {
            margin-top: 20px;
            font-size: 22px;
            color: #00ffcc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎉 Age Calculator 🎂</h2>
        <form method="post">
            <label for="dob">Enter your Date of Birth:</label><br><br>
            <input type="date" name="dob" required>
            <br>
            <button type="submit">Calculate Age</button>
        </form>
        {% if years is not none and days is not none %}
            <h3>Your Age: {{ years }} years and {{ days }} days</h3>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    years, days = None, None
    if request.method == "POST":
        dob_str = request.form["dob"]
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        today = datetime.today().date()

        # Total days lived
        total_days = (today - dob).days

        # Years
        years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Remaining days (after full years)
        last_birthday = dob.replace(year=today.year if (today.month, today.day) >= (dob.month, dob.day) else today.year - 1)
        days = (today - last_birthday).days

    return render_template_string(HTML_TEMPLATE, years=years, days=days)

if __name__ == "__main__":
    app.run(debug=True)
