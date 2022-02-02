from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", num = 3)

@app.route("/<int:num>")
def love_flask_num(num):
    return render_template("index.html", num = num)

@app.route("/play")
def play():
    return render_template("play.html", num_boxes=3)

@app.route("/play/<int:num>")
def play_num(num):
    return render_template("play.html", num_boxes = num)

@app.route("/play/<int:num>/<color>")
def play_num_color(num, color):
    return render_template("play_copy.html", num_boxes = num, color = color)

if __name__ == "__main__":
    app.run(debug=True)