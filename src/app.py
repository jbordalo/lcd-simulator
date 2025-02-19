from flask import Flask, render_template, request, send_file
from tft_lcd import TFT_LCD
import base64
from colors import colors_map

app = Flask(__name__)


def generate_image(code):
    try:
        tft = TFT_LCD(128, 160)
        exec(code, {"tft": tft, **colors_map})
    except Exception as e:
        print(f"Error: {e}")

    return tft.show(display=False)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form["code"]
        img_io = generate_image(code)
        return send_file(img_io, mimetype="image/png")

    # Hack for simplicity
    tft = TFT_LCD(128, 160)
    tft.fill_screen("black")

    img_io = tft.show(display=False)
    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    img_url = f"data:image/png;base64,{img_base64}"

    return render_template("index.html", img_url=img_url)

if __name__ == "__main__":
    app.run(debug=True)
