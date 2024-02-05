from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
    image_path = 'img.jpg'
    return send_file(image_path, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run()
