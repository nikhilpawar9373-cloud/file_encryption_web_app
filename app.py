from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Secret Key Generate
key = Fernet.generate_key()
cipher = Fernet(key)

@app.route("/", methods=["GET", "POST"])
def home():
    encrypted_text = ""
    if request.method == "POST":
        user_text = request.form["text"]
        encrypted_text = cipher.encrypt(user_text.encode()).decode()
    return render_template("index.html", encrypted_text=encrypted_text)

if __name__ == "__main__":
    app.run(debug=True)
