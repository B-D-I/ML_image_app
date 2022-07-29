from classification import *
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.errorhandler(500)
def page_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    try:
        if sanity_check():
            image_file = request.files['image_file']
            predict_image_path = "images/" + image_file.filename
            image_file.save(predict_image_path)

            img = set_image(predict_image_path)
            scene = prediction(img)
            if "a building" or "a street" in scene:
                landing = "unsafe"
            else:
                landing = "safe"

            return render_template('index.html', prediction=scene, safe_landing=landing)
        else:
            page_error()
    except Exception as ex:
        page_error(ex)


if __name__ == '__main__':
    app.run(port=3000)
