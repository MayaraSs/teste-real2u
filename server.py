from flask import Flask, render_template
from flask import *
import json
from url_image import download_image, get_image_name, open_image,  download_image2


app = Flask(__name__)


@app.route("/download-image", methods=['POST'])
def download():
    print(request.data)
    body = json.loads(request.data)
    url = body["url"]
    name = get_image_name(url)
    download_image2(url)
    return  name

@app.route("/<name>", methods=['GET'])
def show_image(name):
    print(name)
    img = open_image(str(name))
    print(img)
    return render_template("index.html", user_image = name)
    
if __name__ == "__main__":
    app.run(debug=True)