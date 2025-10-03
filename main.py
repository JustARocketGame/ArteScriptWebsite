from flask import Flask, render_template, redirect, send_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/download", methods=["GET"])
def download():
    return redirect("https://github.com/JustARocketGame/ArteScriptDownload/releases/download/last_installer/main.exe")

@app.route("/logo", methods=["GET"])
def logo():
    return send_file("as.png")

if __name__ == "__main__":
    app.run(debug=True)