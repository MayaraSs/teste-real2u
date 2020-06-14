from flask import Flask, render_template
import os
from flask import *
import json
from url_image import (
    download_image,
    save_image,
    apply_filter_blur,  
    get_image_name, 
    open_image,  
    download_image2
)
from flask_cors import CORS
from flask import send_file
import io
import base64
from PIL import Image 

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route("/download-image", methods=['POST'])
def download():
    body = json.loads(request.data)
    url = body["url"]
    name = get_image_name(url)
    download_image2(url)
    return  name

@app.route("/<name>", methods=['GET'])
def show_image(name):
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], name)
    return render_template("index.html", user_image = full_filename)

@app.route("/blur/<name>", methods=['GET'])
def apply_filter(name):
    img = open_image(f"static/{name}")
    image_filter = apply_filter_blur(img)
    save_image('static/image_with_filter.jpg',image_filter)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image_with_filter.jpg')
    return render_template("index.html", user_image = full_filename)

@app.route("/filter", methods=['POST'])
def download_apply_filter():
    body = json.loads(request.data)
    print(body)
    url = body["url"]
    name = get_image_name(url)
    download_image2(url)
    img = open_image(f"static/{name}")
    image_filter = apply_filter_blur(img)
    save_image('static/image_with_filter.jpg',image_filter)
    #convertendo a image em base 64
    img = Image.open('static/image_with_filter.jpg', mode='r')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img

if __name__ == "__main__":
    app.run(debug=True, port=8888)